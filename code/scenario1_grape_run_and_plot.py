# ✅ GRAPE 실행 및 결과 재현 시각화
# 파일명: scenario1_grape_run_and_plot.py
# 실행 조건: 현재 디렉토리가 space-simulator 폴더여야 함

import os
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# 0. 현재 작업 디렉토리 확인 및 이동
if not Path("run.py").exists():
    raise EnvironmentError("This script must be run from inside the 'space-simulator' directory.")

# 1. GRAPE 알고리즘 실행 (설정 파일에 기반)
CONFIG_FILE = "config/scenario1_grape.yaml"
if not Path(CONFIG_FILE).exists():
    raise FileNotFoundError(f"Missing configuration file: {CONFIG_FILE}")

os.system(f"python run.py --config {CONFIG_FILE}")

# 2. 최신 GRAPE 결과 파일 탐색 (agentwise.csv)
def find_latest_grape_result():
    latest = None
    for root, _, files in os.walk("."):
        for f in files:
            if "grape" in root.lower() and f.endswith("agentwise.csv"):
                candidate = Path(root) / f
                if not latest or candidate.stat().st_mtime > latest.stat().st_mtime:
                    latest = candidate
    return latest

csv_path = find_latest_grape_result()
if not csv_path:
    raise FileNotFoundError("No GRAPE result file (agentwise.csv) found.")

# 3. 결과 파일 불러오기 및 컬럼 확인
df = pd.read_csv(csv_path)
print("\nColumns:", df.columns.tolist())
print(df.head())

# 4. task 관련 컬럼 자동 탐색
task_col = next((col for col in df.columns if "task" in col.lower()), None)
if not task_col:
    raise ValueError("No column containing 'task' found in result file.")

# 5. Task ID별 에이전트 수 시각화
task_counts = Counter(df[task_col])
tasks = sorted(task_counts.keys())
counts = [task_counts[t] for t in tasks]

plt.figure(figsize=(10, 5))
plt.bar(tasks, counts, color='skyblue', edgecolor='black')
plt.title("GRAPE Result: Number of Agents per Task")
plt.xlabel("Task ID")
plt.ylabel("Number of Agents")
plt.grid(True)
plt.tight_layout()
plt.show()
