import random
import re

def yoda_translate(sentence):
    sentence = sentence.strip().strip('.!?')
    words = sentence.split()

    if len(words) < 4:
        return sentence + ", hmm."

    # Lowercase first word if needed (to prevent awkward capitalization mid-sentence)
    if words[0][0].islower():
        words[0] = words[0].capitalize()

    # Try a smarter split based on sentence length
    n = len(words)
    if n >= 8:
        split1 = n // 3
        split2 = 2 * n // 3
        parts = [words[:split1], words[split1:split2], words[split2:]]
    else:
        split = n // 2
        parts = [words[:split], words[split:]]

    # Reformat with Yoda-style phrasing
    yoda_phrases = [
        f"{' '.join(parts[-1])}, {' '.join(parts[0])} {' '.join(parts[1])}, hmm.",
        f"{' '.join(parts[-1])} — {' '.join(parts[0])}, {' '.join(parts[1])}. Strong in the Force, you are.",
        f"{' '.join(parts[1])}, {' '.join(parts[0])} {' '.join(parts[-1])}. Mmm.",
        f"To you, {' '.join(parts[0])} {' '.join(parts[1])}, {' '.join(parts[-1])}. Yes.",
    ]

    result = random.choice(yoda_phrases)

    # Ensure result is capitalized correctly
    result = result[0].upper() + result[1:]

    return result
