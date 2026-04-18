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


21.

Create an array using np.empty() of size 5

Print the array
Observe the values
Then assign values [1,2,3,4,5] manually and print again

22.

Create a 2×3 array filled with the value 7 using np.full()

Print the array
Verify all values are identical

23.

Use np.logspace() to generate 4 values from 10¹ to 10⁴

Print the array
Explain how the values are generated

24.

Create:

A 4×4 identity matrix using np.identity()
A 3×5 matrix using np.eye()

Print both and compare their structures

25.

Generate random arrays using NumPy:

A 2×2 array using np.random.rand()
A 2×2 array using np.random.randint(1,10)
Set a random seed and regenerate one array

Print all outputs and observe differences


---


### 26.

Create a NumPy array:

```
[1, 2, 3, 4]
```

* Print the array
* Print its **dtype**
* Explain what the dtype represents

---

### 27.

Create two arrays:

* One with `dtype=np.int8`
* One with `dtype=np.int64`

For both arrays:

* Print `itemsize`
* Compare memory usage

---

### 28.

Create a NumPy array:

```
[10, 20, 30]
```

* Convert it to `float32` using `dtype` while creation
* Print the array and dtype
* Print `itemsize`

---

### 29.

Create a float array:

```
[1.5, 2.7, 3.9]
```

* Convert it to integer using `.astype()`
* Print the result
* Observe what happens to decimal values

---

### 30.

Create an array:

```
[0, 1, 2, 0, 5]
```

* Convert it to boolean using `.astype(bool)`
* Print the result
* Explain how NumPy converts values to boolean

---

### 31.

Create a NumPy array:

```
[10, 20, 30, 40]
```

* Create a boolean mask using condition `> 25`
* Use the mask to filter elements
* Print both mask and filtered result

---

### 32.

Create a complex number array:

```
[1+2j, 3+4j, 5+6j]
```

* Print the array
* Print its dtype
* Extract and print:

  * Real part
  * Imaginary part

---

### 33.

Create an array with mixed values:

```
[1, "hello", 3.5]
```

* Force `dtype=object`
* Print the array and dtype
* Try performing a mathematical operation (like `+1`) and observe behavior

---

### 34.

Create an integer array:

```
[1, 2, 3, 4]
```

Convert it step-by-step:

* To float
* To string
* Print dtype after each conversion

---

### 35.

Create two arrays:

* One with `float32`
* One with `float64`

For both:

* Print `dtype`
* Print `itemsize`
* Explain which one uses more memory and why

---

