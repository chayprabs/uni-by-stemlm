# Python Programming (CSN213) - Mid-Semester 2019

- **Institute:** Punjab Engineering College (Deemed to be University), Chandigarh
- **Department:** CSE - Computer Science and Engineering
- **Semester:** 3
- **Course:** Python Programming
- **Course code:** CSN213
- **Exam:** Mid-Semester
- **Programme:** B.Tech / B.E.
- **Year:** 2019
- **Pages:** 2
- **Paper PDF:** [MID-SEM_2019_pecss-g205.pdf](MID-SEM_2019_pecss-g205.pdf)
- **Source:** [1](https://github.com/PEC-CSS/PEC-Previous-Year-Papers/blob/main/Papers/Python%20Programming/Python%20Programming%20-%202.jpg), [2](https://github.com/PEC-CSS/PEC-Previous-Year-Papers/blob/main/Papers/Python%20Programming/Python%20Programming%20-%201.jpg) (PEC-CSS GitHub repo)

> Text below is OCR of scanned/photographed pages. Equations, diagrams and tables
> are often garbled - always check against the PDF before solving.

## Solutions

_Not added yet._

## OCR transcript - page 1

```text
arh

Punjab Engineering College (Deemed to be University), Chan
Mid-Term Examination 2019

Year/Semester: 2" year/19201

Course Code: CSN213

Time: 1 Hr 30 Minutes

B.Tech,
: Python Promgramming
im Marks: 40

{All questions are compulsory
[Unless stated otherwise, the symbols have their usual meanings in context with subject. Assume suitably and state,

additional data required, iFany.

- [Marks ~

LQuNo: =
1. Write one line code for the following task. Code longer than one line will attract zero marks, 542
8) List of elements at odd indices of a list L. Assume list L exists already.
b)_Listof odd clements of a list L, Assume list L exists already.
) List of numbers between 2000 and 4000 (both included) which are either “divisible by 5” or
“divisible by 3 and has 7 at the units place”
4) Create dictionary where value is square of Key in range | to R(both included). Assume R
exist already.
©) Listof list of size MxN where element is 0if (cow index + column index) is divisible by two
else |. Index starts from 0, Assume Mand N exists already.
z There exist a file which siores pairs of name and JobType in following format ie, name followed | 5+5

by its JobType in next line and so on.
Namet

Assistant Professor
Name2

Associate Professor
Name3

Professor

Name4

Assistant Professor

(i) Write the code, if the user enters a name, 1 oufputs the JobType part of the frst pair
is found, it ouputs "No match found”,

matching the name. Ifo mate!

‘Output: Assistant Professor

Gi) Using the ereated file, print all the names corresponding to the each JobType, Suppose, it
the user enters JobTypes, it outputs all names matches. Which data structure would you
use to print the output?

L ‘Output: JobTypei: (<Namet>, <Name2>..), JobType2: [<Namels,
```

## OCR transcript - page 2

```text
Write the code with outputs
()/ Write a function named check repeated that picks a random word from the list that does
not have any repeated fetters. Input should be a list of at least ten words, some of which
have repeated letters and some which don't

Write a function named ordered three that is passed three integers, and returns true if the
three integers are in order from smallest to largest, otherwise it returns false,

345

Golfections” implements specialized container datatypes providing alternatives to Python's
general purpose builtin containers, dict, ist, set, and tuple. One of the specialized container
datatypes is “deque” which supports functionality of double ended queue, Below are initialization
and some methods supported by “deque” with their definitions.

class collections deque({iterable[, maxlen}}); Returns @ new deque object initialized left-to-right
(using append()) with data from iterable. If iterable isnot specified, the new deque is empty. If
imalen is not specified or is None, deques may grow to an arbitrary length. Otherwise, the deque
is bounded to the specified maximum length,

append(x): Add xto the right side of the deque.

appendieft(x

dd x to the left side of the deque.
‘extend(iterable): Extend the right side of the deque by appending elements from the iterable
argument.

extendlefi(iterable): Extend the left side of the deque by appending elements from iterable. Note,
the series of left appends results in reversing the order of elements in the iterable argument,

index(x[, start, stop]}}): Return the position of x in the deque (at or after index start and before
index stop). Returns the first match or raise ValueError if not found,

pop(): Remove and return an element from the right side ofthe deque. If no elements are present,
raises an IndexError.

popleft(): Remove and return an element ftom the left side of the deque, Ifno elements are
present, raises an IndexError.

remove(value): Remove the first occurrence of value. Ifnot found, raises a ValueError,

Example.
>>> from collections import deque
>>> d=deque({1,2,3])

>>> d.pop()

3

Using above supported methods, implement stack and queue,

545
```
