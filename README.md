# 🛍️ Project 3 – Customer Segmentation using K-Means Clustering

## 📌 Project Overview

This project focuses on **Customer Segmentation** using Unsupervised Machine Learning. The objective is to group customers with similar characteristics based on their **Annual Income** and **Spending Score**.

The project uses the **K-Means Clustering algorithm** to identify different customer segments and provides marketing insights for each segment.

---

## 🎯 Objectives

* Load and clean the customer dataset.
* Perform exploratory data analysis.
* Select relevant features for clustering.
* Scale numerical features using `StandardScaler`.
* Use the **Elbow Method** to determine the suitable number of clusters.
* Apply **K-Means Clustering**.
* Visualize customer clusters.
* Profile each customer segment.
* Suggest suitable marketing strategies.
* Save clustered customer data.
* Generate a segment-wise report.

---

## 📊 Dataset

The project uses the **Mall Customers dataset**.

### Features

| Feature                | Description                           |
| ---------------------- | ------------------------------------- |
| CustomerID             | Unique customer identification number |
| Gender                 | Customer gender                       |
| Age                    | Customer age                          |
| Annual Income (k$)     | Annual income in thousands of dollars |
| Spending Score (1-100) | Customer spending behavior score      |

The main features used for clustering are:

* `Annual Income (k$)`
* `Spending Score (1-100)`

---

## 🤖 Machine Learning Algorithm

### K-Means Clustering

K-Means is an **Unsupervised Machine Learning** algorithm that divides data points into a predefined number of clusters.

Each customer is assigned to the cluster whose centroid is closest to that customer.

### Why K-Means?

K-Means is suitable for this project because the goal is to discover customer groups without having predefined labels.

---

## 📉 Elbow Method

The **Elbow Method** is used to determine a suitable value of `K`.

The algorithm is tested with different numbers of clusters and the corresponding inertia values are calculated.

The point where the decrease in inertia starts becoming slower is considered the **elbow point**.

In this project, `K = 5` is used for the final K-Means model.

---

## ⚙️ Project Workflow

```text
Dataset
   ↓
Data Loading
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Feature Selection
   ↓
Feature Scaling
   ↓
Elbow Method
   ↓
K-Means Clustering
   ↓
Cluster Visualization
   ↓
Cluster Profiling
   ↓
Marketing Insights
   ↓
Save Results
```

---

## 📈 Data Visualization

The project generates visualizations for:

1. Customer Age Distribution
2. Annual Income Distribution
3. Spending Score Distribution
4. Elbow Method
5. Customer Clusters

The final cluster visualization shows the relationship between **Annual Income** and **Spending Score**.

---

## 👥 Customer Segments

The project profiles customers based on their average age, income, and spending score.

### 💎 Premium Customers

Customers with relatively high income and high spending behavior.

**Marketing Strategy:**

* Premium products
* Loyalty rewards
* Exclusive offers
* VIP memberships
* Personalized recommendations

### 💰 Careful Customers

Customers with relatively high income but lower spending behavior.

**Marketing Strategy:**

* Discounts
* Value packages
* Personalized promotions
* Limited-time offers

### 🚀 Potential Customers

Customers with lower income but relatively high spending behavior.

**Marketing Strategy:**

* Loyalty programs
* Targeted promotions
* Reward points
* Personalized recommendations

### 📉 Low Value Customers

Customers with relatively lower income and lower spending behavior.

**Marketing Strategy:**

* Budget-friendly offers
* Basic product promotions
* Customer retention campaigns

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Seaborn**
* **Scikit-learn**
* **K-Means Clustering**
* **StandardScaler**

---

## 📁 Project Structure

```text
Customer-Segmentation-KMeans/
│
├── customer_segmentation.py
├── Mall_Customers.csv
├── requirements.txt
├── clustered_customers.csv
├── segment_report.txt
└── README.md
```

---

## 💻 Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

Move into the project folder:

```bash
cd Customer-Segmentation-KMeans
```

Install the required libraries:

```bash
python -m pip install -r requirements.txt
```

---

## ▶️ How to Run

Run the Python program:

```bash
python customer_segmentation.py
```

The program will:

* Load the dataset
* Clean the data
* Perform analysis
* Generate visualizations
* Apply K-Means clustering
* Profile customer segments
* Save the clustered dataset
* Generate the segment report

---

## 📄 Output Files

### `clustered_customers.csv`

Contains the original customer information along with:

* Cluster number
* Customer segment

### `segment_report.txt`

Contains a short report for each customer segment including:

* Number of customers
* Average age
* Average income
* Average spending score
* Suggested marketing action

---

## 📌 Key Learning Outcomes

Through this project, I learned:

* Data preprocessing
* Exploratory Data Analysis
* Feature scaling
* Unsupervised Machine Learning
* K-Means Clustering
* Elbow Method
* Data visualization
* Customer profiling
* Business-oriented interpretation of ML results

---

## 🚀 Future Improvements

Future versions of this project can include:

* Interactive dashboards using Power BI or Streamlit
* Automatic optimal K selection
* More customer attributes
* Real-time customer segmentation
* Advanced clustering algorithms
* Personalized recommendation systems

---

## 👨‍💻 Internship Project

**Internship Project – Project 3**

**Project:** Customer Segmentation using K-Means Clustering

**Domain:** Machine Learning / Data Science

---

## ⭐ Conclusion

This project demonstrates how **K-Means Clustering** can be used to segment customers based on their income and spending behavior.

The identified customer segments can help businesses develop **targeted marketing strategies, personalized offers, and better customer engagement**.
