import pandas as pd
import re

def read_email_list(file_path):
    try:
        df = pd.read_csv(file_path)
        if 'email' not in df.columns:
            raise ValueError("CSV must contain a column named 'email'")

        processed = []

        for email in df['email']:
            match = re.match(r'([^@]+)@(.+)', email)
            if not match:
                continue

            username, domain = match.groups()
            name_parts = re.split(r'\W+', username)
            first_name = name_parts[0].capitalize() if name_parts else ""
            last_name = name_parts[1].capitalize() if len(name_parts) > 1 else ""

            processed.append({
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
                "domain": domain
            })

        return processed
    except Exception as e:
        print(f"❌ Error reading email list: {e}")
        return []
