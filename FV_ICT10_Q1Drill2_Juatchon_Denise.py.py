from pyscript import document, display

from js import document

def generate_message():

    name = document.getElementById("name").value
    age = document.getElementById("age").value
    school = document.getElementById("school").value

    message = f"""
    📘 Student Profile:
    -------------------------
    Name:\t\t\"{name}\"
    Age:\t\t{age}
    School:\t\"{school}\"
    -------------------------
    Welcome, {name}! Keep learning at {school}!
    """

    document.getElementById("output").innerText = message