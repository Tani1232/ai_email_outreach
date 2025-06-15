# 📬 AI Email Outreach System

This is a full-stack, AI-powered system that automates the creation and delivery of hyper-personalized outreach emails. It uses web scraping, natural language processing, and an LLM (Together.ai's LLaMA Turbo) to audit company websites and generate custom HTML emails — all deployed using Docker.

---

## 🚀 Features

- ✅ Upload email list via CSV
- ✅ Extract names and domains from emails
- ✅ Scrape and audit company websites
- ✅ Generate personalized messages using LLaMA Turbo
- ✅ Render branded, professional HTML emails (Jinja2 + templates)
- ✅ Send emails via SendGrid API
- ✅ Fully containerized (frontend + backend) using Docker

---

## 🛠️ Tech Stack

| Layer       | Tech Used                            |
|-------------|---------------------------------------|
| Backend     | Python, FastAPI, BeautifulSoup        |
| AI/LLM      | Together.ai (LLaMA Turbo API)         |
| Frontend    | React + Nginx                         |
| Email       | SendGrid API + Jinja2 HTML Templates  |
| Deployment  | Docker + Docker Compose               |
