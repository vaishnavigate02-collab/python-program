import matplotlib.pyplot as plt

# 1 . Simple datasets
days = ["Mon", "Tue", "Wed", "Thur", "Fri"]
hours_studies = [1, 2, 3, 5, 7]

students = ["Alice", "Bob", "Charlie", "David"]
books_read = [4, 7, 2, 3]

test_scores = [55, 62, 65, 70, 72, 75, 78, 85, 88, 95]


fig, axes = plt.subplots(figsize=(12, 4), nrows=1, ncols=3)

fig.suptitle("Student Data Visualization", fontsize=14, fontweight="bold")

# Plot 1: Line Plot
axes[0].plot(days, hours_studies, marker="o", color="blue", linewidth=2)
axes[0].set_title("Line Plot : Study Hours ")
axes[0].set_xlabel("Days of week")
axes[0].set_ylabel("Hours studied")
axes[0].grid(True)

# Plot 2: Bar Chart
axes[1].bar(students, books_read, color=["pink", "skyblue", "lightgreen", "orange"])
axes[1].set_title("Bar Chart : Books Read")
axes[1].set_xlabel("Students")
axes[1].set_ylabel("Number of Books")

# Plot 3: Histogram
axes[2].hist(test_scores, bins=[50, 60, 70, 80, 90, 100], color="purple", edgecolor="black")
axes[2].set_title("Histogram : Score Distribution")
axes[2].set_xlabel("Score Ranges")
axes[2].set_ylabel("Number of Students")

plt.tight_layout()
plt.show()
