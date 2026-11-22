# Data Structures (CS6301) - Mid-Semester 2023

- **Institute:** Punjab Engineering College (Deemed to be University), Chandigarh
- **Department:** CSE - Computer Science and Engineering
- **Semester:** 3
- **Course:** Data Structures
- **Course code:** CS6301
- **Exam:** Mid-Semester
- **Year:** 2023 (uploader comment)
- **Pages:** 1
- **Paper PDF:** [MID-SEM_2023_kdMz9v.pdf](MID-SEM_2023_kdMz9v.pdf)
- **Source:** pecpapers.vercel.app, upload id `kdMz9veR4blEzb9EOaCV`

> Text below is machine OCR of phone photos of the paper. Equations, diagrams and
> tables are often garbled - always check against the PDF before solving.

## Solutions

_Not added yet._

## OCR transcript - page 1

```text
Punjab Engineering College (Deemed to be University), Chandigarh
Mid-Term Examination Sep 2023

Programme: B.Tech, (AE/CE/EE/ECE/ME/MME/PIE) Year/Semester: 2" yr/23241

Course Name: Data Structures Course Code: CS6301

ee Marks: 25 Time allowed: 1 Hr 30 Minutes
lotes:

e All questions are compulsory. Assume suitably and state, additional data required, if any.
e Unless stated otherwise, the symbols have their usual meanings in context with subject.

fo: No. eee Marks

Convert the below infix expression to postfix expression. Clearly show operation performed for | 6
each character, content of stack, and postfix string after each step.

[a+ (b—c)]*[(d-e)/(f-g+h)]
2. | Considered below implementation of linked list in C++ for both parts (a) and (b):

class Node { class LL {
public: public:
int data; Node* head;
Node* next; LL(){
Node (int dt) { head = NULL;
data = dt; }
next = NULL; }

a) Write a function to implement the function LL::insertM(int key) which inserts a new node | 6
with data key in the middle of linked list. If linked list have 4 nodes, new node will be inserted
after the second node; if 5 nodes then new node will be inserted after third node.

b) Consider a function is implemented as below:
void fun (Node* start) { 3

if (start == Null) return;
cout<< start->data;
if( start -> next != NULL)
fun( start -> next -> next);
cout<< start -> data;
}
What will be the output of the above function for the given linked list?
9-—> 12—> 34-> 37-> 40—> 49

Ss | Consider an Dqueue containing elements {10, 20, 30} where element 10 is at the front. Following | 5

| operations are performed in the same order. Show the content of Dqueue after each operation.

InsertFront(23); DeleteFront( ); DeleteFront( ); InsertFront(28); InsertRear(34); Deletefront( );

InsertRear(45); InsertRear(13); DeleteRear( ); InsertRear(21);

eal Biased Search is modified binary search where mid is calculated as below: 5
mid = (2+s+e)/3

where s is start index and e is end index, For the following sorted list of elements, apply Biased

Search to search element ‘X’. Show each step clearly.

PQRSTUVWXYZ
```
