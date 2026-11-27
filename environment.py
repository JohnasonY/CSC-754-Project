"""SUMO environment scaffold; simulation control is not implemented yet.

Planned interface:
    reset(route_file, seed, gui=False) -> state
    step(action) -> (next_state, reward, done, info)
    close()

One action executes one complete 100-second signal cycle. Observe four
approach queue levels at cycle boundaries and reward the negative average
total queue across the cycle. Preserve yellow and all-red clearances.
"""
