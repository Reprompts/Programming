## Practical NumPy Questions

1. Create a NumPy array with values `[10, 20, 30, 40, 50]`. Print the array and its data type.

2. Create two NumPy arrays `[1,2,3]` and `[4,5,6]`. Perform element-wise addition and print the result.

3. Create a NumPy array from 1 to 10 using a NumPy function (not a Python list). Print the array.

4. Multiply all elements of a NumPy array `[2,4,6,8]` by 5 and print the output.

5. Create a 2D NumPy array:

   ```
   [[1,2,3],
    [4,5,6]]
   ```

   Print the array and its shape.

6. Create a NumPy array `[5,10,15,20]` and calculate:

   * Sum
   * Mean

7. Create a NumPy array `[1,2,3,4]` and add 10 to each element using broadcasting.

8. Create a NumPy array of size 5 with all elements as 0, then change it to all 1s.

9. Create a NumPy array `[1,2,3,4,5]` and compute:

   * Square of each element
   * Square root of each element

10. Create two arrays:

```
a = [1,2,3]
b = [10,20,30]
```

Perform element-wise multiplication and print the result.

---

### 11.

Create the following arrays:

* A scalar (0D) with value `100`
* A 1D array `[1, 2, 3]`
* A 2D array `[[1,2],[3,4]]`

Print the **number of dimensions (`ndim`)** for each.

---

### 12.

Create a 2D NumPy array:

```
[[10, 20, 30],
 [40, 50, 60]]
```

* Print its **shape**
* Print its **total size**
* Verify that size = rows × columns

---

### 13.

Create an array using `np.arange()` from **5 to 15**

* Print the array
* Print its **data type**
* Convert it to `float` and print again

---

### 14.

Create a NumPy array using `np.linspace()` from **0 to 5** with **6 elements**

* Print the array
* Print its **shape and ndim**

---

### 15.

Create a **3×3 matrix of zeros**
Then:

* Convert it into a matrix of ones
* Print both arrays

---

### 16.

Generate a **2×2 random array** using NumPy

* Print the array
* Print its **dtype, itemsize, and total memory (nbytes)**

---

### 17.

Create an array:

```
[1, 2, 3, 4]
```

* Print:

  * `itemsize`
  * `nbytes`
* Manually verify:

  ```
  nbytes = itemsize × number of elements
  ```

---

### 18.

Create an array with mixed values:

```
[1, 2.5, 3]
```

* Print the array
* Print its **dtype**
* Explain why NumPy chose that dtype

---

### 19.

Create a 3D array:

```
[
 [[1,2],[3,4]],
 [[5,6],[7,8]]
]
```

* Print:

  * `ndim`
  * `shape`
  * `size`

---

### 20.

Create any 2D NumPy array and perform **complete inspection**:
Print:

* Array itself
* `ndim`
* `shape`
* `size`
* `dtype`
* `itemsize`
* `nbytes`
* `flags`

---

