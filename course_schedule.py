import json
import collections

def if_possible(prereq_dict):
    visited_set = set()

    def dfs(course):
        if course in visited_set:
            return False
        
        visited_set.add(course)
        for c in prereq_dict[course]:
            if not dfs(c):
                return False

        visited_set.remove(course)
        return True

    for crs in prereq_dict:
        if not dfs(crs):
            return False

    return True

def getCourseOrder(prereq_dict):
    output_list = []
    visited_set = set()
    cycle_set = set()

    def dfs(course):
        if course in cycle_set:
            return False

        if course in visited_set:
            return True
        
        cycle_set.add(course)
        for c in prereq_dict[course]:
            if not dfs(c):
                return False

        cycle_set.remove(course)
        visited_set.add(course)
        output_list.append(course)

        return True

    for k in prereq_dict:
        if not dfs(k):
            return []

    return output_list

def createCourseSchedule(course_ordering,classes_per_term,prereq_dict,system_type="Q"):
    # TODO:
    current_schedule = [(set(),0)]
    current_classes_taken = set() #[]

    def canTakeCourse(proc_course):
        if len(prereq_dict[proc_course]) == 0:
            return True

        res = all(True if prereq in current_classes_taken else False for prereq in prereq_dict[proc_course])
        return res

    current_term = set()

    while course_ordering:
        n = len(course_ordering)
        noClassesAdded = True
        for i in range(n):
            course = course_ordering[i]
            if canTakeCourse(course):
                current_term.add(course)
                noClassesAdded = False
                course_ordering[i] = "N/A"
                if len(current_term) == classes_per_term:
                    current_term = list(current_term)
                    current_term.sort()
                    current_schedule.append((current_term,current_schedule[-1][1] + 1))
                    current_classes_taken.update(current_term)
                    current_term = set()

        if not noClassesAdded:
            course_ordering = [c for c in course_ordering if c != "N/A"]
            if len(course_ordering) == 0:
                current_term = list(current_term)
                current_term.sort()
                for i in range(classes_per_term - len(current_term)):
                    current_term.append("Free Class " + str(i+1))

                current_schedule.append((current_term,current_schedule[-1][1] + 1))
                current_classes_taken.update(current_term)
                current_term = set()
        else:
            current_term = list(current_term)
            current_term.sort()
            for i in range(classes_per_term - len(current_term)):
                current_term.append("Free Class " + str(i+1))
                
            current_schedule.append((current_term,current_schedule[-1][1] + 1))
            current_classes_taken.update(current_term)
            current_term = set()

    current_schedule.pop(0)
    return current_schedule

if __name__ == "__main__":
    prereq_dict = {}

    with open('input.json','r') as f:
        f_data = json.load(f)
        #print(json.dumps(f_data["Courses to take"], indent=4))

        for course in f_data["Courses to take"]:
            course_name = course["Course Name"]
            prerequisites = course["Prerequisites"]
            prereq_dict[course_name] = prerequisites

        if not if_possible(prereq_dict):
            print("Schedule not possible")
        else:
            print("Schedule possible")
            course_ordering = getCourseOrder(prereq_dict)
            #print(course_ordering,end="\n\n")

            numOfClassesPerTerm = input("Enter number of classes you want to take per main term: ")
            while not numOfClassesPerTerm.isdigit():
                print("Need to input a integer digit")
                numOfClassesPerTerm = input("Enter number of classes you want to take per term: ")

            numOfClassesPerTerm = int(numOfClassesPerTerm)
            course_schdule = createCourseSchedule(course_ordering,numOfClassesPerTerm,prereq_dict)

            for c in course_schdule:
                print(c)

