from jinja2 import Template

TEMPLATE_FILE = "template.html"
DATA_FILE = "colors.txt"
HTML_FILE = "colors.html"

with open(TEMPLATE_FILE, "r") as f_template:
	template = f_template.read()

with open(DATA_FILE, "r") as f_data:
	data = [line.rstrip('\n') for line in f_data]


j2_template = Template(template)
html = j2_template.render(colors=data)


with open(HTML_FILE, "w") as f_html:
	f_html.write(html)

