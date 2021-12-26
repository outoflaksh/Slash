from jinja2 import Environment, FileSystemLoader

if __name__ == "__main__":
    requests = [{"url": "/", "method": "GET"}, {"url": "/posts", "method": "GET"}]

    env = Environment(
        loader=FileSystemLoader("./templates"), trim_blocks=True, lstrip_blocks=True
    )
    template = env.get_template("template.html")
    print(template.render(requests))
