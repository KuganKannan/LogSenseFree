def format_report(results):

    report = []

    report.append("LOGSENSE INCIDENT REPORT")
    report.append("--------------------------------")

    report.append(f"Lines scanned: {results['lines']}")
    report.append(f"Errors found: {results['errors']}")
    report.append("")

    if results["root_cause"]:

        timestamp, error = results["root_cause"]

        report.append("Root Cause Candidate")
        report.append(f"{error} (first seen {timestamp})")
        report.append("")

    report.append("Timeline")

    for timestamp, error in results["timeline"]:

        report.append(f"{timestamp} → {error}")

    report.append("")
    report.append("Top Issues")

    for i, (error, count) in enumerate(results["top"][:10], start=1):

        report.append(f"{i}. {error} -> {count}")

    return "\n".join(report)