# ============================================
# Customer Segmentation using K-Means
# ============================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


# ============================================
# 1. LOAD DATASET
# ============================================

print("Loading dataset...")

df = pd.read_csv("Mall_Customers.csv")

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)


# ============================================
# 2. DATA CLEANING
# ============================================

print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

print("\nShape after removing duplicates:")
print(df.shape)


# ============================================
# 3. BASIC DATA INFORMATION
# ============================================

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())


# ============================================
# 4. EXPLORATORY DATA ANALYSIS
# ============================================

# Age Distribution
plt.figure(figsize=(8, 5))

sns.histplot(
    df["Age"],
    bins=20,
    kde=True
)

plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.show()


# Annual Income Distribution
plt.figure(figsize=(8, 5))

sns.histplot(
    df["Annual Income (k$)"],
    bins=20,
    kde=True
)

plt.title("Annual Income Distribution")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.show()


# Spending Score Distribution
plt.figure(figsize=(8, 5))

sns.histplot(
    df["Spending Score (1-100)"],
    bins=20,
    kde=True
)

plt.title("Spending Score Distribution")
plt.xlabel("Spending Score")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.show()


# ============================================
# 5. SELECT FEATURES
# ============================================

# We use Annual Income and Spending Score
# because they are useful for customer segmentation.

X = df[
    [
        "Annual Income (k$)",
        "Spending Score (1-100)"
    ]
]


# ============================================
# 6. FEATURE SCALING
# ============================================

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

print("\nScaled Features:")
print(X_scaled[:5])


# ============================================
# 7. ELBOW METHOD
# ============================================

inertia = []

for k in range(1, 11):

    kmeans = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    kmeans.fit(X_scaled)

    inertia.append(kmeans.inertia_)


# Plot Elbow Curve

plt.figure(figsize=(8, 5))

plt.plot(
    range(1, 11),
    inertia,
    marker="o"
)

plt.title("Elbow Method for Optimal K")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")

plt.xticks(range(1, 11))

plt.grid(True)

plt.tight_layout()

plt.show()


# ============================================
# 8. APPLY K-MEANS
# ============================================

# For Mall Customers, K=5 is commonly used
# because the elbow generally appears around 5.

optimal_k = 5

kmeans = KMeans(
    n_clusters=optimal_k,
    random_state=42,
    n_init=10
)

clusters = kmeans.fit_predict(X_scaled)


# ============================================
# 9. ADD CLUSTER LABELS
# ============================================

df["Cluster"] = clusters

print("\nClustered Dataset:")
print(df.head())


# ============================================
# 10. CLUSTER VISUALIZATION
# ============================================

plt.figure(figsize=(10, 7))

sns.scatterplot(
    data=df,
    x="Annual Income (k$)",
    y="Spending Score (1-100)",
    hue="Cluster",
    palette="viridis",
    s=100
)

# Convert cluster centers back to original scale

centers = scaler.inverse_transform(
    kmeans.cluster_centers_
)

plt.scatter(
    centers[:, 0],
    centers[:, 1],
    s=250,
    c="red",
    marker="X",
    label="Centroids"
)

plt.title("Customer Segmentation using K-Means")

plt.xlabel("Annual Income (k$)")

plt.ylabel("Spending Score (1-100)")

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.show()


# ============================================
# 11. CLUSTER PROFILING
# ============================================

cluster_profile = df.groupby("Cluster").agg(
    Customers=("CustomerID", "count"),
    Average_Age=("Age", "mean"),
    Average_Income=("Annual Income (k$)", "mean"),
    Average_Spending_Score=("Spending Score (1-100)", "mean")
).round(2)

print("\n===================================")
print("CLUSTER PROFILE")
print("===================================")

print(cluster_profile)


# ============================================
# 12. AUTOMATIC SEGMENT NAMES
# ============================================

segment_names = {}

for cluster in cluster_profile.index:

    income = cluster_profile.loc[
        cluster,
        "Average_Income"
    ]

    spending = cluster_profile.loc[
        cluster,
        "Average_Spending_Score"
    ]

    if income >= 60 and spending >= 60:

        segment_names[cluster] = "Premium Customers"

    elif income >= 60 and spending < 60:

        segment_names[cluster] = "Careful Customers"

    elif income < 60 and spending >= 60:

        segment_names[cluster] = "Potential Customers"

    else:

        segment_names[cluster] = "Low Value Customers"


df["Segment"] = df["Cluster"].map(segment_names)


# ============================================
# 13. DISPLAY FINAL PROFILE
# ============================================

final_profile = df.groupby("Segment").agg(
    Customers=("CustomerID", "count"),
    Average_Age=("Age", "mean"),
    Average_Income=("Annual Income (k$)", "mean"),
    Average_Spending_Score=("Spending Score (1-100)", "mean")
).round(2)


print("\n===================================")
print("FINAL CUSTOMER SEGMENTS")
print("===================================")

print(final_profile)


# ============================================
# 14. SAVE CLUSTERED DATA
# ============================================

df.to_csv(
    "clustered_customers.csv",
    index=False
)

print(
    "\nClustered customer data saved as "
    "clustered_customers.csv"
)


# ============================================
# 15. CREATE SEGMENT REPORT
# ============================================

with open(
    "segment_report.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write("CUSTOMER SEGMENTATION REPORT\n")
    file.write("=" * 40 + "\n\n")

    for segment in final_profile.index:

        row = final_profile.loc[segment]

        file.write(
            f"Segment: {segment}\n"
        )

        file.write(
            f"Number of Customers: "
            f"{int(row['Customers'])}\n"
        )

        file.write(
            f"Average Age: "
            f"{row['Average_Age']}\n"
        )

        file.write(
            f"Average Income: "
            f"{row['Average_Income']} k$\n"
        )

        file.write(
            f"Average Spending Score: "
            f"{row['Average_Spending_Score']}\n"
        )

        file.write("\nMarketing Action:\n")

        if segment == "Premium Customers":

            file.write(
                "Offer premium products, loyalty rewards, "
                "exclusive memberships and personalized offers.\n"
            )

        elif segment == "Careful Customers":

            file.write(
                "Use discounts, value deals and budget-friendly "
                "offers to increase spending.\n"
            )

        elif segment == "Potential Customers":

            file.write(
                "Use targeted promotions, recommendations and "
                "loyalty programs to increase customer value.\n"
            )

        else:

            file.write(
                "Use low-cost promotions and basic offers while "
                "focusing on customer retention.\n"
            )

        file.write("\n" + "-" * 40 + "\n\n")


print(
    "Segment report saved as segment_report.txt"
)

print("\nPROJECT COMPLETED SUCCESSFULLY!")