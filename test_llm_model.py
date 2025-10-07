from models.llm_model import create_llm_model

model = create_llm_model()
respopnse = model.invoke("Hello, how are you?").content

print(respopnse)