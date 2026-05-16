# 分析日志并生成报告
def analyze_logs():
    with open("logs.txt") as f:
        logs = f.readlines()
    errors = [line for line in logs if "ERROR" in line or "WARN" in line]
    with open("report.txt", "w") as f:
        for e in errors:
            f.write(e)

if __name__ == "__main__":
    analyze_logs()
