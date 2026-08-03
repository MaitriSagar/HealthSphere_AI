# HealthSphere AI

This is a web application I built that uses Machine Learning to help predict the risk of three major health conditions: Diabetes, Heart Disease, and Chronic Kidney Disease (CKD). I built the entire pipeline from scratch—from cleaning the raw datasets and training the models in Jupyter Notebooks, to building the Python Flask backend and designing the frontend UI.

## What's under the hood?

I used **Random Forest Classifiers** for all three predictive models. 

One of the biggest challenges I ran into during development was **Data Leakage**. When I first trained my Heart and CKD models, they were getting near 100% accuracy. I realized the AI was basically "cheating" by memorizing the Patient ID numbers rather than actually learning the medical symptoms! 

To fix this and make the application user-friendly:
1. I removed the ID and dataset columns so the AI was blind to everything except real biology.
2. I used Random Forest **Feature Importance** to figure out which symptoms actually mattered the most mathematically.
3. I reduced the Heart and CKD questionnaires from 20+ overwhelming questions down to just the **top 6 most critical biological markers**. 

## Tech Stack I Used

* **Data Science & ML:** Python, Pandas, Scikit-Learn (Models saved as `.pkl` files)
* **Backend:** Flask (Python web framework)
* **Frontend:** HTML5, Tailwind CSS (for modern UI styling), Bootstrap Icons
* **Version Control:** Git & GitHub

## How to Run This Project on Your Machine

If you are evaluating this project, here is how you can get it running locally on your computer in just a few minutes:

**1. Clone this repository**
```bash
git clone [https://github.com/YOUR_USERNAME/HealthSphere_AI.git](https://github.com/YOUR_USERNAME/HealthSphere_AI.git)
cd HealthSphere_AI