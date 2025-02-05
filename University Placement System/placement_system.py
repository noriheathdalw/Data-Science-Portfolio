import json

# Define the Student class
class Student:
    def __init__(self, student_id, name, major, gpa):
        self.student_id = student_id
        self.name = name
        self.major = major
        self.gpa = gpa
        self.applied_jobs = []

    def apply_for_job(self, job_id):
        self.applied_jobs.append(job_id)

# Define the Company class
class Company:
    def __init__(self, company_id, name, job_openings):
        self.company_id = company_id
        self.name = name
        self.job_openings = job_openings

    def post_job(self, job_id, job_description):
        self.job_openings[job_id] = job_description

# Define the PlacementSystem class
class PlacementSystem:
    def __init__(self):
        self.students = {}
        self.companies = {}

    def register_student(self, student_id, name, major, gpa):
        student = Student(student_id, name, major, gpa)
        self.students[student_id] = student

    def register_company(self, company_id, name):
        company = Company(company_id, name, {})
        self.companies[company_id] = company

    def post_job(self, company_id, job_id, job_description):
        if company_id in self.companies:
            self.companies[company_id].post_job(job_id, job_description)
        else:
            print("Company not registered.")

    def apply_for_job(self, student_id, job_id):
        if student_id in self.students:
            self.students[student_id].apply_for_job(job_id)
        else:
            print("Student not registered.")

    def save_data(self, filename):
        data = {
            "students": {student_id: student.__dict__ for student_id, student in self.students.items()},
            "companies": {company_id: company.__dict__ for company_id, company in self.companies.items()}
        }
        with open(filename, 'w') as file:
            json.dump(data, file)

    def load_data(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            for student_id, student_data in data['students'].items():
                student = Student(**student_data)
                self.students[student_id] = student
            for company_id, company_data in data['companies'].items():
                company = Company(**company_data)
                self.companies[company_id] = company

# Main function to run the placement system
def main():
    system = PlacementSystem()

    while True:
        print("\n1. Register Student")
        print("\n2. Register Company")
        print("\n3. Post Job")
        print("\n4. Apply for Job")
        print("\n5. Save Data")
        print("\n6. Load Data")
        print("\n7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            major = input("Enter Student Major: ")
            gpa = float(input("Enter Student GPA: "))
            system.register_student(student_id, name, major, gpa)
        elif choice == '2':
            company_id = input("Enter Company ID: ")
            name = input("Enter Company Name: ")
            system.register_company(company_id, name)
        elif choice == '3':
            company_id = input("Enter Company ID: ")
            job_id = input("Enter Job ID: ")
            job_description = input("Enter Job Description: ")
            system.post_job(company_id, job_id, job_description)
        elif choice == '4':
            student_id = input("Enter Student ID: ")
            job_id = input("Enter Job ID: ")
            system.apply_for_job(student_id, job_id)
        elif choice == '5':
            filename = input("Enter filename to save data: ")
            system.save_data(filename)
        elif choice == '6':
            filename = input("Enter filename to load data: ")
            system.load_data(filename)
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 
