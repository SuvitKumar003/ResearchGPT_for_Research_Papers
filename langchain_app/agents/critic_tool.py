from langchain.agents import tool
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

@tool
def critique_summary(summary: str) -> str:
    """Critiques the quality of a summary."""
    prompt = PromptTemplate.from_template("Evaluate and improve this summary:\n\n{summary}")
    llm = HuggingFaceHub(repo_id="google/flan-t5-large", model_kwargs={"temperature": 0})
    chain = LLMChain(llm=llm, prompt=prompt)

    return chain.run(summary)
