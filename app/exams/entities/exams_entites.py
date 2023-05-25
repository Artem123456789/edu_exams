from dataclasses import dataclass


@dataclass
class StudentExamResultsOutputEntity:
    points: int
    max_points: int
