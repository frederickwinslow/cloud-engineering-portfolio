from flask import Flask, render_template_string, url_for

app = Flask(__name__)

# Replace these sample values with your own employee information.
EMPLOYEE = {
    "name": "Alex Morgan",
    "department": "Operations",
    "access": "Employee",
}

DOCUMENTS = [
    {"title": "Employee Handbook", "filename": "employee-handbook.txt"},
    {"title": "Health and Safety Guide", "filename": "health-and-safety-guide.txt"},
    {"title": "IT Acceptable Use Policy", "filename": "it-acceptable-use-policy.txt"},
]

PAGE = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Company Document Portal</title>
    <style>
      body { max-width: 760px; margin: 48px auto; padding: 0 20px; font-family: Arial, sans-serif; color: #243247; background: #f4f7fb; }
      header, section { margin-bottom: 20px; padding: 22px; border-radius: 10px; background: white; box-shadow: 0 2px 8px #18304a14; }
      h1 { margin-top: 0; color: #145da0; }
      li { margin: 12px 0; }
      .note { color: #52657a; }
      a { color: #145da0; }
    </style>
  </head>
  <body>
    <header>
      <h1>Company Document Portal</h1>
      <p class="note">A simple internal portal for employees and company documents.</p>
    </header>
    <section>
      <h2>Employee information</h2>
      <p><strong>Name:</strong> {{ employee.name }}</p>
      <p><strong>Department:</strong> {{ employee.department }}</p>
      <p><strong>Access:</strong> {{ employee.access }}</p>
    </section>
    <section>
      <h2>Company documents</h2>
      <ul>
        {% for document in documents %}
        <li><a href="{{ url_for('static', filename='documents/' ~ document.filename) }}" download>{{ document.title }} (download)</a></li>
        {% endfor %}
      </ul>
      <p class="note">These are sample guides for this portfolio project. Replace them with approved company documents before real use.</p>
    </section>
  </body>
</html>"""


@app.route("/")
def home():
    return render_template_string(PAGE, employee=EMPLOYEE, documents=DOCUMENTS)


if __name__ == "__main__":
    app.run()
