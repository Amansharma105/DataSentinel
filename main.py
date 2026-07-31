import typer

app = typer.Typer()


@app.command()
def start():
    print("DataSentinel Started Successfully")


if __name__ == "__main__":
    app()
