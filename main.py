import fileinput

'''
input sample 1:

7-37,6-36
5-5,5-67
59-84,3-90
26-26,25-99
44-97,96-97
41-77,42-57
33-79,34-80
68-70,68-68
68-81,67-80
4-93,4-5

test results 1:

7-37,6-36 # no
5-5,5-67 # yes
59-84,3-90 # yes
26-26,25-99 # yes
44-97,96-97 # yes
41-77,42-57 # yes
33-79,34-80 # no
68-70,68-68 # yes
68-81,67-80 # no
4-93,4-5 # yes
total=7

input sample 2:
11-33,11-42
66-66,67-67
35-53,34-52
23-23,23-68
9-20,10-15
16-74,15-83
20-82,58-81
19-84,82-84
50-77,50-77
5-7,7-71
18-93,52-92

test results 2:

11-33,11-42 # yes
66-66,67-67 # no
35-53,34-52 # no
23-23,23-68 # yes
9-20,10-15 # yes
16-74,15-83 # yes
20-82,58-81 # yes
19-84,82-84 # yes
50-77,50-77 # yes
5-7,7-71 # no
18-93,52-92 # yes
total=8

input sample 3:

4-85,3-3
8-76,2-76
62-73,45-73
29-31,29-53
76-78,25-77
11-98,11-11
17-93,18-94
4-12,5-12

test results 3:

4-85,3-3 # no
8-76,2-76 # yes
62-73,45-73 # yes
29-31,29-53 # yes
76-78,25-77 # no
11-98,11-11 # yes
17-93,18-94 # no
4-12,5-12 # yes
total=5

'''

def get_assignments(filename):
    elves_assignments = []
    for line in fileinput.input(files=filename):
        line = line.strip()
        elfAssignments = line.split(',')
        if (len(elfAssignments) != 2):
            print("Unexpected elfAssignments input: " + str(elfAssignments))
            sys.exit()

        for assignment in elfAssignments:
            sections = assignment.split('-')
            if (len(sections) != 2):
                print("Unexpected sections input: " + str(sections))
                sys.exit()
                
            sectionsmin = int(sections[0].replace("'", ""))
            sectionsmax = int(sections[1].replace("'", ""))
            new_section = ""
            for i in range(sectionsmin, sectionsmax+1):
                new_section = new_section + " " + str(i) + ","
            elves_assignments.append(new_section)
            
    return elves_assignments

def get_assignments_that_contain_assignments(elves_assignments):
    contained_count = 0
    for i, assignment in enumerate(elves_assignments):
        if (i+1) % 2 == 0: # pair off
            previous_assignment = elves_assignments[i-1]
            if previous_assignment in assignment or assignment in previous_assignment:
                contained_count = contained_count + 1
                
    return contained_count

def main():
    elves_assignments = get_assignments("input.txt")
    print(get_assignments_that_contain_assignments(elves_assignments))

if __name__ == "__main__":
    main()