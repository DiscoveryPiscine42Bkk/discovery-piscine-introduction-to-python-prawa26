def greetings(name="nodle stranger"):
    if isinstance(name, str):
        print(f"Hello, {name}.")
    else:
        print("Error! It was not a name.")

greetings('Trent')
greetings('Alexander')
greetings()
greetings(23)