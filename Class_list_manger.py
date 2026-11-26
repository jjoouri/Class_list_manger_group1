# Class List Manager - Group 1
# MIS 211 Bonus Assignment (GitHub Teamwork)

names = ["Sara", "Noura", "Lama", "Reem", "Amal", "Lama"]

# ===== Each student adds her function BELOW this line =====
# Written by: [jouri] (task 1)
def count_names(names):
    count = 0                       # variable: how many names we counted so far
    for name in names:              # loop: go through every name in the list
        count = count + 1
    return count
# Written by: Hala (task 3)
def sort_names(names):
    return sorted(names)

# Written by: Fatimah (task 4)
def names_starting_with(names, letter):
    result = []
    for name in names:
        if name.startswith(letter):
            result.append(name)
    return result
# ===== Each student adds her function ABOVE this line =====

def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    # Each student calls her function here, for example:
    # print("Number of names:", count_names(names))
    print("Sorted names:", sort_names(names))     
    print("Names starting with L:", names_starting_with(names, "L"))
main()
