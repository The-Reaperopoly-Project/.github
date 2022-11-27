import click
"""
Click module instructions
- command line parameters to ease setup
https://pypi.org/project/click/#:~:text=Click%20is%20a%20Python%20package,defaults%20out%20of%20the%20box.
"""
@click.command()
@click.option('--name')

def main(name):
    fname = click.prompt("Enter your first name")
    click.echo(f"Your name is {fname}")

if __name__ == '__main__':
    main()
