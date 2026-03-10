def print_report(results):

    print("\nLOGSENSE INCIDENT REPORT")
    print("--------------------------------")

    print(f"Lines scanned: {results['lines']}")
    print(f"Errors found: {results['errors']}\n")

    if results["root_cause"]:

        ts, err = results["root_cause"]

        print("Root Cause Candidate")
        print(f"{err} (first seen {ts})\n")

    print("Top Issues")

    for i, (error, count) in enumerate(results["top"][:10], start=1):
        print(f"{i}. {error} -> {count}")

    print("\nTimeline")

    for ts, err in results["timeline"]:
        print(f"{ts} → {err}")