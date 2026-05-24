import streamlit as st
from langchain_classic.memory import ConversationBufferMemory

from utils import *

# 设置网页标题
st.title("💬 克隆ChatGPT")

# 侧边栏用于输入 OpenAI API Key
with st.sidebar:
    openai_api_key = st.text_input("请输入OpenAI API Key：", type="password")
    st.markdown("[获取OpenAI API key](https://xcode.best)")

# 首次进入页面时，初始化对话记忆和聊天记录
if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role": "ai",
                                     "content": "你好，我是你的AI助手，有什么可以帮你的吗？"}]

# 将历史聊天记录显示在页面上
for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

# 获取用户在聊天输入框中输入的问题
prompt = st.chat_input()
if prompt:
    # 没有 API Key 时提示用户输入，并停止继续执行
    if not openai_api_key:
        st.info("请输入你的OpenAI API Key")
        st.stop()

    # 保存并显示用户消息
    st.session_state["messages"].append({"role": "human", "content": prompt})
    st.chat_message("human").write(prompt)

    # 调用工具函数获取 AI 回复
    with st.spinner("AI正在思考中，请稍等..."):
        response = get_chat_response(prompt, st.session_state["memory"],
                                     openai_api_key)

    # 保存并显示 AI 回复
    msg = {"role": "ai", "content": response}
    st.session_state["messages"].append(msg)
    st.chat_message("ai").write(response)
