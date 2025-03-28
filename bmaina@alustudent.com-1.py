# Step 1: Import necessary libraries
import sys

# Step 2: Define the Assignment class
class Assignment:
    def __init__(self, name, category, weight, grade):
        self.name = name
        self.category = category
        self.weight = weight
        self.grade = grade

# Step 3: Function to calculate weighted grade
def calculate_weighted_grade(assignment):
    return (assignment.grade * assignment.weight) / 100

# Step 4: Function to calculate GPA out of 5
def calculate_gpa(weighted_grades, total_weights):
    return (weighted_grades / total_weights) * 5

# Step 5: Function to collect assignment details from the user
def collect_assignment_details():
    name = raw_input("Enter the assignment name: ")
    category = raw_input("Enter the category (Formative/Summative): ").capitalize()
    weight = float(raw_input("Enter the weight of the assignment (as a percentage): "))
    grade = float(raw_input("Enter the grade obtained (out of 100): "))

    # Validate input
    if weight > 100 or weight < 0:
        print("Error: Weight must be between 0 and 100.")
        sys.exit()
    if grade > 100 or grade < 0:
        print("Error: Grade must be between 0 and 100.")
        sys.exit()

    return Assignment(name, category, weight, grade)

# Step 6: Main function to process assignments
def main():
    total_weighted_grade = 0
    total_weight = 0
    formative_total = 0
    summative_total = 0
    total_assignments = int(raw_input("Enter the number of assignments: "))

    for i in range(total_assignments):
        print("\nEnter details for Assignment {}:".format(i + 1))
        assignment = collect_assignment_details()

        weighted_grade = calculate_weighted_grade(assignment)
        total_weighted_grade += weighted_grade
        total_weight += assignment.weight

        if assignment.category == "Formative":
            formative_total += weighted_grade
        elif assignment.category == "Summative":
            summative_total += weighted_grade

    # Calculate and display final results
    if total_weight > 0:
        gpa = calculate_gpa(total_weighted_grade, total_weight)
        print("\nTotal Weighted Grade: {:.2f}".format(total_weighted_grade))
        print("GPA (out of 5): {:.2f}".format(gpa))
        print("Formative Total: {:.2f}".format(formative_total))
        print("Summative Total: {:.2f}".format(summative_total))

        # Pass/Fail determination
        if formative_total >= (total_weighted_grade / 2) and summative_total >= (total_weighted_grade / 2):
            print("Status: PASS")
        else:
            print("Status: FAIL")

# Step 7: Run the main function
if __name__ == "__main__":
    main()


