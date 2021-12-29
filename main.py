from jinja2 import Environment, FileSystemLoader
import sys
import json
import template_renderer


def print_help():
    pass
if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1:
        template_renderer.render_template()
    elif len(args) == 2:
        json_file = args[1]
        template_renderer.render_template(json_file)
    elif len(args) == 3:
        template_renderer.render_template(args[1],args[2])
    else:
        raise Exception("invalid arguments")
