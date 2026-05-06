def load_template(path):
    with open(path, "r") as file:
        return file.read()


def personalize(template, contact):
    return template.format(
        name=contact["name"],
        company=contact["company"]
    )