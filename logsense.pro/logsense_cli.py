import sys
import time
import json
from collections import Counter

from analyzer import LogAnalyzer
from parser import read_log_file
from reporter import print_report


def load_lines(path):

    if path == "-":
        return sys.stdin

    return read_log_file(path)


def analyze(path):

    analyzer = LogAnalyzer()

    for line in load_lines(path):
        analyzer.process_line(line)

    results = analyzer.get_results()

    print_report(results)


def json_output(path):

    analyzer = LogAnalyzer()

    for line in load_lines(path):
        analyzer.process_line(line)

    results = analyzer.get_results()

    print(json.dumps(results, indent=2))


def watch(path):

    print("Watching log file...\n")

    analyzer = LogAnalyzer()

    with open(path, "r", encoding="utf-8") as file:

        file.seek(0, 2)

        while True:

            line = file.readline()

            if not line:
                time.sleep(1)
                continue

            analyzer.process_line(line)

            if "ERROR" in line or "Exception" in line:
                print("ERROR:", line.strip())


def summary(path):

    analyzer = LogAnalyzer()

    for line in load_lines(path):
        analyzer.process_line(line)

    results = analyzer.get_results()

    print("\nSummary")
    print("-------")

    print("Lines:", results["lines"])
    print("Errors:", results["errors"])
    print("Unique errors:", len(results["top"]))


def top(path):

    analyzer = LogAnalyzer()

    for line in load_lines(path):
        analyzer.process_line(line)

    results = analyzer.get_results()

    print("\nTop Errors")

    for err, count in results["top"][:10]:
        print(err, "->", count)


def timeline(path):

    analyzer = LogAnalyzer()

    for line in load_lines(path):
        analyzer.process_line(line)

    results = analyzer.get_results()

    print("\nTimeline")

    for ts, err in results["timeline"]:
        print(ts, "→", err)


def grep_logs(path, pattern):

    for line in load_lines(path):

        if pattern.lower() in line.lower():
            print(line)


def spikes(path):

    timestamps = []

    for line in load_lines(path):

        parts = line.split()

        if len(parts) >= 2:
            timestamps.append(parts[0] + " " + parts[1])

    counts = Counter(timestamps)

    print("\nError Spikes")

    for ts, count in counts.items():

        if count > 3:
            print(ts, "→", count, "events")


def stats(path):

    analyzer = LogAnalyzer()

    for line in load_lines(path):
        analyzer.process_line(line)

    results = analyzer.get_results()

    print("\nStatistics")

    print("Lines scanned:", results["lines"])
    print("Errors found:", results["errors"])

    if results["root_cause"]:
        print("Root cause:", results["root_cause"][1])


def interactive_shell():

    print("\nLogSense Pro CLI")
    print("Type 'help' for commands")
    print("Type 'exit' to quit\n")

    while True:

        command = input("logsense> ").strip()

        if command == "":
            continue

        if command == "exit":
            break

        if command == "help":

            print("""
Commands

analyze <file>
json <file>
watch <file>
summary <file>
top <file>
timeline <file>
grep <file> <pattern>
spikes <file>
stats <file>
exit
""")

            continue

        parts = command.split()

        cmd = parts[0]

        try:

            if cmd == "analyze":
                analyze(parts[1])

            elif cmd == "json":
                json_output(parts[1])

            elif cmd == "watch":
                watch(parts[1])

            elif cmd == "summary":
                summary(parts[1])

            elif cmd == "top":
                top(parts[1])

            elif cmd == "timeline":
                timeline(parts[1])

            elif cmd == "grep":
                grep_logs(parts[1], parts[2])

            elif cmd == "spikes":
                spikes(parts[1])

            elif cmd == "stats":
                stats(parts[1])

            else:
                print("Unknown command")

        except Exception as e:
            print("Error:", e)


def main():

    interactive_shell()


if __name__ == "__main__":
    main()