# laptop-price-prediction

Of course. Here is a comprehensive summary for your Laptop Price Prediction model, formatted perfectly for a GitHub README file.

I've created a `README.md` file that explains the project's purpose, structure, and how to run it.

```markdown:github README:README.md
# Laptop Price Predictor

This project aims to predict the price of laptops based on their specifications. It uses a machine learning model trained on a dataset of over a thousand laptops from various brands. The model is deployed as an interactive web application using Streamlit, allowing users to get price estimates by selecting different hardware and software configurations.

![Screenshot of the Laptop Price Predictor web application](https://i.imgur.com/K3aY2aW.png)

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [How to Run](#how-to-run)
- [Model Development](#model-development)

---

## Overview

The project follows a complete end-to-end machine learning workflow:
1.  **Data Cleaning & Feature Engineering**: The initial dataset (`laptop_data.csv`) is cleaned, and new, more informative features are engineered (e.g., calculating Pixels Per Inch (PPI), extracting CPU/GPU brands).
2.  **Model Training**: A machine learning pipeline is constructed using Scikit-learn. This pipeline handles preprocessing (like one-hot encoding for categorical variables) and trains a regression model to predict the price. The model achieves an **R² score of ~0.81**, indicating a good fit to the data.
3.  **Deployment**: The trained pipeline is saved and integrated into a Streamlit application (`app2.py`), providing a user-friendly interface for making predictions.

---

## Features

-   **Wide Range of Inputs**: Predict prices based on Brand, Type, RAM, Weight, CPU, GPU, Storage (HDD/SSD), and more.
-   **Interactive Web UI**: A simple and intuitive web application for users to input features and get instant price predictions.
-   **Reproducible Workflow**: The entire data processing and model training logic is contained within the `pred.ipynb` Jupyter Notebook.
-   **Efficient Pipeline**: Uses a Scikit-learn pipeline (`pipe.pkl`) to streamline preprocessing and prediction steps.

---

## Tech Stack

-   **Programming Language**: Python
-   **Libraries**:
    -   Pandas & NumPy for data manipulation
    -   Scikit-learn for model building and training
    -   Streamlit for web application deployment
    -   Jupyter Notebook for model development

---

## Project Structure

```

├── app2.py                 \# The Streamlit web application script
├── pred.ipynb              \# Jupyter Notebook with the full data analysis and model training process
├── pipe.pkl                \# The saved Scikit-learn pipeline (preprocessing + model)
├── df.pkl                  \# The cleaned and processed pandas DataFrame
├── laptop\_data.csv         \# The original, raw dataset of laptop specifications
└── README.md               \# This README file

````

---

## How to Run

To get this project running on your local machine, follow these steps:

**1. Clone the repository:**
```bash
git clone [https://github.com/your-username/laptop-price-predictor.git](https://github.com/your-username/laptop-price-predictor.git)
cd laptop-price-predictor
````

**2. Create and activate a virtual environment (recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**3. Install the required dependencies:**
Create a `requirements.txt` file with the following content:

```
pandas
numpy
scikit-learn
streamlit
```

Then, run this command to install them:

```bash
pip install -r requirements.txt
```

**4. Run the Streamlit application:**

```bash
streamlit run app2.py
```

Your web browser should open with the application running, typically at `http://localhost:8501`.

-----

## Model Development

The model was developed inside the `pred.ipynb` notebook. The key steps included:

1.  **Data Cleaning**:
      - Converted `Ram` and `Weight` columns to numerical types.
      - Handled data inconsistencies and formatted columns for processing.
2.  **Feature Engineering**:
      - Created a `Touchscreen` feature (binary 0 or 1).
      - Created an `IPS` display feature (binary 0 or 1).
      - Calculated `PPI` (Pixels Per Inch) from the `ScreenResolution` and `Inches` columns.
      - Extracted high-level brands from `Cpu` and `Gpu` columns (e.g., 'Intel', 'AMD', 'Nvidia').
      - Separated `Memory` into distinct `HDD` and `SSD` columns.
3.  **Modeling**:
      - A `ColumnTransformer` was used within a Scikit-learn `Pipeline` to apply one-hot encoding to categorical features (`Company`, `TypeName`, `CpuBrand`, etc.) while leaving numerical features untouched.
      - A regression model (e.g., `RandomForestRegressor`, `XGBRegressor`) was chosen as the final step in the pipeline.
      - The model was trained and evaluated, achieving a final **R² score of 0.81** on the test set.

