# FileNotFound Handling
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", 'w')
    file.write("Hello Taha!")
except KeyError as error_message:
    print(f"The Key {error_message} doesn't Exist")
else:
    content = file.read()
    print(content)
finally:
    raise KeyError("This is an error created by Taha")

