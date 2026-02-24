
def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title()+" "+last_name.title()
    return full_name

def print_name_age(first_name: str, age: int):
    user = first_name.title()+" "+str(age)
    print(user)

print(get_full_name("john", "doe"))
print_name_age("john", 10)