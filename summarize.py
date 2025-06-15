from langchain.llms import OpenAI

llm = OpenAI(temperature=0.3)

def run(text: str):
    prompt = f"Summarize the following:\n\n{text}"
    summary = llm(prompt)
    return {"summary": summary}

