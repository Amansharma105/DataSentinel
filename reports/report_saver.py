class ReportSaver:

    def save(self, content, filename):

        with open(filename, "w", encoding="utf-8") as file:

            file.write(content)

        return filename
