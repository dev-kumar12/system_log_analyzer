# System Log Analyzer

A Python-based tool that reads and analyzes system log files using regular expressions. It identifies patterns like network faults and resource overuse, and generates a report file for engineers.

## 🔧 Features

- ✅ Parses Linux-style logs (`.log` file)
- ✅ Detects network faults (e.g., connection timeout/refused)
- ✅ Identifies resource issues (e.g., memory, CPU, disk)
- ✅ Works on 10K+ lines easily
- ✅ Auto-generates `report.txt` summary

## 📁 Folder Structure
system_log_analyzer/
├── analyzer.py
├── logs/
│ └── sample.log
├── report.txt <-- (Generated)
└── README.md

## 🚀 How to Run

1. Place your log file inside the `logs/` folder.
2. Run the script:

```bash
python analyzer.py

==== Network Faults ====
Jul 13 13:01:12 server1 sshd[4567]: Connection refused

==== Resource Overuse ====
Jul 13 13:00:21 server1 kernel: Out of memory: Kill process...

