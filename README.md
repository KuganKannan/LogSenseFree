# LogSense

**LogSense** is an intelligent log analysis tool designed to help developers quickly understand system failures by analyzing log files and highlighting the most important errors.

Instead of manually scanning thousands or millions of log lines, LogSense identifies recurring errors, highlights the most common issues, and shows a timeline of failures to help you find the root cause faster.

---

## Features

### Root Cause Detection

LogSense analyzes the timeline of log errors and highlights the **earliest failure**, helping developers quickly identify what likely caused the incident.

### Error Clustering

Errors are grouped together so you can immediately see which issues occur most frequently.

### Incident Timeline

View the sequence of errors as they occurred in the log to understand how a failure propagated through the system.

### Desktop GUI

LogSense includes a simple graphical interface with:

* Welcome screen
* Log explorer
* Manual page
* Split layout for reports

### Works With Large Logs

Logs are processed line-by-line so even very large log files can be analyzed.

---

## Example Output

```
LOGSENSE INCIDENT REPORT
--------------------------------

Lines scanned: 12043
Errors found: 245

Root Cause Candidate
DatabaseTimeoutException (first seen 2026-03-10 10:21:05)

Timeline
2026-03-10 10:21:05 → DatabaseTimeoutException
2026-03-10 10:21:07 → APIServiceException
2026-03-10 10:21:08 → GatewayError

Top Issues
1. DatabaseTimeoutException -> 117
2. APIServiceException -> 82
3. GatewayError -> 46
```

---

## Installation

Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/logsense.git
```

Navigate to the application folder:

```
cd logsense/logsense.app
```

Install dependencies:

```
pip install pillow
```

Run the application:

```
python main.py
```

---

## Building the Desktop Application

You can build LogSense into a standalone executable using PyInstaller.

Install PyInstaller:

```
pip install pyinstaller
```

Build the executable:

```
pyinstaller --onefile --windowed --icon=assets/logsense.ico --add-data "assets;assets" --name LogSense main.py
```

The executable will appear in:

```
dist/LogSense.exe
```

---

## Supported Log Formats

LogSense works with most logs containing common error indicators such as:

```
ERROR
Exception
Traceback
```

Example log entry:

```
2026-03-10 10:20:05 ERROR NullPointerException at UserService.java:42
```

---

## Project Structure

```
logsense
│
├── logsense.app
│   ├── main.py
│   ├── gui.py
│   ├── analyzer.py
│   ├── parser.py
│   ├── reporter.py
│   └── assets
│
├── logsense.web
│   ├── index.html
│   ├── styles.css
│   └── script.js
│
└── README.md
```

---

## Future Features

Planned improvements include:

* Stack trace clustering
* Error spike detection
* Visual error timeline graphs
* Distributed system log correlation
* IDE integration (Pro version)

---

## Author

Developed by **Kugan**, a developer focused on building tools that improve developer productivity.

The project was inspired through discussions with engineers working on large-scale distributed systems.

---

## License

This project is open source and available under the MIT License.
