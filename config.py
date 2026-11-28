"""Shared paths and initial settings for the traffic-signal experiment."""

from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
NET_FILE = PROJECT_DIR / "models" / "networks" / "intersection_fixed_trafficLight.net.xml"
ROUTES_DIR = PROJECT_DIR / "models" / "routes"
MODELS_DIR = PROJECT_DIR / "models"
RESULTS_DIR = PROJECT_DIR / "results"
SCENARIOS = {
    name: ROUTES_DIR / f"{name}.rou.xml"
    for name in ("balanced", "ns_heavy", "ew_heavy")
}

TRAFFIC_LIGHT_ID = "J1"
SIMULATION_STEP_SECONDS = 1
EPISODE_SECONDS = 3600

# Green durations for XML phases 0, 3, 6, 9, respectively:
# N/S protected left, N/S normal, E/W protected left, E/W normal.
# Each green is followed by the existing yellow and all-red phases.
TIMING_PLANS = {
    0: (10, 30, 10, 30),  # Balanced (fixed-time baseline)
    1: (10, 40, 10, 20),  # Favor north-south
    2: (10, 20, 10, 40),  # Favor east-west
}
YELLOW_SECONDS = 3
ALL_RED_SECONDS = 2
CYCLE_SECONDS = 100
QUEUE_THRESHOLDS = (5, 10)  # Low: <5; medium: 5–9; high: >=10.

LEARNING_RATE = 0.1
DISCOUNT_FACTOR = 0.95
EPSILON_START = 1.0
EPSILON_MIN = 0.05
EPSILON_DECAY = 0.99
TRAINING_EPISODES = 200
Q_TABLE_FILE = MODELS_DIR / "q_table.npy"
