import streamlit as st
import random

def load_css():
    with open("styles.css", "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="Number Guessing Game", page_icon="🎮", layout="centered")
    load_css()
    
    st.title("🎯 Number Guessing Game")
    st.markdown("**Welcome to the game! You have 5 attempts to guess the number between 1 and 30. Let's start!**")
    
    # Session state to store variables
    if 'number_guess' not in st.session_state:
        st.session_state.number_guess = random.randint(1, 30)
    
    if 'chances' not in st.session_state:
        st.session_state.chances = 5
    
    if 'guess_counter' not in st.session_state:
        st.session_state.guess_counter = 0
    
    guess = st.number_input("Enter your guess:", min_value=1, max_value=30, step=5)
    
    if st.button("Submit Guess"):
        if st.session_state.guess_counter < st.session_state.chances:
            st.session_state.guess_counter += 1

            if guess == st.session_state.number_guess:
                st.success(f"🎉 Congratulations! You found the number {st.session_state.number_guess} in {st.session_state.guess_counter} attempts!")
                st.session_state.number_guess = random.randint(1, 30)
                st.session_state.guess_counter = 0
            elif guess > st.session_state.number_guess:
                st.warning("📉 Your guess is too high, try again!")
            else:
                st.warning("📈 Your guess is too low, try again!")
        
        if st.session_state.guess_counter >= st.session_state.chances and guess != st.session_state.number_guess:
            st.error(f"❌ Oops! You've used all attempts. The number was {st.session_state.number_guess}. Better luck next time!")
            st.session_state.number_guess = random.randint(1, 30)
            st.session_state.guess_counter = 0
    
    st.markdown(f"**Attempts Left: {st.session_state.chances - st.session_state.guess_counter}**")

if __name__ == "__main__":
    main()
