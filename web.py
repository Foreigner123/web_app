import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo_item = st.session_state["todo"] + "\n"
    todos.append(todo_item)
    functions.write_todo(todos)


st.title("Todo App")
st.subheader("This is a todo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todo(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Enter a todo",
              on_change=add_todo, key='todo')