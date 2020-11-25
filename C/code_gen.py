import os


todo_base_path = os.path.join("tests", "todo")
todos_file_dic = {
    os.path.join(todo_base_path, "todo_add_base.txt"): os.path.join(todo_base_path, "test_todo_add.py"),
    # os.path.join(todo_base_path, "todo_delete_base.txt"): os.path.join(todo_base_path, "test_todo_delete.py"),
    # os.path.join(todo_base_path, "todo_change_base.txt"): os.path.join(todo_base_path, "test_todo_change.py")
}


for base_file, py_file in todos_file_dic.items():
    base_code = open(base_file, "r").read()
    code_file = open(py_file, "a")
    for iteration in range(12):
        code = base_code.replace("X", str(2**iteration))
        code_file.write(code)
