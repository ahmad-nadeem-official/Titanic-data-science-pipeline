[![Google-colab](https://img.shields.io/badge/-0.13.2-e09419?logo=Google-colab&logoColor=white)](https://colab.research.google.com/drive/1KZCEK9QvUOiA0k7trgc_SGiS8KX-k5Vs#scrollTo=NtHnOfp2Bbr6)

Titanic Data Science Pipeline – Automated, Reusable, Production-Ready
=====================================================================

🧠 Project Motivation & Vision
------------------------------

This project was developed by me under the sharp-eyed supervision of ChatGPT — who, acting like a boss, assigned me this task after I asked for a way to work more professionally with the Titanic dataset. At the time of building this, I wasn’t working in a professional setting, but I wanted to break out of the typical beginner loop. ChatGPT challenged me to create a **reusable, automated EDA pipeline** that could be applied to any structured dataset — and this project is the outcome: Version 1 of a clean, scalable, and modular data science workflow. This is just the beginning — in future updates, I plan to make the pipeline more powerful, package it for PyPI, and build a full data visualization interface using React.js or Streamlit. So stay connected — more is coming!

📌 Overview
-----------

Welcome to a **professionally structured, highly reusable, and fully automated data science pipeline**, built around the classic Titanic dataset — but architected to work with _any structured dataset_ with minimal changes.

The core goal? Eliminate repetitive grunt work, automate everything from exploratory data analysis to model evaluation, and make the codebase modular, readable, and robust enough for real-world usage.

Whether you're working on a Kaggle project, a company dataset, or just exploring classification problems — this pipeline is your solid, reusable foundation.

* * *

🎯 What This Project Does
-------------------------

*   Takes raw, messy data and transforms it into a clean dataset ready for modeling
    
*   Automatically performs exploratory data analysis (EDA), null checks, distributions, correlations, etc.

*   visualize data automatically, just asks your presfrence that which graph you want for which column.
    
*   Uses a **custom-built Python EDA class** to keep things reusable across datasets
    
*   Trains classification models (Logistic Regression, Random Forest)
    
*   Evaluates them with metrics like accuracy, F1 score, precision, and recall
    
*   Saves cleaned datasets and trained models for future use
    

All this is done in **a professional folder structure**, using clean Python modules, not messy notebooks.

* * *

💡 Why This Project Matters
---------------------------

Most beginner data science projects stop at the notebook level. This one goes beyond:

*   Shows you understand **project architecture**
    
*   Demonstrates **automation of analysis tasks**
    
*   Highlights your ability to write **production-style code**, not just data exploration
    
*   Proves it care about **scalability, reusability, and best practices**
    
*   Makes it stand out to recruiters and senior devs who read between the lines
    
* * *

🧱 Project Structure
--------------------

*   **data/**
    
    *   `raw/`: Contains the original Titanic dataset (CSV)
        
    *   `processed/`: Stores the cleaned version used in modeling
        
*   **models/**  
    Trained models serialized after evaluation (Logistic, Random Forest, etc.)
    
*   **notebooks/**  
    Interactive experiments: `01_eda.ipynb` (for EDA), `modeling.ipynb` (for training)
    
*   **reports/**  
    Can be used for saved charts, auto-generated visuals, or metrics summaries
    
*   **Spare py files/**  
    Scratchpad versions of the core pipeline for experimentation or backup
    
*   **src/**
    
    *   `main_eda_class.py`: The EDA class that does all the heavy lifting — histogram, nulls, boxplots, correlation, and more
        
    *   `model_training.py`: Clean training loop with evaluation and model saving
        
    *   `utils.py`: Helper functions to reduce code duplication and keep things DRY
        
*   **requirements.txt, README.md, LICENSE** — for dependency management and documentation
    

* * *

⚙️ Features
-----------

*   📊 **Automated EDA**  
    Just call a class — and get stats, visuals, missing value report, and correlation matrix. Saves hours.
    
*   🧼 **Cleaned Dataset Pipeline**  
    Replaces manual cleaning with repeatable code — always get the same results.
    
*   🤖 **Model Training & Saving**  
    One script to train models, print metrics, and save `.pkl` files.
    
*   📈 **Evaluation Metrics**  
    Includes accuracy, precision, recall, F1-score, and confusion matrix.
    
*   💾 **Ready for Other Datasets**  
    Just change the file path and class columns — the pipeline still works.
    

* * *

🛠️ Tech Stack
--------------

*   ![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white) 
    
*   ![Pandas](https://img.shields.io/badge/Pandas-2.1.4-150458?logo=pandas&logoColor=white) 

*   ![Matplotlib](https://img.shields.io/badge/Matplotlib-3.8.4-11557C?logo=matplotlib&logoColor=white) 

*   ![Seaborn](https://img.shields.io/badge/Seaborn-0.13.2-42A5F5?logo=seaborn&logoColor=white) 
    
*   ![scikit-learn](https://img.shields.io/badge/scikit--learn-1.4-F7931E?logo=scikit-learn&logoColor=white) (for models and metrics)
    
*   ![joblib](https://img.shields.io/badge/joblib-0.13.2-42A5F5?logo=joblib&logoColor=white) 
    
    
*   Follows best practices: OOP, modular code, clear naming, and reusable classes
    

* * *

📌 How to Use
-------------

1.  Install dependencies: `pip install -r requirements.txt`
    
2.  Start exploring data with: `notebooks/01_eda.ipynb`
    
3.  Train models using: `notebooks/modeling.ipynb`  
    or just run `model_training.py` inside `/src` if you prefer scripts.
    
4.  Swap in your own dataset under `data/raw/`, update the class target column, and you're good to go.
    

* * *

🔍 Example Use Cases
--------------------

*   College projects that look production-ready
    
*   Industry-ready prototype pipelines
    
*   Quick testing on new classification datasets
    
*   Templates for Kaggle competitions
    
*   HR-stunning portfolio repo 😎
    

* * *

🙋‍♂️ Thanks for your time
---------------------

Created by **Muhammad Ahmad Nadeem** — a passionate data scientist and AI/ML engineer in the making.  
I believe that **clarity, simplicity, and automation** are what separate hobby projects from real engineering.  
This project is a reflection of that mindset — and just the beginning.