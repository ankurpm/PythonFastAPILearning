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

print_marks({"John": 40, "Nick": 50})