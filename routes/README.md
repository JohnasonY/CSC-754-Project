# Traffic demand files

Create these demand files in SUMO NETEDIT and save them here:

- `balanced.rou.xml`: similar demand from all four approaches.
- `ns_heavy.rou.xml`: more north/south demand.
- `ew_heavy.rou.xml`: more east/west demand.

Keep total demand and simulation duration comparable across scenarios.
Define routes and vehicles or flows, not routes alone. Cover the configured
episode duration. The files are not included yet; do not use empty XML files
as substitutes for real demand.

No Python route-generation script is required. Reuse the same demand files
for controller comparisons, and record the SUMO seed for each run. A seed
in a filename does not configure SUMO. Deterministic flows do not acquire
random arrival times just because the seed changes. For evaluation on new
traffic schedules, add distinct demand files or intentionally randomized
flows and keep evaluation cases separate from training.
