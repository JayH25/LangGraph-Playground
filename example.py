#  how to setup llm model

from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
  repo_id="meta-llama/Meta-Llama-3-8B-Instruct",

  task = "text-generation"
)

model = ChatHuggingFace(llm = llm)
result = model.invoke("who is the prime minister of india ?")