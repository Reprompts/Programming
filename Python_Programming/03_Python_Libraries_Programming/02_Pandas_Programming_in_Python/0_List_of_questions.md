# Practical Pandas Library Questions 

# Pandas Core Data Structures — Practical Coding Questions

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

