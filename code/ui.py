import streamlit as st

# Custom CSS to change the UI look
st.markdown("""
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
""", unsafe_allow_html=True)

def app():
    st.title("DoCode")
    st.subheader("Helps with code documentation!")

    # Create 3 text input boxes on the first row
    col1, col2, col3 = st.columns(3)
    with col1:
        input1 = st.selectbox('Model', ('GPT-4', 'GPT-3.5'))
    with col2:
        input2 = st.text_input('Text Input')
    with col3:
        input3 = st.text_input('Open API Key')

    # Create a larger text input box on the second row
    large_input = st.text_area('Query Text')

    # Create a submit button
    if st.button('Submit'):
        # Now the outputs are written in the output text area
        output_value = f'Input 1: {input1}\nInput 2: {input2}\nInput 3: {input3}\nLarge Input: {large_input}'
        st.text_area('Output Display', value=output_value)

    # Create a new row with feedback buttons
    col4, col5 = st.columns(2)
    with col4:
        if st.button('Correct'):
            st.write('You indicated the answer was correct.')
    with col5:
        if st.button('Wrong'):
            st.write('You indicated the answer was wrong.')

if __name__ == '__main__':
    app()
