### ✅ What is a Scatter Plot?

A **scatter plot** shows the **relationship between two numerical variables**.

It answers:

> “Does X affect Y?”
> or
> “Is there a correlation between variables?”

---

### ✅ When to use a Scatter Plot?

| Use Case    | Example                 |
| ----------- | ----------------------- |
| Correlation | Age vs Acceptance       |
| Trend       | Experience vs Selection |
| Pattern     | Study hours vs grades   |
| Clustering  | Types of applicants     |

---

### ✅ Scatter Example

```python
import matplotlib.pyplot as plt
import numpy as np

experience = [1,2,3,4,5,6,7,8,9,10]
acceptance_score = [2,3,4,5,7,7,8,9,9,10]

plt.scatter(experience, acceptance_score)
plt.title("Experience vs Acceptance Score")
plt.xlabel("Programming Experience")
plt.ylabel("Suitability / Score")
plt.show()
```

If points go **upward**, there is a **positive correlation**
👉 more experience → higher acceptance chance

If points go **downward**, **negative correlation**
If random cloud → **no correlation**
