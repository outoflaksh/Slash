from jinja2 import Environment, FileSystemLoader
import json


def load_specs(specs_file):
    data = None
    with open(specs_file, "r") as specs_file:
        data = json.load(specs_file)
    return data

def render_template(json_file=None,out_file=None):
    if json_file == None:
        json_file = "specs.json" 
    if out_file == None:
        out_file = "server.py"
    specs = load_specs(json_file)
    env = Environment(
        loader=FileSystemLoader("./templates"), trim_blocks=True, lstrip_blocks=True
    )
    template = env.get_template("template.j2")
    with open(out_file, "w") as res_file:
        res = template.render(specs = specs)
        res_file.write(res)
