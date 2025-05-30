import streamlit as st
import random

st.set_page_config(page_title="Yoda Translator", page_icon="🛸")

# --- Title
st.title("🛸 Yoda Translator")
st.write("Type a sentence, you must. Translate to Yoda-speak, we will.")

# --- Input box
user_input = st.text_input("Your sentence:", placeholder="Enter a sentence...")

# --- Yoda translator logic
def yoda_translate(sentence):
    words = sentence.strip('.!?').split()
    if len(words) < 4:
        return sentence + " Hmmm."

    split_point = len(words) // 2
    part1 = words[split_point:]
    part2 = words[:split_point]

    templates = [
        f"{' '.join(part1)}, {' '.join(part2)}.",
        f"{' '.join(part1)}... {' '.join(part2)}, yes.",
        f"{' '.join(part2)}, {' '.join(part1)}. Hmmm.",
        f"Hmm. {' '.join(part1)} — {' '.join(part2)}, strong with the Force you are.",
    ]

    return random.choice(templates)

# --- Display output
if user_input:
    yoda_output = yoda_translate(user_input)
    st.markdown(f"**Yoda says:**\n\n> _{yoda_output}_")

# --- Footer
st.caption("Made with 🧠 and ☕ by you.")
