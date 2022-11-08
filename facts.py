from jinja2 import Environment, FileSystemLoader
import requests

# datos
response = requests.get("https://catfact.ninja/facts")
facts_data = response.json()
# vista
environment = Environment(loader=FileSystemLoader("templates/"))
facts_template = environment.get_template("facts.html")
# renderizado
facts_html = facts_template.render(cat_facts=facts_data['data'])
print(facts_html)