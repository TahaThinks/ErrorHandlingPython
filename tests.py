# FileNotFound Handling
try:
    file = open("a_file.txt")
except:
    file = open("a_file.txt", 'w')
    file.write("Hello Taha!")



# # KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_exisitent_key"]
#
# # IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]
#
# # TypeError
# text = "abc"
# print(text + 5)
