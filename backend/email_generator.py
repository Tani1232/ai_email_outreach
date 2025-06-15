from jinja2 import Environment, FileSystemLoader

def generate_email(data):
    env = Environment(loader=FileSystemLoader("."))
    template_str = """
    <html>
      <body>
        <p>Hi {{ name }},</p>
        <p>I came across your website and found it really interesting. Here's a quick summary:</p>
        <p>{{ summary }}</p>
        <p>However, I noticed a few areas for improvement:</p>
        <ul>
        {% for issue in issues %}
          <li>{{ issue }}</li>
        {% endfor %}
        </ul>
        <p>Would you like help improving these? Let's connect!</p>
        <p>Best,<br>Tanishq</p>
      </body>
    </html>
    """
    template = env.from_string(template_str)
    return template.render(name=data['name'], summary=data['summary'], issues=data['issues'])
