# 🚢 Titanic Survival Prediction

A Machine Learning–based web application that predicts whether a passenger would have survived the Titanic disaster based on historical passenger data.

This project demonstrates the complete end-to-end Machine Learning workflow, including data preprocessing, model training, and deployment using a simple web interface.

---

## 📌 Project Overview

The Titanic disaster is a classic classification problem in Machine Learning.  
Using passenger details such as age, gender, class, family information, fare, and port of embarkation, this application predicts the **likelihood of survival**.

The trained model is deployed using **Streamlit**, allowing users to interactively input passenger details and get real-time predictions.

---

## 🚀 Features

- Predicts passenger survival (Survived / Not Survived)
- Interactive web interface built with Streamlit
- Uses real-world historical Titanic dataset
- Clear and user-friendly input fields
- Beginner-friendly ML project with deployment

---

## 📊 Input Parameters

The prediction is based on the following passenger details:

- Passenger Class (1st, 2nd, 3rd)
- Gender
- Age
- Number of Siblings/Spouses aboard
- Number of Parents/Children aboard
- Ticket Fare
- Port of Embarkation (Cherbourg, Queenstown, Southampton)

---

## 🧠 Tech Stack

- Python  
- Scikit-learn  
- Pandas & NumPy  
- Streamlit  

---

## 📂 Project Structure

- `app.py` – Streamlit web application  
- `titanic_model.pkl` – Trained Machine Learning model  
- `Titanic.ipynb` – Model training and analysis notebook  
- `Titanic-Dataset.csv` – Dataset used for training  
- `requirements.txt` – Project dependencies  
- `README.md` – Project documentation  

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally:

1. Clone the repository  
2. Create and activate a virtual environment (optional)  
3. Install the required dependencies  
4. Run the Streamlit application  

---

## 📌 Dependencies

Make sure `requirements.txt` contains:

- streamlit  
- numpy  
- pandas  
- scikit-learn  

---

## 🖥️ How the Application Works

- User enters passenger details through the UI
- Input values are processed and encoded
- The trained ML classification model predicts survival
- Result is displayed instantly as **Survived** or **Not Survived**

---

## 🎯 Sample Output

- **The passenger is predicted to have survived.**  
OR  
- **The passenger is predicted to have not survived.**

---

## 📈 Future Improvements

- Add probability-based prediction output
- Compare multiple classification models
- Improve UI with visual explanations
- Deploy on cloud with enhanced performance

---

## 👨‍💻 Author

**Vedant Patke**  
Second-Year CSE (AI) Student  
