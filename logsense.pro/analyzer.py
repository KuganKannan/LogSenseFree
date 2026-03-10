import re
from collections import defaultdict

ERROR_PATTERN = re.compile(r"(ERROR|Exception|Traceback)")


class LogAnalyzer:

    def __init__(self):

        self.total_lines = 0
        self.errors = defaultdict(int)
        self.timeline = []

    def process_line(self, line):

        self.total_lines += 1

        if ERROR_PATTERN.search(line):

            error_name = self.extract_error(line)
            timestamp = self.extract_timestamp(line)

            self.errors[error_name] += 1

            if timestamp:
                self.timeline.append((timestamp, error_name))

    def extract_error(self, line):

        words = line.split()

        for word in words:

            if "Exception" in word or "Error" in word:
                return word

        return "UnknownError"

    def extract_timestamp(self, line):

        parts = line.split()

        if len(parts) >= 2:
            return parts[0] + " " + parts[1]

        return None

    def get_results(self):

        sorted_errors = sorted(
            self.errors.items(),
            key=lambda x: x[1],
            reverse=True
        )

        root_cause = None

        if self.timeline:
            root_cause = min(self.timeline, key=lambda x: x[0])

        return {
            "lines": self.total_lines,
            "errors": sum(self.errors.values()),
            "top": sorted_errors,
            "timeline": self.timeline[:20],
            "root_cause": root_cause
        }