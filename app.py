from flask import Flask, request, render_template_string

from recommender import recommend_projects


app = Flask(__name__)


HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

    <title>AI Project Topic Recommender</title>

    <style>

        body {
            font-family: Arial, sans-serif;
            background: #f4f7fb;
            margin: 0;
            padding: 0;
        }

        .container {
            width: 90%;
            max-width: 1000px;
            margin: 40px auto;
        }

        .header {
            background: #1f4e79;
            color: white;
            padding: 30px;
            border-radius: 12px;
            text-align: center;
        }

        .form-box {
            background: white;
            padding: 25px;
            margin-top: 25px;
            border-radius: 12px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }

        label {
            display: block;
            font-weight: bold;
            margin-top: 15px;
            margin-bottom: 8px;
        }

        textarea {
            width: 100%;
            padding: 12px;
            border: 1px solid #ccc;
            border-radius: 8px;
            box-sizing: border-box;
            resize: vertical;
        }

        button {
            margin-top: 20px;
            width: 100%;
            padding: 14px;
            background: #198754;
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 17px;
            cursor: pointer;
        }

        button:hover {
            background: #146c43;
        }

        .results {
            margin-top: 25px;
        }

        .card {
            background: white;
            margin-top: 15px;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }

        .score {
            font-weight: bold;
            color: #198754;
        }

        .difficulty {
            font-weight: bold;
        }

    </style>

</head>


<body>

<div class="container">

    <div class="header">

        <h1>🤖 AI Project Topic Recommender</h1>

        <p>
            Find the best project topics based on your
            interests, skills and career goals.
        </p>

    </div>


    <div class="form-box">

        <form method="POST">

            <label>🎯 Your Interests</label>

            <textarea
                name="interests"
                rows="3"
                placeholder="Example: Artificial Intelligence, NLP, Machine Learning"
                required>{{ interests }}</textarea>


            <label>💻 Your Skills</label>

            <textarea
                name="skills"
                rows="3"
                placeholder="Example: Python, Pandas, Scikit-learn, NLP"
                required>{{ skills }}</textarea>


            <label>🎓 Academic Background</label>

            <textarea
                name="background"
                rows="3"
                placeholder="Example: Data Science student interested in AI"
                required>{{ background }}</textarea>


            <label>🚀 Career Goal</label>

            <textarea
                name="career_goal"
                rows="3"
                placeholder="Example: Become an AI Engineer"
                required>{{ career_goal }}</textarea>


            <button type="submit">
                🔍 Get Project Recommendations
            </button>

        </form>

    </div>


    {% if recommendations %}

    <div class="results">

        <h2>🎯 Recommended Projects</h2>


        {% for project in recommendations %}

        <div class="card">

            <h2>
                {{ loop.index }}. {{ project.title }}
            </h2>

            <p>
                <strong>Domain:</strong>
                {{ project.domain }}
            </p>

            <p>
                <strong>Skills:</strong>
                {{ project.skills }}
            </p>

            <p class="difficulty">
                <strong>Difficulty:</strong>
                {{ project.difficulty }}
            </p>

            <p>
                <strong>Description:</strong>
                {{ project.description }}
            </p>

            <p class="score">
                Match Score:
                {{ "%.2f"|format(project.similarity_score * 100) }}%
            </p>

        </div>

        {% endfor %}

    </div>

    {% endif %}

</div>

</body>

</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():

    recommendations = []

    interests = ""
    skills = ""
    background = ""
    career_goal = ""

    if request.method == "POST":

        interests = request.form.get("interests", "")

        skills = request.form.get("skills", "")

        background = request.form.get("background", "")

        career_goal = request.form.get("career_goal", "")


        # Create student profile
        student_profile = f"""
        Interests: {interests}
        Skills: {skills}
        Academic Background: {background}
        Career Goal: {career_goal}
        """


        # Get top 5 recommendations
        recommendations = recommend_projects(
            student_profile,
            top_n=5
        ).to_dict("records")


    return render_template_string(
        HTML_PAGE,
        recommendations=recommendations,
        interests=interests,
        skills=skills,
        background=background,
        career_goal=career_goal
    )


if __name__ == "__main__":

    app.run(debug=True)