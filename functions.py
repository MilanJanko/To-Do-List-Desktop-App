file_path = "todos.txt"


def get_todos(filepath=file_path):
    """ Read text file and return to-do item list"""
    with open(filepath, 'r') as file_read:
        todos = file_read.readlines()
    return todos


def write_todos(new_todos, filepath=file_path):
    """Write to-do items and save them in text file"""
    with open(filepath, 'w') as file:
        file.writelines(new_todos)
