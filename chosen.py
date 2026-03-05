students ={}
def register_student():
    student_id =input("Enter Students ID:")
    if student_id in students:
        print("already existing")
    register_student
    name = input("Enter Student Name:")
    age = input("Enter Age:")
    course = input("Enter Course:")
    students[student_id] ={
        "name":name,
        "age":age,
        "course" :course,
    }
    print("registered successfully")

def view_student():
    student_id =input("Enter Students ID:")
    if not students:
        print("students not existing")
        return
    for student_id, details in students.items():
            print("\nStudent ID: ",student_id)
            print("name:",details["name"])
            print("Age:",details["age"])
            print("Course:",details["course"])

def search_student():
    student_id = input("Enter Students ID to search: ")
    if student_id in students:
        student = students[student_id]
        print("Name:",student["name"])
        print("Age:",student["age"])
        print("Course:",student["course"])
    else:
        print("Student not found.")

    student_id = input("Enter Students ID to update: ")
    if student_id in students:
        name = input("Enter new name: ")
        age = input("Enter new age: ")
        course = input("Enter new course: ")
        students[student_id] = {
            "name": name,
            "age": age, 
            "course": course   
        }
        
        print("Students information updated")
    else:
        print("Student not found") 

def update_student():
    student_id = input("Enter Students ID to update: ")
    if student_id in students:
        name = input("Enter new name: ")
        age = input("Enter new age: ")
        course = input("Enter new course: ")
        students[student_id] = {
            "name": name,
            "age": age, 
            "course": course   
        }
        
        print("Students information updated")
    else:
        print("Student not found")  

def delete_student():
    student_id = input("Enter Students ID to delete: ")
    if student_id in students:
        del students[student_id]
        print("Student deleted successfully.")
    else:
        print("Student not found.")


def menu():
    while True:
        print("\n--- Student Registration System ---") 
        print("1. Register Student")
        print("2. View Student")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_student()
        elif choice == "2":
            view_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")
menu()            


