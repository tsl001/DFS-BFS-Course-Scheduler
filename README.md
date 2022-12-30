# DFS-BFS-Course-Scheduler
- We can represent each class/course as a node

- The graph would be a directed graph such that if a node points to another node then the source node is a prerequisite to the destination node

- Try to implement in DFS and BFS (can create a mode to use one of the traversals later as an added feature)

- Need to know whether using quarter or semester system

- Input format could be\
 (CSE 101, CSE 123),(CSE 151),(CSE 123,CSE 21, CSE 31),(CSE 31)\
 such that the first element in each of the list would be the course and the remaining elements from index 1 onwards would be the prerequisites for the course
 we would store this list of lists into a hash map/dicitonary format
 so one example of what the dictionary would look like after with this example would be\
 {\
&emsp;CSE 101: [CSE 123],\
&emsp;CSE 123: [CSE 21, CSE 31],\
&emsp;CSE 151: [],\
&emsp;CSE 31: []\
&emsp;...\
 }

- We'll want to check first to see if the courses are even possible to complete

- Should be similar to leetcode problem "Course Schedule" except that we'll need to return some type of list

- User would have to specify the maximum number of courses they'd be willing to take each quarter

- After we've implemented the logic of the program we can focus on making an interface for it to make it look more appealing


Notes:
- We can assume that each node is unique (no duplicate courses)
- Later on we can try to add constraints such that some courses are offered only some quarters/semesters
- Write the program in python but then if you want to for extra practice you can try rewriting it in C or C++
- I'm unsure how much time I'll have to put into this project. If I am not offered back a position for Amazon SDE role then I can probably spend more time on this project
otherwise I will probably focus more of my time on the internship.