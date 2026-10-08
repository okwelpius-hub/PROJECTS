# PROJECT: GRADE TRACKER
#1.The Data,Understand the structure. Each student has three scores. Some may be empty or have bad data

import csv
import io

csv_data = """name,score1,score2,score3
James Omondi,85,90,78
Sandra Weru,72, ,88
Patrick Njiru,91,87,94
Grace Achieng,60,bad data,70
Brian kamau,55,48,62"""

f = io.StringIO(csv_data)
reader = csv.DictReader(f)

for row in reader:
    print(dict(row))

print("*"*40)

#2. Parse Scores Safely, write a function that tries to convert a score to an integer. If it fails, Return none.

def parse_score(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

# Test
print(parse_score("85"))
print(parse_score(""))
print(parse_score("bad data"))
print(parse_score(None))

#3. Calculate Average and Letter Grade
# Write a function to calculate the average of valid scores only, and another to assign a letter grade.

def calculate_average(scores):
    valid = [s for s in scores if s is not None]
    if not valid:
        return None
    return round(sum(valid) /len(valid), 1)

def letter_grade(avg):
    if avg is None:
        return "N/A"
    if avg >= 90:
        return "A"
    if avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

# Test
scores_a = [85, 90, 78]
scores_b = [72, None, 88]
scores_c = [60, None, None]

for s in [scores_a, scores_b, scores_c]:
    avg = calculate_average(s)
    print(f"Scores: {s} | Avg: {avg} | Grade: {letter_grade(avg)}")

# Step 4: Full Grade Tracker
# Complete Grade Tracker- Reads CSV, parses scores with error handling, calculates averages and grades, prints a report and exports JSON results

import csv
import io
import json

csv_data = """name,score1,score2,score3
James Omondi,85,90,78
Sandra Weru,72, ,88
Patrick Njiru,91,87,94
Grace Achieng,60,bad data,70
Brian kamau,55,48,62"""

# Functions 
def parse_sscore(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

def calculate_average(scores):
    valid = [s for s in scores if s is not None]
    if not valid:
        return None
    return round(sum(valid) / len(valid), 1)

def letter_grade(avg):
    if avg is None: return "N/A"
    if avg >= 90: return "A"
    elif avg >= 80: return "B"
    elif avg >= 70: return "C"
    elif avg >= 60: return "D"
    else:           return "F"

#Process CSV
f = io.StringIO(csv_data)
reader = csv.DictReader(f)
results = []

print("=" * 50)
print(f"{'NAME':<20} {'AVG':>5} {'GRADE':>5} NOTES")
print("=" * 50)

for row in reader:
    scores = [
        parse_score(row["score1"]),
        parse_score(row["score2"]),
        parse_score(row["score3"])
    ]
    invalid_count = scores.count(None)
    avg = calculate_average(scores)
    grade = letter_grade(avg)
    notes = f"{invalid_count} invalid scores(s)" if invalid_count else "All scores valid"

    print(f"{row['name']:<20} {str(avg):>5} {grade:>5} {notes}")

    results.append({"name": row["name"],
                    "scores": [row["score1"], row["score2"], row["score3"]],
                    "average": avg,
                    "grade": grade})

print("=" * 50)

#Class Summary
valid_avgs = [r["average"] for r in results if r["average"] is not None]
class_avg = round(sum(valid_avgs) / len(valid_avgs), 1)
print(f"\nClass average: {class_avg}")
print(f"Students: {len(results)}")

#Export as JSON
print("\nJSON export:")
print(json.dumps(results, indent=2))