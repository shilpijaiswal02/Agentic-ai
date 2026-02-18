from Agents.summarize_agent import summarize
from Agents.clauseAgent import extract_clauses
from Agents.riskAgent import detect_risk

def run_pipeline(text: str):
    summary = summarize(text)
    clauses = extract_clauses(text)

    risks = []
    for clause in clauses:
        risks.append({
            "clause": clause,
            "risk": detect_risk(clause, text)
        })

    return {
        "summary": summary,
        "risks": risks
    }
