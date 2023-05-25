from dataclasses import dataclass


@dataclass
class StudentExamResultsOutputEntity:
    points: int
    max_points: int
    hours_pass: int
    minutes_pass: int
    seconds_pass: int
