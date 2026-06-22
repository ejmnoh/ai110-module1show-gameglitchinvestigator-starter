import random

# FIX: Created the new function using agent mode
def new_game_state(low: int = 1, high: int = 100, secret=None):
    """Return a fresh game state for starting a new game.

    Defines every field a new game must reset, in one place. The original bug
    was that "New Game" reset some fields but left ``status`` as "won"/"lost",
    so the game-over gate never cleared and the board stayed frozen. Building
    the full state here means no field can be forgotten.

    No Streamlit here on purpose: this is pure logic (values in, values out),
    so it can be unit-tested without launching the app. ``app.py`` copies the
    returned dict into ``st.session_state``.

    ``secret`` can be passed in for deterministic tests; otherwise it's drawn
    randomly from the [low, high] range.
    """
    if secret is None:
        secret = random.randint(low, high)
    return {
        "secret": secret,
        "attempts": 0,
        "score": 0,
        "status": "playing",
        "history": [],
    }


def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
