import random
from datetime import datetime, timedelta
import csv

# Helper functions
def csvWriter(output_file,data):
    with open(f'data/{output_file}',mode='w',newline="",encoding="utf-8") as file:
        writer = csv.DictWriter(file,fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    print(f"Generated rows and saved to {output_file}")

def random_date(start, end):
    """Generate a random datetime between two datetime objects."""
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

def generate_review_text():
    texts = [
        "Great product! Highly recommend.",
        "Not worth the price.",
        "Amazing quality and features.",
        "Disappointed with the performance.",
        "Exceeded my expectations!",
        "The design feels outdated.",
        "Good value for money.",
        "Too complicated to use.",
        "Excellent customer support experience.",
        "The material feels cheap.",
        "Love it! Will buy again."
    ]
    return random.choice(texts)

def generate_tone():
    tones = ["Positive", "Negative", "Neutral", None]  # Nullable field
    return random.choice(tones)

def generate_sentiment():
    sentiments = ["Joy", "Anger", "Trust", "Disgust", "Anticipation", None]  # Nullable field
    return random.choice(sentiments)

def generateReviewHistoryData(num_rows,categories):
    review_history_data = []
    start_date = datetime(2024, 12, 1)
    end_date = datetime(2025, 1, 23)

    for i in range(1, num_rows + 1):
        created_at = random_date(start_date, end_date)
        updated_at = created_at + timedelta(hours=random.randint(1, 48))
        review_history_data.append({
            "id": i,
            "text": generate_review_text(),
            "stars": random.randint(1, 10),
            "review_id": f"R-{random.randint(1, 500)}",
            "tone": generate_tone(),
            "sentiment": generate_sentiment() if random.random() > 0.2 else None,  # 20% NULL
            "category_id": random.choice(categories),
            "created_at": created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": updated_at.strftime("%Y-%m-%d %H:%M:%S"),
        })
    return review_history_data

def generateCategoricalData(categories):
    categorical_data = []
    for i in range(len(categories)):
        categorical_data.append({
            "id" : i+1,
            "name": categories[i],
            "description": f'Reviews on {categories[i]}'
        })
    return categorical_data




if __name__ == "__main__":
    dataset_size = 10000
    review_category_id = [1, 2, 3, 4, 5]
    review_history_data = generateReviewHistoryData(dataset_size,review_category_id)
    category_names = ['Electronics','Home Appliances','Books','Fashion','Automotive']
    categorical_data = generateCategoricalData(category_names)
    csvWriter('categories.csv',categorical_data)
    csvWriter('review_history.csv',review_history_data)
