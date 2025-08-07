import streamlit as st
import functions

# Load existing todos
todos = functions.get_todos()

# Function to add a new todo
def add_todo():
    todo = st.session_state["new_todo"].strip()
    if todo:  # Prevent blank todos
        todos.append(todo + "\n")
        functions.write_todos(todos)
    st.session_state["new_todo"] = ""  # Clear input after adding

# UI
st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity.")

# Display todos with checkboxes
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

# Input field to add a new todo
st.text_input(
    label="",
    placeholder="Add a new todo...",
    on_change=add_todo,
    key="new_todo"
)
