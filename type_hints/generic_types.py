"""
Generic Types: List, tuples, sets, dict, union, possibly none
"""
"""
Define List type and its type params
"""
def get_names(names: list[str]):
    for name in names:
        print(name.title())
    return names
#print(get_names(["john", "doe"]))

'''
Define tuple and set types
'''
def names1(names: tuple[int, int, str], marks: set[str]):
    for name in names:
        print(name)

#names1((1, 2, "john"), {'a', 'b', 'c'})

'''
Define dictionary type and its type parameters
'''
def print_marks(scores: dict[str, float]):
    for name, score in scores.items():
        print(name+" scored "+str(score))

#print_marks({"John": 40, "Nick": 50})

'''
Union type
It means the type either be this or that
'''
def demo_union(entry: str|int):
    print(entry)
#demo_union("John")
#demo_union(10)

'''
Possibly none
It means the type can possibly be none
If you dont give any va;ue to only str type, it will cause an exception
'''
def demo_none( entry: str | None = None):
    print(entry)

demo_none("John")
demo_none()