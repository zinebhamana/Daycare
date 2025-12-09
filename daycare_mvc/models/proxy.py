# models/child.py
class Child:
    def __init__(self, name, age, group):
        self.name = name
        self.age = age
        self.group = group

    def get_info(self):
        return f"Child: {self.name}, Age: {self.age}, Group: {self.group}"

# proxy.py
class ChildProxy:
    def __init__(self, child, allowed_roles):
        self._child = child
        self.allowed_roles = allowed_roles

    def get_info(self, user_role):
        if user_role in self.allowed_roles:
            return self._child.get_info()
        else:
            return "Access Denied"

# usage
child1 = Child("Ahmed", 5, "Préparatoire")
proxy = ChildProxy(child1, allowed_roles=["Admin", "Teacher"])

print(proxy.get_info("Teacher"))  # Accès autorisé
print(proxy.get_info("Parent"))   # Accès refusé
