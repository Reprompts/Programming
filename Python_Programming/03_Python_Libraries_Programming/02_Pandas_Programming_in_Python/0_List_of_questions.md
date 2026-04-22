# Practical Pandas Library Questions 

# 1. Pandas Core Data Structures — Practical Coding Questions

## 1. Creating a Series
Create a Pandas Series from the following list:
```python
[15, 25, 35, 45, 55]
````

Then assign custom index labels: `["a", "b", "c", "d", "e"]`.

---

## 2. Dictionary to Series

Given the dictionary below:

```python
data = {"Alice": 80, "Bob": 90, "Charlie": 85}
```

Create a Series and print only the values for `"Alice"` and `"Charlie"`.

---

## 3. Indexing (loc vs iloc)

Create a Series:

```python
s = pd.Series([100, 200, 300, 400], index=["x", "y", "z", "w"])
```

Write code to:

* Access value using label `"z"`
* Access value using position index `2`

---

## 4. Series Slicing

Given:

```python
s = pd.Series([5, 10, 15, 20, 25, 30])
```

Write code to:

* Slice elements from index position 1 to 4
* Print last 3 elements using slicing

---

## 5. Series Attributes

Create a Series:

```python
s = pd.Series([10, 20, 30, 40, 50], name="numbers")
```

Write code to print:

* index
* values
* dtype
* shape
* size
* name

---

## 6. Series Arithmetic Operations

Given:

```python
s1 = pd.Series([1, 2, 3], index=["a", "b", "c"])
s2 = pd.Series([4, 5, 6], index=["a", "b", "c"])
```

Perform:

* Addition
* Multiplication by 2 on `s1`

---

## 7. Index Alignment Problem

Given:

```python
s1 = pd.Series([10, 20, 30], index=["a", "b", "c"])
s2 = pd.Series([5, 15, 25], index=["b", "c", "d"])
```

Perform addition and observe the result. Print output and explain missing values using code.

---

## 8. Creating DataFrame from Dictionary

Create a DataFrame using:

```python
data = {
    "Name": ["Amit", "Neha", "Ravi"],
    "Age": [22, 24, 23],
    "Score": [85, 90, 88]
}
```

Then:

* Print the DataFrame
* Display only `"Name"` and `"Score"` columns

---

## 9. DataFrame from NumPy Array

Given:

```python
import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
```

Create a DataFrame with column names `["A", "B", "C"]`.

---

## 10. DataFrame Operations + Indexing

Given:

```python
data = {
    "Name": ["A", "B", "C"],
    "Marks": [70, 80, 90]
}
df = pd.DataFrame(data)
```

Perform the following:

* Set `"Name"` as index
* Reset the index back to default
* Print first 2 rows using `head()`
* Display summary using `info()`


# 2. Pandas Data Selection & Indexing — Practical Coding Questions

## Dataset Setup (Use for all questions)
```python
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 35, 28, 22],
    "Department": ["HR", "IT", "Finance", "IT", "Marketing"],
    "Salary": [50000, 70000, 80000, 65000, 45000]
}

df = pd.DataFrame(data)
````

---

## 1. Single Column Selection

Write code to select the `"Name"` column using:

* Bracket notation
* Attribute notation

---

## 2. Multiple Column Selection

Select `"Name"` and `"Salary"` columns and display them as a new DataFrame.

---

## 3. Selecting a Single Row (loc)

Use `loc` to select the row with index `2`.

---

## 4. Selecting a Single Value

Use `loc` to extract the `"Department"` of the employee at index `3`.

---

## 5. Selecting Multiple Rows

Use `loc` to select rows with index `1` and `3`.

---

## 6. Row Slicing using loc

Use `loc` to select rows from index `1` to `3` (inclusive).

---

## 7. Subset of Rows and Columns

Using `loc`, select rows `1` to `3` and only `"Name"` and `"Salary"` columns.

---

## 8. Position-Based Row Selection

Use `iloc` to select the third row.

---

## 9. Position-Based Value Selection

Use `iloc` to extract the value at row position `2` and column position `1`.

---

## 10. iloc Slicing

Use `iloc` to:

* Select rows from position `1` to `3`
* Select first two columns for these rows

---

## 11. Boolean Indexing

Write code to filter all employees whose age is greater than 30.

---

## 12. Conditional Filtering (Single Condition)

Filter employees whose salary is greater than 60,000.

---

## 13. Conditional Filtering (Multiple Conditions)

