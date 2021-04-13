from types import SimpleNamespace


data = {"name": "John Smith", "hometown": {"name": "New York", "id": 123}}
sn = SimpleNamespace(**data)

print(getattr(sn, "name"))
print(getattr(sn, "job", "no job attribute"))

key = "hometown"
a = SimpleNamespace(**data[key]) if key in data else None
print(a)
print(getattr(a, "zip", None))