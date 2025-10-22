This block creates a **dashboard-style time series visualization**, combining multiple metrics with annotations and a highlighted campaign period.

---

## 1️⃣ Setup the Figure

```python
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

plt.figure(figsize=(14, 7))
```

* `figsize=(14,7)` → Wide dashboard look (better readability).
* We import `mdates` to format the x-axis as real dates (not plain text).

---

## 2️⃣ Primary Axis (Left Side)

```python
ax = plt.gca()
ax.plot(df["date"], df["new_users_ma7"],  linewidth=2.5, label="New Users (MA7)")
ax.plot(df["date"], df["active_users_ma7"], linewidth=2.5, label="Active Users (MA7)")
```

✅ This axis displays **growth**, i.e., users joining and staying active.
✅ We use the **7-day moving average** to smooth the lines.
✅ `linewidth=2.5` makes the lines thicker → more like a dashboard.

---

## 3️⃣ Secondary Axis (Right Side)

```python
ax2 = ax.twinx()
ax2.plot(df["date"], df["churned_ma7"], linewidth=2.0, linestyle="--", label="Churned (MA7)", alpha=0.8)
```

We need a **second y-axis** because churned users are a different scale.

📌 Why a second axis?
If churn is much smaller than total users, keeping it on the same axis makes it “invisible”.
`twinx()` = share the x-axis but have separate y-values.

Dashed style (`linestyle="--"`) visually separates churn from growth.

---

## 4️⃣ Highlight the Campaign Window

```python
ax.axvspan(campaign_start, campaign_end, color="#f5c542", alpha=0.15, label="Campaign Window")
```

This draws a **transparent rectangle** behind the data to show the period of the marketing campaign.

* `axvspan()` = vertical shading between two dates
* `alpha=0.15` = light transparency to avoid distracting from the lines
* This gives **context** → “This spike happened *because* of this event”

---

## 5️⃣ Annotate the Spike (Max New Users)

```python
max_new_idx = df["new_users"].idxmax()
ax.scatter(df.loc[max_new_idx, "date"], df.loc[max_new_idx, "new_users_ma7"], s=60)
ax.annotate(
    f"Spike: {int(df.loc[max_new_idx, 'new_users'])} new",
    xy=(df.loc[max_new_idx, "date"], df.loc[max_new_idx, "new_users_ma7"]),
    xytext=(20, 25), textcoords="offset points",
    arrowprops=dict(arrowstyle="->", lw=1.5)
)
```

📌 What happens here?

1. We find the **index of the largest new_users value** (`idxmax()`).
2. We highlight that point with a **scatter dot**.
3. We add an **annotation text + arrow** to give meaning to the spike.

This transforms the chart from **visualization → storytelling**.

---

## 6️⃣ Annotate the Churn Peak

```python
max_churn_idx = df["churned_users"].idxmax()
ax2.scatter(df.loc[max_churn_idx, "date"], df.loc[max_churn_idx, "churned_ma7"], s=50)
ax2.annotate(
    f"Churn peak: {int(df.loc[max_churn_idx, 'churned_users'])}",
    xy=(df.loc[max_churn_idx, "date"], df.loc[max_churn_idx, "churned_ma7"]),
    xytext=(-60, -30), textcoords="offset points",
    arrowprops=dict(arrowstyle="->", lw=1.5)
)
```

This shows **negative signal** → when many users uninstalled or left.
It gives students insight:

> "Big campaigns often bring many new users, but also many leave → retention matters."

---

## 7️⃣ Titles, Labels & X-Axis Formatting

```python
ax.set_title("SaaS Growth Dashboard — New, Active & Churn (7-day MA)")
ax.set_xlabel("Date")
ax.set_ylabel("Users (New/Active)")
ax2.set_ylabel("Users (Churn)")
```

This sets:

* a clear title
* left axis label: New/Active users
* right axis label: Churned

Formatting the x-axis as dates:

```python
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
```

This:

* Shows **1 tick per week** (cleaner than all 100 dates)
* Formats as `Jan 15`, etc.
* Rotates labels to avoid overlap

---

## 8️⃣ Combined Legend

```python
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, loc="upper left", frameon=False)
```

Since we used **two axes**, each has its own legend.
We **combine** them into **one unified legend**, which is more professional.

---

## 9️⃣ Final Touch

```python
ax.grid(alpha=0.25)
plt.tight_layout()
plt.show()
```

* Soft grid improves readability
* `tight_layout()` fixes clipping
* `show()` renders the dashboard

---

# ✅ Summary

| What we did          | Why it matters                |
| -------------------- | ----------------------------- |
| Two axes             | Compare growth vs churn       |
| Shaded window        | Highlight campaign impact     |
| Moving averages      | Dashboard-level smooth trends |
| Annotations          | Data storytelling             |
| Legends & formatting | Professional visualization    |
