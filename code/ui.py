import streamlit as st
from helper import validate_dbml
from streamlit_ace import st_ace
from io import StringIO

# Custom CSS to change the UI look
st.markdown(
    """
    <style>
        .reportview-container {
            flex-direction: column;
            background-color: #e6f0f3;
            color: #333;
        }
        input {
            margin-bottom: 10px;
        }
        .stButton>button {
            color: white;
            background-color: #0083B0;
            border-radius: 5px;
            padding: 10px;
            width: 100%;
            transition: all 0.3s ease-in-out;
        }
        .stButton>button:hover {
            background-color: #005266;
        }
    </style>
""",
    unsafe_allow_html=True,
)


def app():
    st.title("DoCode")
    st.subheader("Helps with code documentation!")

    # Create 3 text input boxes on the first row
    col1, col2, col3 = st.columns(3)
    with col1:
        input1 = st.selectbox("Model", ("GPT-4", "GPT-3.5"))
    with col2:
        input2 = st.text_input("Text Input")
    with col3:
        input3 = st.text_input("Open API Key")

    st.subheader("Upload a file or Paste below:")

    uploaded_file = st.file_uploader("Choose a file")

    # Create a larger text input box on the second row
    code = st_ace(
        height=400,
        language="plain_text",
        theme="github",
        keybinding="vscode",
        font_size=14,
        tab_size=4,
        show_gutter=True,
        show_print_margin=True,
        key="ace-editor",
    )

    # Create a submit button
    if st.button("Submit"):
        if uploaded_file is not None and code != "":
            if uploaded_file != None:
                stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
                string_data = stringio.read()
            else:
                string_data = code
            if validate_dbml(string_data):
                # Now the outputs are written in the output text area
                output_value = f"Input 1: {input1}\nInput 2: {input2}\nInput 3: {input3}\nLarge Input: {string_data}"
                st.text_area("Output Display", value=output_value)
            else:
                st.error("Check the syntax of the DBML")
        else:
            st.error("Upload a file or Paste code.")

    # Create a new row with feedback buttons
    col4, col5 = st.columns(2)
    with col4:
        if st.button("Correct"):
            st.write("You indicated the answer was correct.")
    with col5:
        if st.button("Wrong"):
            st.write("You indicated the answer was wrong.")


if __name__ == "__main__":
    app()
