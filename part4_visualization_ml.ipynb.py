import pandas as pd

# Load dataset
df = pd.read_csv("students.csv")

# 1. First 5 rows
print(df.head())

# 2. Shape and data types
print("Shape:", df.shape)
print("\nData Types:\n", df.dtypes)

# 3. Summary statistics
print("\nSummary Statistics:\n", df.describe())

# 4. Pass/Fail count
print("\nPass/Fail Count:\n", df['passed'].value_counts())

# 5. Average per subject
subject_cols = ['math', 'science', 'english', 'history', 'pe']

passed_avg = df[df['passed'] == 1][subject_cols].mean()
failed_avg = df[df['passed'] == 0][subject_cols].mean()

print("\nAverage (Passed Students):\n", passed_avg)
print("\nAverage (Failed Students):\n", failed_avg)

# 6. Top student
df['average'] = df[subject_cols].mean(axis=1)
top_student = df.loc[df['average'].idxmax()]

print("\nTop Student:\n", top_student)
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("students.csv")

# Columns
subject_cols = ['math', 'science', 'english', 'history', 'pe']

# Create average column
df['avg_score'] = df[subject_cols].mean(axis=1)

# ------------------ 1. BAR CHART ------------------
plt.figure()
avg_scores = df[subject_cols].mean()

plt.bar(subject_cols, avg_scores)
plt.title("Average Score per Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Score")

plt.savefig("plot1_bar.png")
plt.show()


# ------------------ 2. HISTOGRAM ------------------
plt.figure()

plt.hist(df['math'], bins=5)

mean_math = df['math'].mean()
plt.axvline(mean_math, linestyle='dashed', label=f"Mean = {mean_math:.2f}")

plt.title("Distribution of Math Scores")
plt.xlabel("Math Scores")
plt.ylabel("Frequency")
plt.legend()

plt.savefig("plot2_hist.png")
plt.show()


# ------------------ 3. SCATTER PLOT ------------------
plt.figure()

passed = df[df['passed'] == 1]
failed = df[df['passed'] == 0]

plt.scatter(passed['study_hours_per_day'], passed['avg_score'], label="Pass")
plt.scatter(failed['study_hours_per_day'], failed['avg_score'], label="Fail")

plt.title("Study Hours vs Average Score")
plt.xlabel("Study Hours per Day")
plt.ylabel("Average Score")
plt.legend()

plt.savefig("plot3_scatter.png")
plt.show()


# ------------------ 4. BOX PLOT ------------------
plt.figure()

pass_attendance = passed['attendance_pct'].tolist()
fail_attendance = failed['attendance_pct'].tolist()

plt.boxplot([pass_attendance, fail_attendance], labels=['Pass', 'Fail'])

plt.title("Attendance Distribution (Pass vs Fail)")
plt.ylabel("Attendance %")

plt.savefig("plot4_box.png")
plt.show()


# ------------------ 5. LINE PLOT ------------------
plt.figure()

plt.plot(df['name'], df['math'], marker='o', label="Math")
plt.plot(df['name'], df['science'], marker='s', label="Science")

plt.title("Math vs Science Scores")
plt.xlabel("Student Name")
plt.ylabel("Score")
plt.xticks(rotation=45)
plt.legend()

plt.savefig("plot5_line.png")
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("students.csv")

# Create avg_score (if not already created)
subject_cols = ['math', 'science', 'english', 'history', 'pe']
df['avg_score'] = df[subject_cols].mean(axis=1)

# ------------------ 1. BAR PLOTS (Math & Science) ------------------
plt.figure(figsize=(10,5))

# Subplot 1 (Math)
ax1 = plt.subplot(1, 2, 1)
sns.barplot(data=df, x='passed', y='math', ax=ax1)
ax1.set_title("Average Math Score (Pass vs Fail)")
ax1.set_xlabel("Passed (0=Fail, 1=Pass)")
ax1.set_ylabel("Math Score")

# Subplot 2 (Science)
ax2 = plt.subplot(1, 2, 2)
sns.barplot(data=df, x='passed', y='science', ax=ax2)
ax2.set_title("Average Science Score (Pass vs Fail)")
ax2.set_xlabel("Passed (0=Fail, 1=Pass)")
ax2.set_ylabel("Science Score")

