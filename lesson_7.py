pythonist_skills = [
    {"Gohar" : "Python Basics"},
    {"Lilit" : "OOP"},
    {"Janna" : "Git"},
    {"Luiza" : "C++"},
    {"Lilit" : "Business Analyst"},
    {"Janna" : "Numpy"},
    {"Luiza" : "Animation"},
    {"Gohar" : "Business Consultant"}
]

unique_keys_dict = dict()
for dict in pythonist_skills:
    for list in dict:
        if list in unique_keys_dict:
            unique_keys_dict[list] += ", " + (dict[list])
        else:
            unique_keys_dict[list] = dict[list]
print(unique_keys_dict)

