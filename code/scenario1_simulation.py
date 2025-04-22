# scenario1_simulation.py
# Basic simulation structure for Scenario 1 – Distributed Task Allocation using GRAPE logic

import random
import math

# -------------------------------
# Task definition
# -------------------------------
class Task:
    def __init__(self, tid, location):
        self.tid = tid
        self.location = location
        self.coalition = []

    def update_coalition(self, agent):
        if agent not in self.coalition:
            self.coalition.append(agent)

    def reset_coalition(self):
        self.coalition = []

# -------------------------------
# Agent definition
# -------------------------------
class Agent:
    def __init__(self, aid, position):
        self.aid = aid
        self.position = position
        self.assigned_task = None

    def evaluate_tasks(self, tasks):
        utilities = []
        for task in tasks:
            d_ij = self.distance(task.location)
            p_collision = len(task.coalition) / 10  # example: collision increases with coalition size
            wait_time = random.uniform(1, 5)
            utility = (
                ALPHA / d_ij +
                BETA * (1 - p_collision) +
                GAMMA / wait_time -
                DELTA * len(task.coalition)
            )
            utilities.append((utility, task))
        utilities.sort(reverse=True, key=lambda x: x[0])
        return utilities[0][1]

    def distance(self, task_location):
        dx = self.position[0] - task_location[0]
        dy = self.position[1] - task_location[1]
        return math.sqrt(dx**2 + dy**2)

# -------------------------------
# Simulation setup
# -------------------------------
def run_simulation():
    agents = [Agent(aid=i, position=(0, i)) for i in range(NUM_AGENTS)]
    tasks = [Task(tid=j, location=(9, j)) for j in range(NUM_TASKS)]

    for t in range(MAX_STEPS):
        print(f"Step {t+1}")
        for task in tasks:
            task.reset_coalition()
        for agent in agents:
            chosen_task = agent.evaluate_tasks(tasks)
            chosen_task.update_coalition(agent)
            agent.assigned_task = chosen_task
        print_summary(agents)

def print_summary(agents):
    for agent in agents:
        print(f"Agent {agent.aid} assigned to Task {agent.assigned_task.tid}")

# -------------------------------
# Parameters (can be tuned)
# -------------------------------
NUM_AGENTS = 5
NUM_TASKS = 5
MAX_STEPS = 10
ALPHA = 1.0
BETA = 1.0
GAMMA = 1.0
DELTA = 1.0

if __name__ == "__main__":
    run_simulation()
