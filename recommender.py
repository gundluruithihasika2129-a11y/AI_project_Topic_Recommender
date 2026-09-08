import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from preprocessing import preprocess_text


# Load project dataset
DATA_PATH = "data/project_topics.csv"

projects = pd.read_csv(DATA_PATH)


# Create a combined text column
projects["combined_text"] = (
    projects["title"].fillna("") + " " +
    projects["domain"].fillna("") + " " +
    projects["skills"].fillna("") + " " +
    projects["description"].fillna("")
)


# Preprocess project text
projects["processed_text"] = projects["combined_text"].apply(
    preprocess_text
)


# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer()

project_vectors = vectorizer.fit_transform(
    projects["processed_text"]
)


def recommend_projects(student_profile, top_n=5):
    """
    Recommend projects based on the student's profile.
    """

    # Preprocess student profile
    processed_profile = preprocess_text(student_profile)

    # Convert student profile into TF-IDF vector
    student_vector = vectorizer.transform(
        [processed_profile]
    )

    # Calculate cosine similarity
    similarity_scores = cosine_similarity(
        student_vector,
        project_vectors
    ).flatten()

    # Add similarity scores to projects
    results = projects.copy()

    results["similarity_score"] = similarity_scores

    # Sort by highest similarity
    results = results.sort_values(
        by="similarity_score",
        ascending=False
    )

    # Return top recommendations
    return results.head(top_n)[
        [
            "project_id",
            "title",
            "domain",
            "skills",
            "difficulty",
            "description",
            "similarity_score"
        ]
    ]


# Test the recommendation system
if __name__ == "__main__":

    student_profile = """
    I am interested in Artificial Intelligence,
    Machine Learning and Natural Language Processing.
    I know Python, Pandas and Scikit-learn.
    My career goal is to become an AI Engineer.
    """

    recommendations = recommend_projects(
        student_profile,
        top_n=5
    )

    print("\nRecommended Projects:\n")

    for _, project in recommendations.iterrows():

        score = project["similarity_score"] * 100

        print(f"Project: {project['title']}")
        print(f"Domain: {project['domain']}")
        print(f"Difficulty: {project['difficulty']}")
        print(f"Match Score: {score:.2f}%")
        print(f"Description: {project['description']}")
        print("-" * 60)