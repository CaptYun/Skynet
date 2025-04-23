# scenario1_simulation_extended.py

# ✅ 확장 시뮬레이터 구조 초기화
# GRAPE 기반 분산 Task Allocation에 시간, 고도, 우선권 로직 포함

class TaskBlock:
    def __init__(self, tid, x, y, altitude, time_slot):
        self.tid = tid
        self.x = x
        self.y = y
        self.altitude = altitude
        self.time_slot = time_slot
        self.coalition = []

    def update_coalition(self, agent):
        if agent not in self.coalition:
            self.coalition.append(agent)

    def is_available(self, current_time):
        return self.time_slot == current_time

class Agent:
    def __init__(self, aid, start, goal, speed, fuel_level, eta):
        self.aid = aid
        self.start = start
        self.goal = goal
        self.position = start
        self.speed = speed
        self.fuel_level = fuel_level
        self.eta = eta
        self.assigned_task = None

    def evaluate_tasks(self, tasks, current_time):
        best_utility = -float('inf')
        best_task = None
        for task in tasks:
            if not task.is_available(current_time):
                continue
            d_ij = self.distance((task.x, task.y))
            p_collision = len(task.coalition) / 10
            wait_time = abs(task.time_slot - current_time)
            priority = self.compute_priority(task)
            utility = (
                1.0 / d_ij +
                (1 - p_collision) +
                1.0 / (wait_time + 1e-5) -
                len(task.coalition) +
                priority
            )
            if utility > best_utility:
                best_utility = utility
                best_task = task
        return best_task

    def compute_priority(self, task):
        # 우선권 로직: 연료 부족 + ETA에 가까운 task 선호
        return max(0.0, (self.fuel_level / 100) + (1.0 - abs(task.time_slot - self.eta) / 10))

    def distance(self, pos):
        dx = self.position[0] - pos[0]
        dy = self.position[1] - pos[1]
        return (dx**2 + dy**2)**0.5

class Airspace3D:
    def __init__(self, width, height, altitudes, time_slots):
        self.tasks = []
        tid = 0
        for t in time_slots:
            for z in altitudes:
                for x in range(width):
                    for y in range(height):
                        self.tasks.append(TaskBlock(tid, x, y, z, t))
                        tid += 1

def run_simulation():
    airspace = Airspace3D(width=5, height=5, altitudes=[100,200], time_slots=range(10))
    agents = [
        Agent(aid=0, start=(0,0), goal=(4,4), speed=1, fuel_level=80, eta=5),
        Agent(aid=1, start=(0,4), goal=(4,0), speed=1, fuel_level=60, eta=6)
    ]

    for t in range(10):
        for task in airspace.tasks:
            task.coalition = []
        for agent in agents:
            chosen_task = agent.evaluate_tasks(airspace.tasks, current_time=t)
            if chosen_task:
                chosen_task.update_coalition(agent)
                agent.assigned_task = chosen_task
        print(f"Step {t}:")
        for agent in agents:
            print(f"  Agent {agent.aid} -> Task {agent.assigned_task.tid if agent.assigned_task else 'None'}")

if __name__ == "__main__":
    run_simulation()
