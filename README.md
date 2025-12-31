# Netflix_Project
Here’s a **clear, simple, and professional README** you can directly use for your project. You can copy-paste it into a `README.md` file.

---

# Netflix Data Analysis using Python

This project performs **exploratory data analysis (EDA)** on the Netflix dataset using **Pandas** and **Matplotlib**.
It visualizes trends related to Netflix movies and TV shows, including content type distribution, ratings, duration, release trends, and country-wise content.

---

## 📁 Dataset

* **File name:** `netflix_titles.csv`
* **Source:** Netflix Movies and TV Shows dataset
* **Used columns:**

  * `type`
  * `release_year`
  * `rating`
  * `country`
  * `duration`

---

## 🛠️ Technologies Used

* **Python**
* **Pandas** – Data cleaning and analysis
* **Matplotlib** – Data visualization

---

## ⚙️ Data Cleaning

Before analysis, the dataset is cleaned by:

* Removing rows with missing values in important columns:

  * `type`
  * `release_year`
  * `rating`
  * `country`
  * `duration`

This ensures accurate and meaningful visualizations.

---

## 📈 Visualizations Generated

### 1️⃣ Movies vs TV Shows (Bar Chart)

* Compares the total number of **Movies** and **TV Shows** available on Netflix.
* **Output file:** `Movies_vs_TvShows.png`

---

### 2️⃣ Content Ratings Distribution (Pie Chart)

* Shows the percentage distribution of Netflix content based on **ratings** (e.g., TV-MA, PG-13).
* **Output file:** `Content_Ratings_Pie.png`

---

### 3️⃣ Movie Duration Distribution (Histogram)

* Displays how movie durations are distributed (in minutes).
* Only includes **Movies**.
* **Output file:** `Movie-Duration-Histogram.png`

---

### 4️⃣ Release Year vs Number of Shows (Scatter Plot)

* Shows how Netflix content releases have changed over the years.
* **Output file:** `Release-Year-Scatter.png`

---

### 5️⃣ Top 10 Countries by Content (Horizontal Bar Chart)

* Displays the **top 10 countries** producing the most Netflix content.
* **Output file:** `Top-10-Countries.png`

---

### 6️⃣ Movies Released Per Year (Line Plot)

* Shows the trend of movie releases over time.

### 7️⃣ TV Shows Released Per Year (Line Plot)

* Shows the trend of TV show releases over time.

Both plots are displayed as **side-by-side subplots** for comparison.

* **Output file:** `Movies_TV-Shows_Comparison.png`

---

## ▶️ How to Run the Project

1. Make sure Python is installed
2. Install required libraries:

   ```bash
   pip install pandas matplotlib
   ```
3. Place `netflix_titles.csv` in the same directory as the script
4. Run the Python script:

   ```bash
   python your_script_name.py
   ```

---

## 📌 Output

* All visualizations are displayed on the screen
* Each plot is also saved as a `.png` file in the project directory

---

## 🎯 Purpose of the Project

* Practice **data analysis and visualization**
* Understand **Netflix content trends**
* Learn how to clean real-world datasets
* Build strong fundamentals in **Python EDA**


 ✨ Author

Umer Shaikh
