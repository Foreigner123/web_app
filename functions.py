def get_todos(filepath="todos.txt"):
    with open("todos.txt", "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todo(todos_arg, filepath='todos.txt'):
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)

