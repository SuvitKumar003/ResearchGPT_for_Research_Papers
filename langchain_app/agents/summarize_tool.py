from langchain.agents import tool
from langchain.llms import HuggingFaceHub
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

@tool
def summarize_text(text: str) -> str:
    """Summarizes a given text using HuggingFace LLM."""
    template = "Summarize the following text:\n\n{text}"
    prompt = PromptTemplate.from_template(template)

    llm = HuggingFaceHub(repo_id="google/flan-t5-large", model_kwargs={"temperature": 0})
    chain = LLMChain(llm=llm, prompt=prompt)

    return chain.run(text)
