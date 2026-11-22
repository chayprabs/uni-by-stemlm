# Data Science and Machine Learning (DSN4005) - End-Semester 2025

- **Institute:** Punjab Engineering College (Deemed to be University), Chandigarh
- **Department:** CSE-DS - CSE (Data Science)
- **Semester:** 4
- **Course:** Data Science and Machine Learning
- **Course code:** DSN4005
- **Exam:** End-Semester
- **Year:** 2025 (uploader comment)
- **Pages:** 3
- **Paper PDF:** [END-SEM_2025_u9wxof.pdf](END-SEM_2025_u9wxof.pdf)
- **Source:** pecpapers.vercel.app, upload id `u9wxofzLwbXjwEYFk4DP`

> Text below is machine OCR of phone photos of the paper. Equations, diagrams and
> tables are often garbled - always check against the PDF before solving.

## Solutions

_Not added yet._

## OCR transcript - page 1

```text
AN

PUNJAB ENGINEERING COLLEGE CHANDIGARH
End-Semester Examination

Programme: B.Tech CSE (DS) Year/Semester: 4""/24252
Course Name: Data Science and Machine Learning/AIML (Backlog) Course Code: DSN4005/ES1701
Maximum Marks: 60 Time allowed: 3 Hours

Q. No. Marks

1.(a)| Differentiate between correlation and regression with respect to their purpose, 05
causation and variables. Further, find the sales of a company (in million dollars) for
each year as shown in the table below:

x (year) | 2005 | 2006 2007 2008 2009 |
(sales) [12 [19 29 37 45
(i) Find the least square regression line y = ax + b.
(ii) Use the least squares regression line as a model to estimate the sales of the
company in 2012.
(b) | Use the given two methods to normalize the following group of data: 05
Marks | 8 | 10 | 15 | 20
(i) Method 1: min-max normalization by setting min = 0 and max = 1
(ii) Method 2: z-score normalization

(c)| You have a "Product Category" feature with 200 unique categories. 05
Which encoding method: Label encoding / One-hot encoding is better for decision trees
and why? Further, one-hot encode the "Weather" feature with categories {Sunny, Rainy,
Cloudy} for the following data:

ID 1 2 [3 4
Weather Sunny Rainy | Cloudy Rainy mal
2.(a)| A confusion matrix for a binary classification problem is given below: 05
[| ___|Predicted Yes| Predicted No
Actual Yes
[Actual No |
What is the Precision, Recall, and F1 Score for the class "Yes"?

(b) | A company is developing a machine learning model to classify emails as "spam" or "not | 95
spam." During training, they experiment with different models and observe the following
behaviors:

Model X: Achieves 99% accuracy on the training set but only 72% accuracy on the test set.
Model ¥: Achieves 68% accuracy on both the training and test sets.
Model Z: Achieves 88% accuracy on the training set and 85% on the test set.

(i) Identify which model is overfitting, underfitting, and generalizing well.

(ii) Explain the reason behind your choice in each case.
```

## OCR transcript - page 2

```text
3.(a)

(b)

You're given a dataset of customers with two features: Age and Income, and a binary
label Buys Product.

(i) Compute Euclidean distance from a new customer to each of the 7 existing data points.
(ii) Use K = 3 to find the 3 nearest neighbors.

(ili) Based on majority voting, predict whether the new customer will buy the product.

You are given a dataset with 7 rows and 3 attributes. The goal is to classify whether a
person will Buy a Laptop (Yes or No).

Income |Student| Buy_Laptop

(i) What is the entropy of the entire dataset?
(ii) Calculate information gain for each of three attributes: Age, Income, and Student.
(iii) Which attribute would be selected as the root node for the decision tree?

m= YO.

Galsactio,

Ds,

4(a) |

Consider the following dataset:

Red | Round | Apple _|

Chilli

Cucumber

Now, you are given a new object with following attribute values:
e Color=Red
e Shape = Long

Predict the class (Apple, Chili, or Cucumber) using Naive Bayes Classifier.

leas

05
```

## OCR transcript - page 3

```text
ay

y
1 (b) | Suppose you are designing an SVM-based system to detect fraudulent credit card 05
] transactions. The data has features like Transaction amount, Merchant type, Time of
transaction, Device used and Location (Jatitude/longitude). Some patterns are nonlinear,
for example, certain frauds happen only at specific times and locations together. Answer
the following questions:
(i) Would a linear SVM be sufficient? Why or why not?
(ii) Design/propose a Kernel Trick idea that could help SVM in this case.
(iii) Name a specific kernel type you would suggest and briefly justify.
5.(a)| Suppose you have a dataset of 1000 points. You apply DBSCAN with different ¢ values. 05
e With ¢=0.5, you get 10 clusters and 200 noise points.
e With e= 1.5, you get 2 clusters and 10 noise points.
(i) Explain why increasing ¢ decreases the number of clusters.
(ii) In your opinion, which ¢ would better capture small dense clusters?
(b) | The table below is a distance matrix for 6 objects: 05
A B G D Era 8
A 0
Bae O:t2e70
(exp ass los ple (0)
D/|084 0.16 014 O
EB170:28: 0:77 =::0:70 310452520
F 0:34 0.61 0.93. 0.20'0.67. <0
Show the final result after using any one of the clustering methods: k-means clustering or
dendogram clustering (HAC) with detailed explanation of the steps.
(c) | A company collects data on two variables from 1000 customers for financial forecasting: 05
e Variable 1 (V1): Age (in years)
e Variable 2 (V2): Annual Spending (in $)
They notice that:
e Variable 1 and Variable 2 are highly positively correlated (correlation ~ 0.95).
e Variable 1 has a much larger variance than Variable 2.
Based on above information, if you perform PCA, describe:
(i) How many principal components will you need to explain most of the variance?
(ii) Will the first principal component be closer to V1, V2, or some mix?
```
