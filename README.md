# 🤖 AI Project Topic Recommender

An NLP-based recommendation system that suggests relevant project topics to students based on their interests, skills, academic background, and career goals.

## 📌 Project Overview

The AI Project Topic Recommender uses Natural Language Processing and Content-Based Filtering to recommend suitable project topics.

The system uses:

- TF-IDF Vectorization
- Cosine Similarity
- NLP Text Preprocessing
- Content-Based Recommendation
- Flask Web Interface

## 🎯 Objectives

- Understand NLP text preprocessing
- Learn TF-IDF vectorization
- Implement cosine similarity
- Build a content-based recommendation system
- Generate personalized project recommendations
- Create a simple web interface using Flask

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- NLTK
- Scikit-learn
- Flask
- HTML
- CSS

## 📂 Project Structure

AI_Project_Topic_Recommender/

├── data/

│   └── project_topics.csv

├── app.py

├── recommender.py

├── preprocessing.py

├── requirements.txt

└── README.md

## ⚙️ How It Works

1. Student enters interests.
2. Student enters technical skills.
3. Student provides academic background.
4. Student enters career goal.
5. NLP preprocessing cleans the text.
6. TF-IDF converts text into numerical vectors.
7. Cosine Similarity compares the student profile with project topics.
8. Projects are ranked according to similarity.
9. Top 5 project recommendations are displayed.

## 🧠 Recommendation Method

The project uses Content-Based Filtering.

TF-IDF is used to represent project and student text as numerical vectors.

Cosine Similarity is then used to calculate the similarity between the student profile and project topics.

A higher similarity score indicates a stronger match.

## ✨ Features

- Student Interest Profile
- Project Topic Database
- NLP Preprocessing
- TF-IDF Vectorization
- Cosine Similarity
- Personalized Recommendations
- Top-N Recommendations
- Flask Web Interface

## 🚀 How to Run

### 1. Clone the repository

git clone YOUR_GITHUB_REPOSITORY_URL

### 2. Open the project folder

cd AI_Project_Topic_Recommender

### 3. Install dependencies

pip install -r requirements.txt

### 4. Run the application

python app.py

### 5. Open in browser

http://127.0.0.1:5000

## 📊 Example Input

Interests:

Artificial Intelligence, Machine Learning, NLP

Skills:

Python, Pandas, Scikit-learn, TF-IDF

Academic Background:

Data Science student

Career Goal:

AI Engineer

## 🎯 Output

The system generates the Top 5 project recommendations with:

- Project title
- Domain
- Required skills
- Difficulty level
- Project description
- Match score

## 🔮 Future Improvements

- Difficulty-level filtering
- Topic clustering
- Trend analysis
- User feedback integration
- Topic visualization
- BERT/Transformer-based recommendations
- Advanced recommendation algorithms

## 👩‍💻 Author

Gundluru Ithihasika

Data Science Student

## 📜 Internship Task

Task ID: AI-SS-003

Task Name: AI Project Topic Recommender

Domain: Student Support & Internship Management NLP