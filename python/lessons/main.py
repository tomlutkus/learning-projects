from collections.abc import Callable

# add_one: Callable[[int], int] = lambda x: x + 1
# print(add_one(2))

get_age: Callable[[str], int | str] = lambda name: {
    "lane": 29,
    "hunter": 69,
    "allan": 17,
}.get(name, "not found")

print(get_age("lane"))
