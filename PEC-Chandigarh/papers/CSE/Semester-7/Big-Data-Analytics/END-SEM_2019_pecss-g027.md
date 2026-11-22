# Big Data Analytics (CSN409) - End-Semester 2019

- **Institute:** Punjab Engineering College (Deemed to be University), Chandigarh
- **Department:** CSE - Computer Science and Engineering
- **Semester:** 7
- **Course:** Big Data Analytics
- **Course code:** CSN409
- **Exam:** End-Semester
- **Programme:** B.Tech / B.E.
- **Year:** 2019
- **Pages:** 2
- **Paper PDF:** [END-SEM_2019_pecss-g027.pdf](END-SEM_2019_pecss-g027.pdf)
- **Source:** [1](https://github.com/PEC-CSS/PEC-Previous-Year-Papers/blob/main/Big%20Data%20Analytics/Big%20Data%20Analytics%20-%202.jpg), [2](https://github.com/PEC-CSS/PEC-Previous-Year-Papers/blob/main/Big%20Data%20Analytics/Big%20Data%20Analytics%20-%200.jpg) (PEC-CSS GitHub repo)

> Text below is OCR of scanned/photographed pages. Equations, diagrams and tables
> are often garbled - always check against the PDF before solving.

## Solutions

_Not added yet._

## OCR transcript - page 1

```text
No

Punjab Engineering College

oo
(Deemed to be University)
»End-ferm Examination
' 5
Programme: B.Tech (CSE)
Year/Semester 2019/Seventh(19201)
Course Name: Big Data Analytics Course-Code:CSN-409
Maximum Marks: 60 ‘Time allowed: 180 mins
Notes: ah
45 Alt questios are COmPUBATD: rite the solutions, should please check the question paper for any diserepa

fore tating 10

The candidates. (elven he question per of ight course code

| Marks

aBig

ats ensure that hey BB
Fain Analytic lab OF 100 computers, Witha neat block [1 +2=3

|

Question __
Ben CSE
j- Da SE purose of nsesary components involve to deploy Hadoo cist. anaes
| na ig Data environment nd what ceumstanes HDF is preferred compared 10 RDBMS? |» marks
| Write justilication for yours answer with at least three supportive points.
|S TFAF Suppose we want to use Big Data Analytic inthe development of smart ety project. Derive | 3 marks
four major chile ent this and how it can be useil for this project?
| Justify the purpose of configuration files handoop-env-sh, coresite.xml, hdf-sitexml and yamn- | 3 marks
in setting up the Apache Hadoop Big Data cluster. f
fe the Tour major differences between I1Base and RDBAIS data storage mechanism using | 2¥2=4 "|
‘tabular format. Describe in brief the functional architecture of HBase framework. marks
| \y& Explain two major limitations of the Apache Hadoop Map Reduce cluster. How ‘Apache Spark | 3 marks
\ solves it using Resilient Distributed Dataset (RDD)? *
| | GA sustity purpose of Abstract Syntax Tree in Apache Hive and with a neat block diagram | 1+3 =
| y illustrating the functional architecture of Hive framework. 4 marks
|| GF Develop an Apache Spark Seala/Python (RDD) programming model to evaluate the Frequency | 4 marks
of occurrence of words from a large data set.
{#4 Consider allowing sample daa for studenten deptenv in the following format W55 |
| [ Rollno [Name] CGPA ] [Rollne [Ocpt.Name | University | pmarks |
001 | tohn [3.0 | 001 CSE Harvard
| |[(902 "tock Tao [oor [ec | Stanford =
| [003 Harvard
Food | cra Yaie
08 | CSE mit | |
(007 | Eleerical [Stanford]

“Analyze this data set using Apache PIG scripts to perform the following operations:
|

‘in bwo relations namely: “Student* and “Department” based on the “Roll no’ column,
Hy Todisplay the details of students who belong to MIT and Stanford University.
©) To ind the tuples of those students where COPA is greater than 3.5. :
is of all students trom Harvard University.
2d by thee students, CGPA >= 4.0 place

) To display the det
©) To partition a relation based on CGPA acqui

|
ee
|
|

relation )

CGPA<4.0, place it into relatio
```

## OCR transcript - page 2

```text
———  ——

——— 5 — is dataset | 1*5=5
4 ‘Sample data for sporie.csv in the following format. Analyze this Farha
| HiveQL. programming langange to perfana the following operations: :
| tent . ig [Silver
| untry | Sport __| Gold _| SI
2 Tolls the foal number of gold and silver [Nome | Countey | Spert_—__ Geld
| inedals won by India, “" Tiichael | canal Ee
| AH To fist the numberof medats won by [ven Canada _| Swimming —1
| Australia in Cricket © [coven est aming [212
Sy To display the name oF countries that won | Aa_—| AUS Footbal [4 [4
| gold medals in Swimming, sy ee Toning peal
| \@ ‘To find out the count of the total number [RY india | Swimming [312
| of athletes in each sports category. Ryan nada | Swimming | 8 [4
| 1&6 To disptay all tuples data order by sports Ryan ~yeanada | Swimming [6 [3
, | sategory ‘Michael | Australia _| Cricket 4 a 4 i
| el jing umber of training programs 5
j } (i). Consider the following sample dataset education.csv regarding the nu ‘ations: marks

if ‘ical education organii
| conducted on the mentioned technology areas at different technical r ae
|_| Analyze this dataset using Apache Spark Seala (RDD) programming language t0

following operations laa | Course | Total
cows conducted by UT iydebad, "| EDawenbed | Baekchain a

To get the sum of total courses Pree cenagan Teyber Security 180

conducted by NITTTR Chandigarh. | (r yderabod ML 416
pate display all tuples data for IT Fyirrra Chandigarh [Big Data 250
[Do tind out how many orsizaons | qeeaaiRe; — Cou comostng S32
| have conducted taining on both Bis Fyirrrechandgarh [cyber Secuniy [315

loop uses replication to achieve fault tolerance. How is this achieved in Apache | 2+2=4
Hlustrate about the four major libraries that constitute the Spark ecosystem.
|

| (i), Consider the following dataset automobile.csy. This dataset has a different characteristic such

| gs company name, mileage and price. Write Python/R scrip!

a (0 perform the following operations:
14) To display first and last four rows, S.No Mileage | Price

| |) To lisplay company name and price of most Fy 24 73950
{cs Toulsply count of oa ars pes com : eae
|a) To display each company's fichen ais 3 era 6 se
|e) To tind ow average price of BMW care ee is see
r ‘erage price of BMW cars, S__[JAGUAR | a5 32250
| 6 JAGUAR 1s 35550

| (ii). Suggest a technique with supportive Big Data analytics packages which will you adapt to find | 4 marks
the opinion of the buyer of an el

lectronic gadget from social sites. The output of the analysis should
|_| reveal whether the user has a positive or negative or neutral sentiment about that product.

|
\Gid) Give appropriate justification, why NoSQL plays significant role in handling Big Data? | 2 marks
\ | Mlustrate the four major Properties of NoSQL database technology.

\Giy). Justify yours answer,

: 1 is data analytics and data visualization are same? Explain regression |
\__Laiialysis. grouping methods

c 4 marks
and multiple equation models Big Data visualization techniques,
```
