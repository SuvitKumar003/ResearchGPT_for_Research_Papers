from langchain.agents import tool
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

@tool
def synthesize_insights(data: str) -> str:
    """Combines insights into a final research summary."""
    prompt = PromptTemplate.from_template("Create a final research insight from:\n\n{data}")
    llm = HuggingFaceHub(repo_id="google/flan-t5-large", model_kwargs={"temperature": 0})
    chain = LLMChain(llm=llm, prompt=prompt)

    return chain.run(data)
