# Data Structures (CS6301) - End-Semester 2023

- **Institute:** Punjab Engineering College (Deemed to be University), Chandigarh
- **Department:** CSE - Computer Science and Engineering
- **Semester:** 3
- **Course:** Data Structures
- **Course code:** CS6301
- **Exam:** End-Semester
- **Year:** 2023 (uploader comment)
- **Pages:** 2
- **Paper PDF:** [END-SEM_2023_rgxpXw.pdf](END-SEM_2023_rgxpXw.pdf)
- **Source:** pecpapers.vercel.app, upload id `rgxpXw6Mes6SIXZG4fW7`

> Text below is machine OCR of phone photos of the paper. Equations, diagrams and
> tables are often garbled - always check against the PDF before solving.

## Solutions

_Not added yet._

## OCR transcript - page 1

```text
Punjab Engineering College (Deemed to be University), Chandigarh
End-Term Examination Dec 2023

Pitbn ae oon (AE/CE/EE/ECE/ME/MME/PIE) AS ik eas om Yet
ourse Name: Data Structures Coarse ie:
Maximum Marks: 80 2210 7036 Time allowed: 3 hrs
Notes:

All questions are compulsory. Assume suitably and state, additional data required, if any.
Unless stated otherwise, the symbols have their usual meanings in context with subject.

[Q. No. zi ; | Marks
i. a. Use the substitution method to solve the following recurrence relation: {5
T(n) = 2T(m/2) +n
T(2) =1 |
b. With the help of an example demonstrate AVL trees don’t suffer from skewness. 5
12. | Write a program in C++ to implement stack using linked list for storing non-negative | 3+3+4
integers using classes. Assume your system has infinite memory space. Your program
should support following operations:
i. push function which inserts input integer at the top of stack. Time complexity for
push function should be O(1). |
ii. pop function which removes and returns the integer at the top of stack if stack is
not empty and -1 otherwise. Time complexity of pop function should be O(1).
iii. | Implement a max function which returns the maximum integer present in the stack
if stack is not empty and -] otherwise. Time complexity for max function should
be O(i). max Function having time complexity more than O(1) will get no marks.
a) a. A Priority Queue (PQ) is implemented using a Min-Heap. Elements in Min-Heap is | 5
inserted as (key, priority) pair. Element with lower priority value has higher priority.
Perform the following operation on the Min-Heap and show the content of heap after
each operation.
Enqueue(23, 3); Enqueue(28, 2); Enqueue(34, 1); Enqueue(45, 2); Enqueue(13, 4);
Dequeue(); Enqueue (21, 6); Enqueue(17, 3); Enqueue(55, 1); Dequeue(), |
b. Evaluate the following postfix evaluation and show each step clearly. 5
987654—-—+4+/%* *
4. it Perform the following operations on the given 4-order B “a0
Tree in the given sequence and show each step clearly.
: [aT sfio|
Insert(15), Insert(14), Delete(9), Delete(4), Delete(5) Bor aS Oren
GME)
nh zi Perform the Bubble Sort on the following array of positive integers. Show the content of | 10
the array after each iteration along with total number of swaps in that iteration.
13, 16, 11,4, 12, 6, 7,90, 67,5, 20
```

## OCR transcript - page 2

```text
Consider the graph given and step-by-step
construct the Minimum Spanning Tree using
Prim’s algorithm. Consider F as the starting vertex.
Show each step clearly.

Consider the data of various flights operated by | S.No. | Sre | Dst Cost Voisin 248
Speed Airlines between source and destination 1. A Boe ne
cities along with its price and duration of flight. = TR TC t 13,000 5 hrs |
a. Represent the given flight data in form of Iq aaslipal 25,000 | 10 hrs
directed graph along with edge information. | 5. |C_|E | 7,000 | 3 hrs
b. Find the minimum time taking path from (6. E |D_| 11,000 Ahrs
city ‘B’ to all other cities using Dijkstra’s LZ. By A | pan 38 nes 4
algorithm. Show each iteration clearly. 4 . TB 112,000 bana 4
Also, mention the path and total cost of (Jo, |p B__ | 28,000 | 11 hrs
each path. [ii [E [Cc | 7,500_| 3.5 hrs
12. D |A_ | 9,500 | 5 hrs
10

| will be as follows:

Subset Sum problem is defined as “Given a set A of non-negative integers, and a value K, |
| determine if there is a subset of the given set with sum equal to given K”. |
One simple solution is to generate all possible subsets and finding their sum. If there exist
a subset having sum equal to K, then return ‘True’ else ‘False’. Time complexity of this
solution will be exponential as it explores all possible subsets.

Since smaller subsets are part of larger subsets, e.g. {1,2} is part of {1,23}. this
characteristic can be utilized to design Dynamic Programming solution. DP solution will
work as follows:

We will create a 2D array DP of size (A.size() + 1) * (K + 1) of type boolean. The state
DP[i]{j] will be ‘True’ if there exists a subset of elements from A[1....i] with sum value =
‘j’. DP[O][j] will be initialized with ‘False’ for all values of ‘j’ followed by DP[i]{0}
initialized with ‘True’ for all values of ‘i’. The condition to populate the remaining matrix

GiCAD ee uh oe Ip
BPli\|j] = DPli— 1){7]
else
DP\illj] = DPli-- UF] OR DPIi - Uj - Ali-1])

Using the above approach, populate the DP array for the given instance:

— bs

A =[3,9,4,8,5,2] and K = 10.

te,
```
