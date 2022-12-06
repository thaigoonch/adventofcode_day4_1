import fileinput

elves_assignments = []

def get_assignments(filename):
    for line in fileinput.input(files=filename):
        line = line.strip()
        elfAssignments = line.split(',')
        if (len(elfAssignments) != 2):
            print("Unexpected elfAssignments input: " + str(elfAssignments))
        else:
            for assignment in elfAssignments:
                sections = assignment.split('-')
                if (len(sections) != 2):
                    print("Unexpected sections input: " + str(sections))
                else:
                    sectionsmin = int(sections[0].replace("'", ""))
                    sectionsmax = int(sections[1].replace("'", ""))
                    new_section = ""
                    for i in range(sectionsmin, sectionsmax+1):
                        new_section = new_section + str(i)
                    elves_assignments.append(new_section)

def get_assignments_that_contain_assignments():
    contained_count = 0
    for i, assignment in enumerate(elves_assignments):
        if (i+1) % 2 == 0: # pair off
            previous_assignment = elves_assignments[i-1]
            assignment_small = assignment
            assignment_large = previous_assignment
            if (len(assignment) > len(previous_assignment)):
                assignment_small = previous_assignment
                assignment_large = assignment
            #print("len(assignment_small): " + str(len(assignment_small)) + ", len(assignment_large): " + str(len(assignment_large)))
            if assignment_small in assignment_large:
                contained_count = contained_count + 1
                
    return contained_count

def main():
    get_assignments("input.txt")
    #print("elves_assignments: " + str(elves_assignments))
    print(get_assignments_that_contain_assignments())

if __name__ == "__main__":
    main()