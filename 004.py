#================================
# Student Data Organizer Project
# ================================

# Global data structures
students = []        # List to store all student records
all_subjects = set() # Set to store unique subjects


# -------- MENU FUNCTION --------
def show_menu():
    print("""
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
""")


# -------- ADD STUDENT --------
def add_student():
    print("\n--- Add Student ---")

    sid = int(input("Student ID: "))
    dob = input("Date of Birth (YYYY-MM-DD): ")
    name = input("Name: ")
    age = int(input("Age: "))
    grade = input("Grade: ")

    subjects = input("Subjects (comma-separated): ").split(",")
    subjects = [s.strip() for s in subjects]

    student = {
        "id_dob": (sid, dob),   # Tuple (immutable)
        "name": name,
        "age": age,
        "grade": grade,
        "subjects": subjects
    }

    students.append(student)

    for sub in subjects:
        all_subjects.add(sub)

    print("✅ Student added successfully!\n")


# -------- DISPLAY STUDENTS --------
def display_students():
    print("\n--- Display All Students ---")

    if not students:
        print("No student records found.\n")
        return

    for s in students:
        sid, dob = s["id_dob"]   # tuple unpacking
        print(f"ID: {sid} | Name: {s['name']} | Age: {s['age']} | "
              f"Grade: {s['grade']} | Subjects: {', '.join(s['subjects'])}")
    print()


# -------- UPDATE STUDENT --------
def update_student():
    print("\n--- Update Student Information ---")
    sid = int(input("Enter Student ID to update: "))

    for s in students:
        if s["id_dob"][0] == sid:
            s["age"] = int(input("Enter new age: "))

            new_subjects = input("Enter new subjects (comma-separated): ").split(",")
            s["subjects"] = [sub.strip() for sub in new_subjects]

            for sub in s["subjects"]:
                all_subjects.add(sub)

            print("✅ Student updated successfully!\n")
            return

    print("❌ Student not found.\n")


# -------- DELETE STUDENT --------
def delete_student():
    print("\n--- Delete Student ---")
    sid = int(input("Enter Student ID to delete: "))

    for i in range(len(students)):
        if students[i]["id_dob"][0] == sid:
            del students[i]   # del keyword
            print("✅ Student deleted successfully!\n")
            return

    print("❌ Student not found.\n")


# -------- DISPLAY SUBJECTS --------
def display_subjects():
    print("\n--- Subjects Offered ---")

    if not all_subjects:
        print("No subjects found.\n")
        return

    for sub in all_subjects:
        print(sub)
    print()


# -------- MAIN PROGRAM --------
print("🎓 Welcome to Student Data Organizer")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        display_subjects()
    elif choice == "6":
        print("🙏 Thank you for using Student Data Organizer")
        break
    else:
        print("❌ Invalid choice, try again.\n")
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
