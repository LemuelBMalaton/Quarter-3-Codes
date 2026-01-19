name = input("Enter your name: ")
age = input("Enter your age: ")
favoritesubject = input("Enter your favorite subject: ")
student = {
    "name": name,
    "age": age,
    "subject": favoritesubject
}
print("Student Record: ")
print("Name:", student["name"])
print("Age:", student["age"])
print("Favorite Subject:", student["favoritesubject"])
