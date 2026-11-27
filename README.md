# CSC-754: Adaptive Traffic Signal Timing

SUMO simulation of one intersection, with a planned tabular Q-learning
controller compared against a fixed-time baseline.

## Project structure

```text
config.py          Shared paths and proposed experiment settings
networks/          Existing SUMO road networks
routes/            Demand files created manually in NETEDIT
environment.py     Scaffold for SUMO cycle execution and observations
q_learning.py      Scaffold for the Q-learning agent
train.py           Training entry-point scaffold
evaluate.py        Evaluation entry-point scaffold
demo.py            Original fixed-time SUMO-GUI demonstration
models/            Saved Q-table (generated later)
results/           Metrics and plots (generated later)
```

## Current status

The folder structure and configuration are ready. The original
`test_traffic_light.py` is now `demo.py`, with its network path updated.
It still generates vehicles in Python every three simulation iterations;
it does not yet load the planned NETEDIT demand files.

The environment, agent, training, and evaluation files are scaffolds, not
a working RL implementation. No route files, trained models, or results
have been fabricated.

## Setup and existing demo

Install SUMO separately, with `sumo` and `sumo-gui` available on PATH.
Install the Python dependencies in your preferred virtual environment:

```sh
python -m pip install -r requirements.txt
python demo.py
```

## Planned RL experiment

- State: low/medium/high stopped-vehicle counts for each of four approaches.
- Actions: balanced, N/S-priority, or E/W-priority green timing plans.
- Timing: one action per 100-second cycle, retaining protected-left,
  yellow, and all-red phases in their existing order.
- Reward: negative average total queue over the completed cycle.
- Agent: 81 states by 3 actions in a Q-table; epsilon-greedy training.
- Baseline: always select the balanced plan.
- Evaluation: freeze learning and exploration; compare both controllers
  on the same demand cases and seeds, including unfinished demand metrics.

Settings in `config.py` are starting values for the future implementation.
They do not change the original demo's timing or runtime yet.

## Next steps

1. Create the three scenario demand files described in `routes/README.md`.
2. Implement and verify the shared SUMO environment and fixed-time baseline.
3. Implement Q-learning, training, and model saving.
4. Evaluate both controllers and produce comparison plots.

The uncontrolled network is preserved for reference; it is not required
for the initial fixed-time versus Q-learning comparison.
