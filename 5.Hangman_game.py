import random
import requests
from pyfiglet import Figlet
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich import print

console = Console()

stages = [
    """
       ------
       |    |
       |
       |
       |
       |
    ----------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    ----------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    ----------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    ----------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    ----------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    ----------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    ----------
    """
]

def get_ai_word():

    try:

        url = "https://random-word-api.herokuapp.com/word"

        response = requests.get(url)

        word = response.json()[0]

        return word.lower()

    except:

        backup_words = [
            "python",
            "developer",
            "artificial",
            "science",
            "computer"
        ]

        return random.choice(backup_words)

figlet = Figlet(font="slant")

title = figlet.renderText("Hangman AI")

print(f"[cyan]{title}[/cyan]")

console.print(
    Panel.fit(
        "[bold green]Welcome to AI Powered Hangman Game[/bold green]"
    )
)

chosen_word = get_ai_word()

display = ["_"] * len(chosen_word)

guessed_letters = []

wrong_guesses = 0

max_wrong = 6

score = 0

while wrong_guesses < max_wrong and "_" in display:

    console.print(
        Panel(
            stages[wrong_guesses],
            title="[red]Hangman[/red]"
        )
    )

    print(f"[yellow]Word:[/yellow] {' '.join(display)}")

    print(f"[magenta]Guessed Letters:[/magenta] {guessed_letters}")

    print(f"[green]Score:[/green] {score}")

    guess = Prompt.ask(
        "\n[bold cyan]Guess a letter[/bold cyan]"
    ).lower()

    if len(guess) != 1 or not guess.isalpha():

        print("[red]Invalid input. Enter only one letter.[/red]\n")

        continue

    if guess in guessed_letters:

        print("[yellow]Letter already guessed.[/yellow]\n")

        continue

    guessed_letters.append(guess)

    if guess in chosen_word:

        for i in range(len(chosen_word)):

            if chosen_word[i] == guess:

                display[i] = guess

        score += 5

        print("[green]Correct guess.[/green]\n")

    else:

        wrong_guesses += 1

        print("[red]Wrong guess.[/red]\n")

console.print(
    Panel(
        stages[wrong_guesses],
        title="[red]Final Stage[/red]"
    )
)

if "_" not in display:

    console.print(
        Panel.fit(
            f"[bold green]You Won[/bold green]\n\n"
            f"Word: [yellow]{chosen_word}[/yellow]\n"
            f"Final Score: [cyan]{score}[/cyan]"
        )
    )

else:

    console.print(
        Panel.fit(
            f"[bold red]You Lost[/bold red]\n\n"
            f"Correct Word: [yellow]{chosen_word}[/yellow]"
        )
    )