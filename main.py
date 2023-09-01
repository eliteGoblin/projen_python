import os

import typer
from dotenv import load_dotenv

if not load_dotenv(dotenv_path=".env_example"):
    raise RuntimeError(f"Failed to load .env file, in {os.getcwd()}")

app = typer.Typer()


@app.command()
def main(
    name: str = typer.Option(..., prompt=True, help="The name to greet."),
    age: int = typer.Option(..., help="The age of the person."),
    is_vip: bool = typer.Option(False, "--vip", help="Is the person a VIP?"),
    lang: str = typer.Option(None, "--lang", "-l", help="Language to greet in."),
) -> None:
    """This is a greeting app."""
    greeting = "Hello"
    if lang == "es":
        greeting = "Hola"
    elif lang == "fr":
        greeting = "Bonjour"

    vip_str = " VIP" if is_vip else ""
    typer.echo(f"{greeting}, {name}{vip_str}! You are {age} years old.")

    my_credential = os.getenv("MY_EXAMPLE_CREDENTIAL")
    if my_credential is None:
        typer.echo("MY_EXAMPLE_CREDENTIAL is not set.")
        raise typer.Exit()
    typer.echo(f"my_credential: {my_credential}")


@app.command()
def add(x: float, y: float) -> None:
    """Add two numbers."""
    typer.echo(f"The sum is: {x+y}")


@app.command()
def subtract(x: float, y: float) -> None:
    """Subtract two numbers."""
    typer.echo(f"The result is: {x-y}")


if __name__ == "__main__":
    app()
