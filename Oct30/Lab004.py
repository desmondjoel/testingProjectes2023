# Remove a key-value pair from the dictionary.

emp={"QA":"Pritam","Dev":"Aman","UX":"Ron","UI":"John","Backend":"trudy"}
print(emp)
print(emp.keys())
print(emp.values())
print(emp.get("UI"))

test = emp.pop("Backend")
print(test)
print(emp)