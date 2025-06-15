def reporter_agent(state) -> dict:
    report = "\n\n".join(f"Paper {i+1} Summary:\n{sm}"
                         for i, sm in enumerate(state["summaries"]))
    return {"report": report}
