import re
from collections import defaultdict
from datetime import datetime

ERROR_PATTERN = re.compile(r"(ERROR|Exception|Traceback)")
TIMESTAMP_PATTERN = re.compile(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}")


class LogAnalyzer:

    def __init__(self):

        self.total_lines = 0
        self.errors = defaultdict(int)

        self.timeline = []

        self.first_occurrence = {}

    def process_line(self, line):

        self.total_lines += 1

        if ERROR_PATTERN.search(line):

            error_name = self.extract_error(line)
            timestamp = self.extract_timestamp(line)

            self.errors[error_name] += 1

            if error_name not in self.first_occurrence:
                self.first_occurrence[error_name] = timestamp

            if timestamp:
                self.timeline.append((timestamp, error_name))

    def extract_error(self, line):

        parts = line.split()

        for word in parts:

            if "Exception" in word or "Error" in word:
                return word

        return "UnknownError"

    def extract_timestamp(self, line):

        match = TIMESTAMP_PATTERN.search(line)

        if match:
            return match.group(0)

        return None

    def get_results(self):

        sorted_errors = sorted(
            self.errors.items(),
            key=lambda x: x[1],
            reverse=True
        )

        root_cause = None

        if self.timeline:

            earliest = min(self.timeline, key=lambda x: x[0])
            root_cause = earliest

        return {
            "lines": self.total_lines,
            "errors": sum(self.errors.values()),
            "top": sorted_errors,
            "timeline": sorted(self.timeline)[:10],
            "root_cause": root_cause
        }