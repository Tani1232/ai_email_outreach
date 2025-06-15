from input_handler import read_email_list
from scraper import scrape_website
from audit import audit_website
from llm_client import summarize_website, generate_issue_analysis, generate_structured_email
from email_generator import generate_email
from email_sender import send_email
from logger import log_status

def run_audit_pipeline():
    file_path = "email_list.csv"
    contacts = read_email_list(file_path)

    if not contacts:
        return {"error": "No contacts found. Check your CSV file."}

    all_results = []

    for contact in contacts:
        email = contact['email']
        first_name = contact.get('first_name', '')
        last_name = contact.get('last_name', '')
        name = f"{first_name} {last_name}".strip()
        domain = contact['domain']

        try:
            info = scrape_website(domain)
            audit_results = audit_website(info, domain)

            html_text = info.get("html", "")
            if not html_text:
                all_results.append({
                    "email": email,
                    "domain": domain,
                    "mail_sent": False,
                    "summary": None,
                    "issues": [],
                    "error": "No HTML content found."
                })
                continue

            summary = summarize_website(html_text)
            issues = generate_issue_analysis(html_text).split("\n")[:5]
            llm_structured = generate_structured_email(name, summary, issues)

            if llm_structured:
                email_html = generate_email(llm_structured)
                send_email(
                    to_email=email,
                    subject="Quick Website Audit for Your Site",
                    content=email_html
                )
                all_results.append({
                    "email": email,
                    "domain": domain,
                    "mail_sent": True,
                    "summary": summary,
                    "issues": issues
                })
            else:
                all_results.append({
                    "email": email,
                    "domain": domain,
                    "mail_sent": False,
                    "summary": summary,
                    "issues": issues,
                    "error": "Failed to generate structured email"
                })

        except Exception as e:
            all_results.append({
                "email": email,
                "domain": domain,
                "mail_sent": False,
                "summary": None,
                "issues": [],
                "error": str(e)
            })

    return {"results": all_results}
