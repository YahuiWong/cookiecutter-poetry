from typing import List

import click
from click import Context

from poetrymytemplete.settings import Settings


def version():
    # wait poetry fix up: https://github.com/python-poetry/poetry/issues/1338
    # with open("pyproject.toml") as f:
    #     ret = re.findall(r'version = "(\d+\.\d+\.\d+)"', f.read())
    #     return ret[0]
    return "0.0.1"


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(version(), "-V", "--version")
@click.option("--alias", help="alias from config.", required=True)
@click.option(
    "-c", "--config", default="./app.yaml", show_default=True, help="Config file.",
)
@click.pass_context
def cli(ctx: Context, alias: str, config: str):
    """
    CLI TITLE.
    """
    ctx.ensure_object(dict)
    ctx.obj["alias"] = alias
    Settings.init(config)

@cli.command(help="Check whether equal count of target database records and ClickHouse.")
@click.option("--schema", help="Schema to check.", required=True)
@click.pass_context
def check(ctx: Context, schema: str):
    alias = ctx.obj["alias"]



if __name__ == "__main__":
    cli()