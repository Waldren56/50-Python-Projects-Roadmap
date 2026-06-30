# 13 — Multiple-Choice Quiz with Scoring

A terminal-based multiple-choice quiz with scoring and a wrong-answer review at the end. Questions are stored as a list of nested dictionaries. After completing the quiz, the user can choose to see which questions they got wrong, along with the correct answers.

## Skills used

- Nested data structures: list of dictionaries containing lists
- `enumerate()` with `start=1` for numbered option display
- Accumulator pattern for score tracking
- Records pattern: wrong answers stored as dictionaries, not parallel lists
- Separation of concerns: display, input handling, and results in separate functions

## How to run

```bash
cd 13-quiz
python main.py
```

No external dependencies required.