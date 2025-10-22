### ✅ What is a Boxplot?

A **boxplot** is used to visualize **the distribution of a numerical variable** and detect:

* Median (central value)
* Quartiles (spread of middle 50%)
* Outliers (extreme values)
* Variation / inequality

It answers the question:

> “How is the data spread or distributed?”

---

### ✅ When do we use a Boxplot?

| Use Case               | Example                 |
| ---------------------- | ----------------------- |
| Compare groups         | Male vs Female salaries |
| Detect outliers        | Unusual exam scores     |
| Understand variability | Age spread by education |
| See inequality         | Income in regions       |

---

### ✅ Anatomy of a Boxplot

| Element      | Meaning                         |
| ------------ | ------------------------------- |
| Middle line  | Median (50th percentile)        |
| Box          | Q1 to Q3 (middle 50% of values) |
| Whiskers     | Range of typical values         |
| Dots outside | Outliers (unusual points)       |

---

### ✅ Mini Example (Boxplot Code)

```python
import matplotlib.pyplot as plt
import numpy as np

data = [18, 19, 21, 22, 23, 23, 24, 25, 26, 28, 33, 35]  # ages

plt.boxplot(data, vert=True)
plt.title("Simple Age Distribution Boxplot")
plt.ylabel("Age")
plt.show()
```

This would show:

* Median = around 23–24
* Outliers = 33 and 35 (older candidates)
