def audit_website(info, domain):
    issues = []
    suggestions = []

    if not info.get("title"):
        issues.append("Missing <title> tag.")
        suggestions.append("Add a relevant <title> tag to improve SEO.")

    if not info.get("meta_description"):
        issues.append("Missing meta description.")
        suggestions.append("Add a meta description for better search engine indexing.")

    if not domain.startswith("https://"):
        issues.append("Site is not secured with SSL.")
        suggestions.append("Enable HTTPS to secure your website.")

    return {
        "summary": f"The site at {domain} was analyzed for basic SEO and accessibility issues.",
        "issues": issues,
        "suggestions": suggestions,
        "fomo": "Sites with poor SEO and no SSL often lose traffic and trust. Let us help you fix that before it impacts your business."
    }
