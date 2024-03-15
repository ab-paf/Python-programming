# JTMS-14
# problem 6.7.py
# Abel Mengistu
# abmengistu@jacobs-university.de

# add a new key/value pair to a directory using []:
# <a dictionary> [<a key>] = <a value>
info = {}
info["name"] = "Andy", "Sandy"
info["occupation"] = "Janitor"
print(info)
# []used to replace a value at an existing key:
info["occupation"] = "CEO"
print(info)
print(list(info.values()))
print(list(info.keys()))