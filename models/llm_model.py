from langchain_groq import ChatGroq
from config import Config


def create_llm_model():
    model = ChatGroq(api_key=Config.GROQ_API_KEY,
                     model=Config.MODEL_NAME,
                     temperature=Config.TEMPERATURE,
                     streaming=False,
                     verbose=True)
    return model