Filter employees who:

* Work in `"IT"` department
* Have salary greater than 60,000

---

## 14. Combine Filtering + Column Selection

From the filtered IT employees (salary > 60,000), select only `"Name"` and `"Salary"` columns.

---

## 15. Query Method

Rewrite the following filter using `query()`:

* Age greater than 25
* Department is `"IT"`

---

## 16. Query with Variable

Create a variable:

```python
min_salary = 60000
```

Use `query()` to filter employees with salary greater than `min_salary`.

---

## 17. Index Slicing

Use slicing to select rows from index `1` to `3` using standard slicing (`df[]`).

---

## 18. Custom Index + Slicing

* Set `"Name"` column as index
* Use `loc` to slice from `"Alice"` to `"Charlie"`

---

## 19. Boolean Mask Creation

Create a boolean mask for employees whose department is `"IT"`, then use it to filter the DataFrame.

---

## 20. Mixed loc Filtering

Use `loc` with a condition to:

* Filter employees with Age > 25
* Select only `"Name"` and `"Department"`


# 3 Pandas Data Inspection & Exploration — Practice Dataset & Questions

## Dataset

```python
import pandas as pd
import numpy as np

data = {
    "EmployeeID": [101, 102, 103, 104, 105, 106, 107],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace"],
    "Age": [25, 30, np.nan, 28, 22, 40, 35],
    "Department": ["HR", "IT", "Finance", "IT", "Marketing", "IT", "HR"],
    "Salary": [50000, 70000, 80000, None, 45000, 90000, 75000],
    "JoinDate": pd.to_datetime([
        "2020-01-15", "2019-03-10", "2018-07-23",
        "2021-06-01", "2022-09-12", "2017-11-30", "2016-05-20"
    ])
}

df = pd.DataFrame(data)
````

---

## Questions

## 1. Basic Inspection

Write code to:

* Display the first 5 rows
* Display the last 3 rows
* Print the shape of the dataset

---

## 2. Structure & Data Types

Write code to:

* Display complete dataset information using `info()`
* Print data types of all columns
* Identify how many non-null values exist in each column

---

## 3. Summary Statistics & Distribution

Write code to:

* Generate summary statistics for all numeric columns
* Calculate mean, median, and standard deviation of `"Salary"`
* Plot a histogram of `"Salary"`

---

## 4. Categorical Analysis

Write code to:

* Count occurrences of each `"Department"` using `value_counts()`
* Find number of unique departments
* List all unique department names

---

## 5. Missing Data Analysis

Write code to:

* Check for missing values in the dataset
* Count missing values in each column
* Identify which columns contain any missing data


# 4 Pandas Data Types & Conversion — Practical Coding Questions

## Dataset

```python
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": ["25", "30", "35", "unknown"],
    "Salary": ["50000", "60000.5", "75000", "90000"],
    "JoinDate": ["2022-01-10", "2021-06-15", "invalid_date", "2020-09-20"],
    "Department": ["HR", "IT", "Finance", "IT"]
}

df = pd.DataFrame(data)
````

---

## 1. Inspecting Data Types

Write code to:

* Display the data types of all columns using `dtypes`
* Identify which columns are stored as `object`
* Print memory usage of the dataset using `memory_usage()`

---

## 2. Numeric Conversion & Error Handling

Convert `"Age"` and `"Salary"` columns to numeric types.

Requirements:

* Use `pd.to_numeric()`
* Handle invalid values using `errors="coerce"`
* Print the DataFrame after conversion
* Check how many `NaN` values appear after conversion

---

## 3. Datetime Conversion

Convert the `"JoinDate"` column into datetime format.

Requirements:

* Use `pd.to_datetime()`
* Handle invalid dates using `errors="coerce"`
* Print updated data types
* Extract:

  * Join year
  * Join month
* Find the difference between earliest and latest join date

---

## 4. String & Category Conversion

Perform the following conversions:

* Convert `"Name"` column to Pandas `"string"` dtype
* Convert `"Department"` column to `"category"` dtype
* Print available categories
* Rename category `"HR"` to `"Human Resources"`

---

## 5. Complete Data Cleaning Workflow

Using the dataset above, perform a full data type cleaning process:

Tasks:

* Convert `"Age"` to numeric
* Convert `"Salary"` to numeric
* Convert `"JoinDate"` to datetime
* Convert `"Department"` to category
* Print final `dtypes`
* Print memory usage before and after conversion
* Display cleaned DataFrame


