## Homework

The homework notebook can be found at [hw.ipynb](./hw.ipynb).

### Q1. Pandas version

What's the version of Pandas that you installed?

You can get the version information using the `__version__` field:

```python
pd.__version__
```

### Getting the data 

For this homework, we'll use the Car Fuel Efficiency dataset. Download it from <a href='https://raw.githubusercontent.com/alexeygrigorev/datasets/master/car_fuel_efficiency.csv'>here</a>.

You can do it with wget:
```bash
wget https://raw.githubusercontent.com/alexeygrigorev/datasets/master/car_fuel_efficiency.csv
```

Or just open it with your browser and click "Save as...".

Now read it with Pandas.

<details>
<summary>Solution</summary>


**Answer**: `2.3.2`
</details>


### Q2. Records count

How many records are in the dataset?

- 4704
- 8704
- 9704
- 17704

<details>
<summary>Solution</summary>

- [ ] 4704
- [ ] 8704
- [x] 9704
- [ ] 17704


**Answer**: 9704
</details>

### Q3. Fuel types

How many fuel types are presented in the dataset?

- 1
- 2
- 3
- 4

<details>
<summary>Solution</summary>

- [ ] 1
- [x] 2
- [ ] 3
- [ ] 4

**Answer**: 2
</details>

### Q4. Missing values

How many columns in the dataset have missing values?

- 0
- 1
- 2
- 3
- 4

<details>
<summary>Solution</summary>

- [ ] 0
- [ ] 1
- [ ] 2
- [ ] 3
- [x] 4

**Answer**: 4
</details>

### Q5. Max fuel efficiency

What's the maximum fuel efficiency of cars from Asia?

- 13.75
- 23.75
- 33.75
- 43.75

<details>
<summary>Solution</summary>

- [ ] 13.75
- [x] 23.75
- [ ] 33.75
- [ ] 43.75

**Answer**: 23.75
</details>

### Q6. Median value of horsepower



1. Find the median value of `horsepower` column in the dataset.
2. Next, calculate the most frequent value of the same `horsepower` column.
3. Use `fillna` method to fill the missing values in `horsepower` column with the most frequent value from the previous step.
4. Now, calculate the median value of `horsepower` once again.

Has it changed?


- Yes, it increased
- Yes, it decreased
- No

<details>
<summary>Solution</summary>

- [x] Yes, it increased
- [ ] Yes, it decreased
- [ ] No

**Answer**: Yes, it increased
</details>

### Q7. Sum of weights

1. Select all the cars from Asia
2. Select only columns `vehicle_weight` and `model_year`
3. Select the first 7 values
4. Get the underlying NumPy array. Let's call it `X`.
5. Compute matrix-matrix multiplication between the transpose of `X` and `X`. To get the transpose, use `X.T`. Let's call the result `XTX`.
6. Invert `XTX`.
7. Create an array `y` with values `[1100, 1300, 800, 900, 1000, 1100, 1200]`.
8. Multiply the inverse of `XTX` with the transpose of `X`, and then multiply the result by `y`. Call the result `w`.
9. What's the sum of all the elements of the result?

> **Note**: You just implemented linear regression. We'll talk about it in the next lesson.

- 0.051
- 0.51
- 5.1
- 51

<details>
<summary>Solution</summary>

- [ ] 0.051
- [x] 0.51
- [ ] 5.1
- [ ] 51

**Answer**: 0.51
</details>

## Submit the results

* Submit your results here: https://courses.datatalks.club/ml-zoomcamp-2025/homework/hw01
* If your answer doesn't match options exactly, select the closest one