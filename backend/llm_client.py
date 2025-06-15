from bs4 import BeautifulSoup

def summarize_website(html_text):
    soup = BeautifulSoup(html_text, "html.parser")

    # Extract title
    title = soup.title.string.strip() if soup.title and soup.title.string else "No title found"

    # Extract meta description
    description_tag = soup.find("meta", attrs={"name": "description"})
    description = description_tag["content"].strip() if description_tag and "content" in description_tag.attrs else "No meta description found"

    # Extract top headings (h1, h2)
    headings = [h.get_text(strip=True) for h in soup.find_all(["h1", "h2"])][:5]
    heading_text = ", ".join(headings) if headings else "No major headings found"

    # Construct the summary
    summary = (
        f"The website titled '{title}' includes the following key sections: {heading_text}. "
        f"Meta description: {description}."
    )
    return summary


def generate_issue_analysis(html_text):
    soup = BeautifulSoup(html_text, "html.parser")
    issues = []

    # Check title
    if not (soup.title and soup.title.string.strip()):
        issues.append("Missing title tag.")

    # Check meta description
    description_tag = soup.find("meta", attrs={"name": "description"})
    if not (description_tag and "content" in description_tag.attrs and description_tag["content"].strip()):
        issues.append("Missing meta description.")

    # Check SSL - note: this requires external validation, so just simulate for now
    issues.append("No SSL security.")  # In real use, check domain starts with https

    # Check for missing image alt tags
    images = soup.find_all("img")
    if any(not img.get("alt") for img in images):
        issues.append("No alt tags for some images.")

    # Check for structured data (e.g., schema.org JSON-LD)
    if not soup.find("script", type="application/ld+json"):
        issues.append("No structured data found.")

    return "\n".join(issues)


def generate_structured_email(name, summary, issues):
    return {
        "name": name,
        "summary": summary,
        "issues": issues
    }
