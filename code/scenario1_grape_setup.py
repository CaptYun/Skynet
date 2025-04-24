# Scenario 1 GRAPE Setup (Colab Version)

# 🟩 Step 1: Setup directory
!mkdir -p config bt_xml

# 🟩 Step 2: Write full YAML config
yaml_content = '''
simulation:
  screen_width: 1000
  screen_height: 1000
  sampling_freq: 10
  gif_recording_fps: 10
  profiling_mode: false
  task_visualisation_factor: 1.0

saving_options:
  save_gif: false
  save_result_csv: true

plugin:
  behavior_tree_xml: default_bt.xml
  plugin_name: GRAPE

GRAPE:
  execute_movements_during_convergence: true
  initialize_partition: false
  reinitialize_partition_on_completion: false
  cost_weight_factor: 1.0
  social_inhibition_factor: 0.1

agents:
  quantity: 20
  locations:
    x_min: 0
    x_max: 100
    y_min: 0
    y_max: 100
    non_overlap_radius: 1.5
  max_speed: 2.0
  max_accel: 0.5
  max_angular_speed: 1.5
  target_approaching_radius: 2.0
  communication_radius: 15.0
  behavior_tree_xml: default_bt.xml
  work_rate: 1.0
  agent_track_size: 0.5
'''

with open("config/scenario1_grape_a20_t6.yaml", "w") as f:
    f.write(yaml_content)

# 🟩 Step 3: Write behavior tree file
bt_xml = '''<?xml version="1.0"?>
<root main_tree_to_execute="MainTree">
  <BehaviorTree ID="MainTree">
    <ReactiveFallback name="Root">
      <TaskAssignment/>
    </ReactiveFallback>
  </BehaviorTree>
</root>
'''

with open("bt_xml/default_bt.xml", "w") as f:
    f.write(bt_xml)

# 🟩 Step 4: Run GRAPE (must be in space-simulator root directory)
!python main.py --config config/scenario1_grape_a20_t6.yaml

# 🟩 Step 5: Find latest result file and visualize
import os
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from collections import Counter

latest = None
for root, _, files in os.walk("."):
    for f in files:
        if "grape" in root.lower() and f.endswith("agentwise.csv"):
            candidate = Path(root) / f
            if not latest or candidate.stat().st_mtime > latest.stat().st_mtime:
                latest = candidate

assert latest, "No result file found."
df = pd.read_csv(latest)

# Basic task assignment distribution plot
task_col = next((col for col in df.columns if "task" in col.lower()), None)
counts = Counter(df[task_col])
plt.bar(counts.keys(), counts.values(), edgecolor='black')
plt.title("GRAPE Result: Number of Agents per Task")
plt.xlabel("Task ID")
plt.ylabel("Number of Agents")
plt.grid(True)
plt.tight_layout()
plt.show()
