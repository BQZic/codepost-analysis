import codepost
import csv
import random
codepost.configure_api_key("4c94d9d338cefd5e8e08ec3cef7a93f011ebb8bd")
#print(codepost.course.list_available())

def getCourse(name, period):
    # select course according to name and period
    course = codepost.course.list_available()[1]
    return course

def getAssignment(course, name):
    return course.assignments.by_name('Hello World')

if __name__ == "__main__":
    course = codepost.course.list_available()[1]
    roster = codepost.roster.retrieve(id = course.id)
    graders = roster.graders
    assignment = course.assignments.by_name('Hello')

    selected_submissions = []
    for grader in graders:
        submission_link = 'https://codepost.io/code/'
        submissions = assignment.list_submissions(grader = grader)
        num_of_submissions = len(submissions)
        if num_of_submissions > 0:
            rand_id = random.randint(0, num_of_submissions - 1)
            submission_id = submissions[rand_id].id
            submission_link += str(submission_id)
            selected_submissions.append(submission_link)
        else: selected_submissions.append(submission_link)

    with open('File.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['', 'Assignment Viewed', 'All rubric comments correctly applied', 'No application of a rubric comment was missing', 'No custom comment was a rubric comment', 'Notes'])
        num_graders = len(graders)
        for i in range(num_graders):
            writer.writerow([graders[i], selected_submissions[i]])