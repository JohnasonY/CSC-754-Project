import random   # randomly choose routes for vehicles.
import traci    # allows Python to control a running SUMO simulation
import sumolib  # read network files and locate the SUMO executable

NET_FILE = "intersection_fixed_trafficLight.xml"
SIM_TIME = 999999   # the maximum number of iterations for the simulation

# Read network and find valid routes
net = sumolib.net.readNet(NET_FILE)     # a network object containing information about roads, junctions, and connections
junction = net.getNode("J1")
routes = []

for edge in junction.getIncoming():
    for next_edge in edge.getOutgoing():

        # No U-turns
        if edge.getFromNode() == next_edge.getToNode():
            continue

        routes.append([edge.getID(), next_edge.getID()])      # append([incoming road id, outgoing road id])

print(routes)

# Start SUMO-GUI
traci.start([
    sumolib.checkBinary("sumo-gui"),
    "-n", NET_FILE,
    "--start",
    "--delay", "100"
])

try:
    # Register routes
    for i, route in enumerate(routes):
        traci.route.add(f"route{i}", route)

    # Run simulation
    for t in range(SIM_TIME):

        # Generate one vehicle every 3 seconds
        if t % 3 == 0:
            route_id = f"route{random.randrange(len(routes))}" # generate a random route id

            traci.vehicle.add(
                f"car{t}",  # unique car id
                route_id,   # the route to instantiate the car
                departLane="random" # randomly choose a departure lane
            )

        traci.simulationStep()

        # Display traffic light phase
        phase = traci.trafficlight.getPhase("J1")

        print(
            f"Time: {t + 1}s | "
            f"Phase: {phase} | "
            f"Vehicles: {traci.vehicle.getIDCount()}"
        )

finally:
    traci.close()
