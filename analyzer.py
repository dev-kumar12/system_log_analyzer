import re

with open("logs/sample.log", "r") as file:
    lines = file.readlines()

network_errors = []
resource_issues = []

for line in lines:
    if re.search(r'connection (refused|timeout)', line, re.IGNORECASE):
        network_errors.append(line.strip())

    if re.search(r'out of memory|CPU usage|disk error', line, re.IGNORECASE):
        resource_issues.append(line.strip())

with open("report.txt", "w") as report:
    report.write("==== Network Faults ====\n")
    report.write("\n".join(network_errors) + "\n\n")
    report.write("==== Resource Overuse ====\n")
    report.write("\n".join(resource_issues) + "\n")

print("✅ Report generated as report.txt")
