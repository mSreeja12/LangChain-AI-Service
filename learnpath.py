from langchain.llms import OpenAI

llm = OpenAI(temperature=0.5)

def run(topic: str):
    prompt = f"Create a learning path for the topic: {topic}."
    roadmap = llm(prompt)
    return {"learning_path": roadmap}
