import streamlit as st
from streamlit_ace import st_ace
import io
import contextlib

# Set up the app title
st.title("Python Code Editor with Syntax Highlighting")

# Ace editor for writing Python code
code = st_ace(
    value="""
# Write your Python code here
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))
""",
    language="python",   # Syntax highlighting for Python
    theme="monokai",     # Choose an Ace editor theme
    height=300           # Height of the editor
)

# Button to execute the code
if st.button("Run Code"):
    if code:
        # Capture the output of the executed code
        output = io.StringIO()
        try:
            with contextlib.redirect_stdout(output):  # Redirect standard output to StringIO
                exec_globals = {}
                exec(code, exec_globals)
            st.success("Code executed successfully!")
        except Exception as e:
            output.write(f"Error while running the code: {e}")
        # Display the output in the app
        st.text_area("Output", value=output.getvalue(), height=200)
    else:
        st.warning("Please write some code before running.")
