from jinja2 import Template

template = """<h1>Colors Palette</h1>
<ul>
{% for color in colors %}
  <li>{{ color  }}</li>
{% endfor %}
</ul>
"""

data = ["#2A9D8F", "#E9C46A", "#FFFFFF"]

j2_template = Template(template)
html = j2_template.render(colors=data)
print(html)
