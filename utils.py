from langchain_openai import ChatOpenAI
from langchain_classic.chains import ConversationChain
def get_chat_response(prompt,memory,openai_key):
    model=ChatOpenAI(model="gpt-5.5",base_url="https://xcode.best/v1",
                     api_key=openai_key)
    chain=ConversationChain(llm=model,memory=memory)
    response=chain.invoke({"input":prompt})
    return response["response"]
