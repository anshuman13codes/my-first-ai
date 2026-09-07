import streamlit as st
import datetime
import random
import math

st.set_page_config(page_title="My Colourful AI v1", page_icon="🤖", layout="centered")

st.title("🤖 My Colourful AI v1 - by anshuman13codes")
st.markdown("Talk to my AI from anywhere! Created in Imphal.")

name = st.text_input("What's your name?", placeholder="Enter your name")
if name:
    st.success(f"Hello {name}! Welcome to my AI world! 🌈")

option = st.selectbox("Choose what my AI should do:", 
    ["Select an option", "Check Prime Number", "Find Factorial", "Calculator", "Tell a Joke", "Show Current Time", "Palindrome Check", "BMI Calculator"])

if option == "Check Prime Number":
    num = st.number_input("Enter a number", min_value=1, step=1)
    if st.button("Check Prime"):
        is_prime = True
        if num < 2: is_prime = False
        else:
            for i in range(2, int(math.sqrt(num))+1):
                if num % i == 0: is_prime = False; break
        if is_prime: st.balloons(); st.write(f"✅ {num} IS a Prime Number!")
        else: st.write(f"❌ {num} is NOT a Prime Number.")

elif option == "Find Factorial":
    num = st.number_input("Enter a number", min_value=0, step=1)
    if st.button("Find Factorial"):
        st.write(f"Factorial of {num} is **{math.factorial(num)}**")

elif option == "Calculator":
    a = st.number_input("First number")
    b = st.number_input("Second number")
    op = st.selectbox("Operation", ["+", "-", "*", "/"])
    if st.button("Calculate"):
        if op == "+": st.write(f"Result: {a+b}")
        elif op == "-": st.write(f"Result: {a-b}")
        elif op == "*": st.write(f"Result: {a*b}")
        elif op == "/": st.write(f"Result: {a/b if b!=0 else 'Cannot divide by zero'}")

elif option == "Tell a Joke":
    jokes = ["Why don't scientists trust atoms? Because they make up everything! 😂", "I told my computer I needed a break, it said 'No problem, I'll go to sleep' 😴", "Why did Python developer wear glasses? Because they couldn't C! 👓"]
    if st.button("Tell me a joke"):
        st.write(random.choice(jokes))

elif option == "Show Current Time":
    st.write(f"Current Time: **{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}**")
    st.write(f"Your location: Imphal, Manipur!")

elif option == "Palindrome Check":
    word = st.text_input("Enter word/number")
    if st.button("Check"):
        if word == word[::-1]: st.write(f"✅ {word} is Palindrome!")
        else: st.write(f"❌ {word} is NOT Palindrome!")

elif option == "BMI Calculator":
    h = st.number_input("Height in meters", min_value=0.5, max_value=3.0, value=1.7)
    w = st.number_input("Weight in kg", min_value=10, value=60)
    if st.button("Calculate BMI"):
        bmi = w / (h*h)
        st.write(f"Your BMI is: **{bmi:.2f}**")

st.markdown("---")
st.markdown("Made with ❤️ in Imphal | [My GitHub](https://github.com/anshuman13codes/my-first-ai)")