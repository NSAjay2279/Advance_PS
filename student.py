class Student:
    def __init__(self, name, house):
        ...


def main():
    student = get_student()
    print(student)



def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)



if __name__ == "__main__":
    main()
