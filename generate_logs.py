import random
from datetime import datetime, timedelta

# Error patterns
errors = [
    "kernel: Out of memory: Kill process 1234 (python) score 1000",
    "sshd[4567]: Connection refused",
    "CRON[5678]: CPU usage over threshold",
    "sshd[8901]: Connection timeout",
    "kernel: Disk read error",
    "INFO: Everything running smoothly",
    "NOTICE: Maintenance window starting",
    "AUTH: Login successful",
]

# Generate 10,000+ log lines
log_lines = []
start_time = datetime(2025, 7, 1, 0, 0, 0)

for i in range(10000):
    timestamp = (start_time + timedelta(seconds=i*5)).strftime("%b %d %H:%M:%S")
    server = f"server{random.randint(1,5)}"
    error = random.choice(errors)
    log_line = f"{timestamp} {server} {error}"
    log_lines.append(log_line)

# Write to logs/sample.log
with open("logs/sample.log", "w") as f:
    f.write("\n".join(log_lines))

print("✅ 10K+ log lines written to logs/sample.log")
