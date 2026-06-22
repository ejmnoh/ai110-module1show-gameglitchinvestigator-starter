from logic_utils import check_guess, new_game_state

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

# FIX: Created the tests using agent mode
def test_new_game_resets_status_to_playing():
    # The bug: "New Game" left status as "won"/"lost", so the game-over gate
    # never cleared and the board stayed frozen. A fresh game must be playable.
    state = new_game_state()
    assert state["status"] == "playing"

def test_new_game_resets_all_progress():
    # A new game must wipe every piece of prior progress, not just some.
    state = new_game_state()
    assert state["attempts"] == 0
    assert state["score"] == 0
    assert state["history"] == []

def test_new_game_accepts_injected_secret():
    # secret can be passed in for deterministic tests.
    state = new_game_state(secret=42)
    assert state["secret"] == 42


# FIX: Created the tests using agent mode

# A fresh game must start with attempts == 0 (zero guesses made yet). The bug
# was initializing it to 1, which made the "attempts left" display wrong from
# the start and ended the game one guess early.
def test_new_game_starts_with_zero_attempts():
    state = new_game_state()
    assert state["attempts"] == 0


def test_attempts_left_is_full_limit_before_any_guess():
    # "Attempts left" is computed as attempt_limit - attempts (see app.py).
    # Before the player guesses, all attempts must still be available.
    attempt_limit = 8
    state = new_game_state()
    attempts_left = attempt_limit - state["attempts"]
    assert attempts_left == attempt_limit
