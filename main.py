from jinja2 import Environment, FileSystemLoader
import sys
import json


def load_specs(specs_file):
    data = None
    with open(specs_file, "r") as specs_file:
        data = json.load(specs_file)
    return data


def render_template(template,specs):
    res = template.render(specs = specs)
    return res


def parse_params():
    pass


if __name__ == "__main__":
    specs = load_specs("specs.json")
    env = Environment(
        loader=FileSystemLoader("./templates"), trim_blocks=True, lstrip_blocks=True
    )
    template = env.get_template("template.j2")
    with open("server.py","w") as out_file:
        res = render_template(template,specs)
        out_file.write(res)
    # print(specs)
