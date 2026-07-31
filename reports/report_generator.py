from jinja2 import Environment, FileSystemLoader


class ReportGenerator:

    def generate(self, data):

        env = Environment(
            loader=FileSystemLoader("templates")
        )

        template = env.get_template("report.html")

        return template.render(data=data)
