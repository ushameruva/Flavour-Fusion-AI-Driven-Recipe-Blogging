import streamlit as st
import google.generativeai as genai
import random

# ===============================
# Gemini API Configuration
# ===============================
genai.configure(api_key="AIzaSyB7aDiR4xQmIY-URfslyAxZuNV2w6d6enI")

generation_config = {
    "temperature": 0.75,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    #"response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="models/gemini-2.5-flash",
    generation_config=generation_config
)

# ===============================
# Joke Generator
# ===============================
def get_joke():
    jokes = [
        "Why don't programmers like nature? It has too many bugs.",
        "Why do Java developers wear glasses? Because they don't see sharp.",
        "Why was the JavaScript developer sad? Because he didn't know how to 'null' his feelings.",
        "Why do programmers prefer dark mode? Because light attracts bugs.",
        "Why did the programmer quit his job? Because he didn't get arrays.",
        "Why did the computer get cold? It left its Windows open.",
        "Why was the developer broke? Because he used up all his cache.",
        "Why did the programmer bring a ladder? To reach the high-level language."
    ]
    return random.choice(jokes)

# ===============================
# Recipe Generation Function
# ===============================
def recipe_generation(user_input, word_count):
    try:
        st.info("⏳ Generating your recipe...")
        st.write(
            "😂 While I work on creating your blog, here's a little joke to keep you entertained:\n\n"
            f"**{get_joke()}**"
        )

        prompt = (
            f"Write a detailed recipe blog on the topic '{user_input}' "
            f"with approximately {word_count} words. "
            "Include an introduction, ingredients, step-by-step instructions, tips, and serving suggestions."
        )

        chat_session = model.start_chat(history=[])
        response = chat_session.send_message(prompt)

        st.success("✅ Your recipe is ready!")
        return response.text

    except Exception as e:
        st.error(f"❌ Error generating recipe: {e}")
        return None

# ===============================
# Streamlit UI
# ===============================
st.set_page_config(page_title="Flavour Fusion", page_icon="🍽️", layout="centered")

st.title("🍽️ Flavour Fusion: AI-Driven Recipe Blogging")
st.write("👩‍🍳 Hello! I'm **Flavour Fusion**, your friendly AI chef. Let’s cook up something amazing!")

topic = st.text_input("🍜 Enter Recipe Topic", placeholder="e.g., Vegan Chocolate Cake")
word_count = st.number_input("📝 Number of Words", min_value=300, max_value=2000, step=100)

if st.button("✨ Generate Recipe"):
    if topic.strip() == "":
        st.warning("⚠️ Please enter a recipe topic.")
    else:
        result = recipe_generation(topic, int(word_count))
        if result:
            st.markdown("---")
            st.markdown(result)
