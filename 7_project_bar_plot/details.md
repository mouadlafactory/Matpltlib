
This project simulates the growth of a **startup SaaS (Software-as-a-Service) application** over a period of 100 days.
Just like a real startup, the company initially grows slowly, then invests in **a marketing campaign**, which creates a **big spike in new users**, and after that growth **stabilizes**.

This reproduces **a real-life business scenario**, not a toy dataset.

---

### 🎯 Main Objective

The main objective of this project is to **analyze user growth over time** and understand:

1. **How explosive growth happens** when a campaign or promotion is launched.
2. **What happens after the campaign** — stabilization or drop.
3. The difference between:

   * **new users** (signups)
   * **active users** (real usage)
   * **churned users** (users who uninstall / stop using)
4. How to calculate **net growth** (new − churn)
5. How to track **cumulative total users** over time (real retention)


| Column          | Description                        |
| --------------- | ---------------------------------- |
| `date`          | Daily time series (100 days)       |
| `new_users`     | Newly registered users per day     |
| `active_users`  | Users who opened the app that day  |
| `churned_users` | Users who stopped using            |
| `total_users`   | Total cumulative users after churn |


---

### 📊 Why this project is useful

| Business problem                                 | What we learn             |
| ------------------------------------------------ | ------------------------- |
| "Are we really growing or just spiking?"         | Trend analysis            |
| "Do users stay after signup?"                    | Retention (active vs new) |
| "Is churn killing our growth?"                   | Churn trends              |
| "What was the impact of our marketing campaign?" | Before/after comparison   |

---

### practice

* Reading a **time-series dataset**
* Cleaning and transforming the data
* Creating **rolling averages** (smooth dashboards look)
* Plotting multiple metrics on the same figure
* Highlighting campaign/event windows
* Annotating important spikes
* Interpreting results like a **real data analyst / product analyst**

---

### 🔍 Final Takeaway

This project is not only about *drawing a line chart* —
it is about **telling the story of a startup through its data**:

> 📈 Growth ≠ Success unless users stay.
> You can get **signups easily**, but **retention is the real proof of value**.

That’s why in this dataset:

* We don’t only track how many signed up,
* We also track **who actually uses the product** (active users),
* And **who left** (churn),
* And we analyze the campaign’s impact visually.




