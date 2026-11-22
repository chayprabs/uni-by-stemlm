# Data Structures (AIN301) - Mid-Semester 2025

- **Institute:** Punjab Engineering College (Deemed to be University), Chandigarh
- **Department:** CSE-AI - CSE (Artificial Intelligence)
- **Semester:** 3
- **Course:** Data Structures
- **Course code:** AIN301
- **Exam:** Mid-Semester
- **Year:** 2025 (read from paper)
- **Pages:** 2
- **Paper PDF:** [MID-SEM_2025_WwGIxv.pdf](MID-SEM_2025_WwGIxv.pdf)
- **Source:** pecpapers.vercel.app, upload id `WwGIxvm8oZH4vxIcX0us`

> Text below is machine OCR of phone photos of the paper. Equations, diagrams and
> tables are often garbled - always check against the PDF before solving.

## Solutions

_Not added yet._

## OCR transcript - page 1

```text
UMN OIe" = oti

Punjab Engineering College (Deemed to be University), Chandigarh

Mid-Term Examination Oct 2025
Year/Semester: 2™ yr/25261

Programme: B.Tech. (CS/CS(AD)
Cc Ourse Name: Data Structures Course Code: CTN301/AIN301
Maximum Marks: 30 Time allowed: 1 Hr 30 Minutes
Notes:

° All questions are compulsory. Assume suitably and state, additional data required, if any.

ir usual meanings in context with subject.

© Unless stated otherwise, the symbols have thei
——————— = sth area. sa EAS he T
Qa | | Mar
No. | ks
ae Convert the below infix expression to postfix expression using stack. Clearly show the operation 5

Performed for each character, the content of stack, and the postfix string after each step.
a—(b+c*d/(e/f *g+h)-i)
|5

2. “Solve the following recurrence relation using the substitution method. |
n

Tn) = 27 (5) +n;7@) =1 |

of length 5. The queue is full when 4 | 5

ircular queue after each operation if the

Ss Ticuaae a circular queue is ‘implemented using an array
elements are stored in the queue. Show the content of the ci
operation is executed successfully, show underflow/overflow otherwise.

Enqueue(1@), Enqueue(2@), Enqueue(3@) , Enqueue(4@),
Dequeue(), Enqueue(6@), Dequeue(), Dequeué( ) , Dequeue(),

| Dequeue(), Enqueue(7@), Enqueue(8@), Dequeue() ‘

| 4. Biased Search is modified binary search where mid is calculated as below: |

| mid = (2*s+e)/3

i where s is the start index and e is end index. Write the pseudo-code for the Biased Search and apply fs

Biased Search to search element ‘x’ in the following sorted list of elements. Show each step clearly.

NOPQRSTUVWXYZ zl
5. [ Consider the following code snippets for node class and PQ (Priority Queue) class:

Enqueue(5@),
Dequeue( sn

class PQ {
node * head;
node * tail;

class node {
int priority;

int key;
| int value; PQ ( ){
node * next; heac = NULL;
node (int p, int k, int v) { tail = NULL;
priority = p; }
| key = k; ENQUEUE (int p, int k, int v)3
value = v; 35
next = NULL;
ti

Write a function in C++ to implement the ENQUEUE operation that inserts a node into a priority

queue implemented using a SLL. The nodes in the SLL should be inserted in such a way that the
priority (i.e., the highest-priority node appears

priority queue remains sorted in descending order of
first).

Page 1 of 2
```

## OCR transcript - page 2

```text
Write a function in C++ to perform addition of two sparse matrices. Each sparse matrix is 5
represented using a SLL in row-wise order. Each node in the SLL contains three data members:
row, col, and value; representing the position and value of a non-zero element in the matrix. Define

a function node* mat_addition(node* mat1, node* mat2); that takes pointers to the two
matrices as input and returns a pointer to the resultant matrix after addition. The node structure in
the SLL is given below.

(Note: When all the non-zero values of the first row are stored first, followed by the values of the
second row, third row, and so on, the matrix is said to be stored in row-wise order.)

class node { if

int row;
int column; —
int value;
node * next;
node (int r, int c, int v) {

row =r;

column = c;

value = v;

next = NULL;

ie
```
