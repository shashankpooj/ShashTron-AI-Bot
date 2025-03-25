from langchain_google_genai import GoogleGenerativeAI
from langchain.schema import(
    SystemMessage,
    HumanMessage,
    AIMessage
)
import streamlit as st
from streamlit_chat import message


from dotenv import load_dotenv

# Manually specify the path to .env
env_path = r"C:\Users\DEEKSHA B POOJARY\OneDrive\Documents\Udemy course\.env"
load_dotenv(env_path, override=True)

st.set_page_config(
    page_title='Your Custom Assistant',
    page_icon='🤖'

)

st.subheader('ShashTron AI 🤖')
chat=GoogleGenerativeAI(model="gemini-2.0-flash",temperature=0.5)
if 'messages' not in st.session_state:
    st.session_state.messages=[]


with st.sidebar:
    system_message=st.text_input(label='System role')
    user_prompt=st.text_input(label='Send a message')
    if system_message:
        if not any(isinstance(x,SystemMessage) for x in st.session_state.messages):
            st.session_state.messages.append(
                SystemMessage(content=system_message)
        )
            
    

    if user_prompt:
        st.session_state.messages.append(
            HumanMessage(content=user_prompt)
        )

    with st.spinner('Working on your request...'):
        response = chat.invoke("\n".join(msg.content for msg in st.session_state.messages if isinstance(msg, (SystemMessage, HumanMessage))))

        
    st.session_state.messages.append(AIMessage(content=response))

# st.session_state.messages
    
# message('this is  ShashTron AI',is_user=False)
# message('this is the user',is_user=True)
if len(st.session_state.messages)>=1:
    if not isinstance(st.session_state.messages[0],SystemMessage):
        st.session_state.messages.insert(0,SystemMessage(content='You are a helpful assistant.'))


for i,msg in enumerate(st.session_state.messages[1:]):
    if i%2==0:
        message(msg.content,is_user=True,key=f'{i} + 👽')
    else:
        message(msg.content,is_user=False,key=f'{i} + 🤖')