plt.tight_layout()
plt.savefig("plot6_seaborn_bar.png")
plt.show()


# ------------------ 2. SCATTER + REGRESSION ------------------
plt.figure()

# Scatter plot
sns.scatterplot(data=df, x='attendance_pct', y='avg_score', hue='passed')

# Regression lines
sns.regplot(data=df[df['passed'] == 1], x='attendance_pct', y='avg_score', label='Pass')
sns.regplot(data=df[df['passed'] == 0], x='attendance_pct', y='avg_score', label='Fail')

plt.title("Attendance vs Average Score (with Regression)")
plt.xlabel("Attendance %")
plt.ylabel("Average Score")
plt.legend()

plt.savefig("plot7_seaborn_scatter.png")
plt.show()


# ------------------ 3. COMMENT  ------------------

# Seaborn is easier to use for statistical plots like bar charts and scatter plots
# because it automatically calculates averages and adds better styling.
# Compared to Matplotlib, Seaborn requires less code and gives more visually
# appealing graphs, while Matplotlib needs more manual customization.
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# ------------------ LOAD DATA ------------------
df = pd.read_csv("students.csv")

# ------------------ STEP 1: PREPARE DATA ------------------
feature_cols = ['math', 'science', 'english', 'history', 'pe',
                'attendance_pct', 'study_hours_per_day']

X = df[feature_cols]   # features
y = df['passed']       # target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ------------------ STEP 2: TRAIN MODEL ------------------
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# Training accuracy
train_pred = model.predict(X_train_scaled)
train_acc = accuracy_score(y_train, train_pred)
print("Training Accuracy:", train_acc)

# ------------------ STEP 3: EVALUATE ------------------
y_pred = model.predict(X_test_scaled)
test_acc = accuracy_score(y_test, y_pred)

print("\nTest Accuracy:", test_acc)

# Print each student result
print("\nTest Predictions:")
names = df.loc[X_test.index, 'name']

for name, actual, pred in zip(names, y_test, y_pred):
    result = "✅ Correct" if actual == pred else "❌ Wrong"
    print(f"{name} | Actual: {actual} | Predicted: {pred} | {result}")

# ------------------ STEP 4: FEATURE IMPORTANCE ------------------
coefficients = model.coef_[0]

# Pair feature names with coefficients
feature_importance = list(zip(feature_cols, coefficients))

# Sort by absolute value (largest first)
feature_importance.sort(key=lambda x: abs(x[1]), reverse=True)

print("\nFeature Importance (sorted):")
for feature, coef in feature_importance:
    print(f"{feature}: {coef:.4f}")

# Plot
features = [f[0] for f in feature_importance]
values = [f[1] for f in feature_importance]

colors = ['green' if v > 0 else 'red' for v in values]

plt.figure()
plt.barh(features, values, color=colors)
plt.title("Feature Importance (Logistic Regression)")
plt.xlabel("Coefficient Value")
plt.ylabel("Features")

plt.savefig("plot8_feature_importance.png")
plt.show()

# ------------------ STEP 5: NEW STUDENT (BONUS) ------------------
new_student = [[75, 70, 68, 65, 80, 82, 3.2]]

# Scale
new_student_scaled = scaler.transform(new_student)

# Predict
prediction = model.predict(new_student_scaled)[0]
probability = model.predict_proba(new_student_scaled)[0]

result = "Pass" if prediction == 1 else "Fail"

print("\nNew Student Prediction:", result)
print("Probability [Fail, Pass]:", probability)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Load data
df = pd.read_csv("students.csv")

print("Columns:", df.columns)  # DEBUG

# Required columns
feature_cols = ['math', 'science', 'english', 'history', 'pe',
                'attendance_pct', 'study_hours_per_day']

# Check if columns exist
for col in feature_cols + ['passed']:
    if col not in df.columns:
        print(f"❌ Missing column: {col}")

# Features and target
X = df[feature_cols]
y = df['passed']

# Convert to numeric (fix hidden errors)
X = X.apply(pd.to_numeric, errors='coerce')
y = pd.to_numeric(y, errors='coerce')

# Drop rows with missing values
X = X.dropna()
y = y.loc[X.index]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

print("✅ Model trained successfully!")