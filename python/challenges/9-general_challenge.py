"""
Problem: "Certification Score Aggregator"

Context: Your AI certification tool evaluates candidates across multiple skills. Each evaluation returns a JSON result.

Task: Write a Python function (or a small REST endpoint if they prefer) that:

Takes a list of evaluation results like:
evaluations = [
    {"skill": "Python", "score": 82, "passed": True,  "duration_s": 310},
    {"skill": "HTML",   "score": 55, "passed": False, "duration_s": 420},
    {"skill": "SQL",    "score": 91, "passed": True,  "duration_s": 280},
    {"skill": "Python", "score": 74, "passed": True,  "duration_s": 350},
]

Returns a summary dict containing:
overall_passed: True only if all skills have at least one passing result
average_score: mean score rounded to 1 decimal
by_skill: a dict keyed by skill with best_score, attempts, and passed
total_duration_minutes: total time rounded to 1 decimal

Expected output for the example above:

{
  "overall_passed": False,  # HTML never passed
  "average_score": 75.5,
  "by_skill": {
    "Python": {"best_score": 82, "attempts": 2, "passed": True},
    "HTML":   {"best_score": 55, "attempts": 1, "passed": False},
    "SQL":    {"best_score": 91, "attempts": 1, "passed": True},
  },
  "total_duration_minutes": 22.7
}
"""
from collections import defaultdict

def certification_aggregator(evaluations: list[dict[str, int| bool| int]]) -> dict:
    result = {
        "overall_passed": False,
        "average_score": 0,
        "by_skill": {},
        "total_duration_minutes": 0
    }
    result_per_skill = result["by_skill"]
    total_time = 0
    total_score = 0

    for evaluation in evaluations:
        skill = evaluation["skill"]
        score = evaluation["score"]
        passed = evaluation["passed"]
        duration = evaluation["duration_s"]

        total_score+=score
        total_time+=duration

        saved_res = result_per_skill.setdefault(skill, {"best_score":0, "attempts":0, "passed":False})
        saved_res["best_score"] = max(saved_res["best_score"], score)
        saved_res["attempts"]+=1
        saved_res["passed"] = saved_res["passed"] or passed
    

    result["overall_passed"] = all([s["passed"] for s in result_per_skill.values()])
    nb_eval = len(evaluations)
    result["average_score"] = round(total_score /nb_eval, 1)
    result["total_duration_minutes"] = round(total_time/60, 1)
    return result



evaluations = [
    {"skill": "Python", "score": 82, "passed": True,  "duration_s": 310},
    {"skill": "HTML",   "score": 55, "passed": False, "duration_s": 420},
    {"skill": "SQL",    "score": 91, "passed": True,  "duration_s": 280},
    {"skill": "Python", "score": 74, "passed": True,  "duration_s": 350},
]

print(certification_aggregator(evaluations))