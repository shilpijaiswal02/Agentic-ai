IMPORTANT_CLAUSES = {
    "Data Sharing": ["share", "third party"],
    "Arbitration": ["arbitration"],
    "Auto Renewal": ["renew", "subscription"],
    "Liability": ["liability", "not responsible"]
}

def extract_clauses(text: str):
    found = []
    text_lower = text.lower()

    for clause, keywords in IMPORTANT_CLAUSES.items():
        for word in keywords:
            if word in text_lower:
                found.append(clause)
                break

    return found
