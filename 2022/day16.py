import sys
from collections import deque

infile = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(infile).read().strip()
lines = [line for line in data.split('\n')]

class Valve:
    def __init__(self, name):
        self.name = name
        self.flowRate = None
        self.neighbors = []
        self.open = False

    def __str__(self):
        string = f"\nValve: {self.name}\n"
        string += f"\tflowRate: {self.flowRate}\n"
        string += f"\topen: {self.open}\n"
        string += f"\tneighbors: "
        for neighbor in self.neighbors:
            string += f"{neighbor.name} "
        string += "\n"
        return string

name_to_valve = {}

for line in lines:
    valve, tunnels = line.split('; ')
    valve, flowRate = valve.split(' has flow rate=')
    valve = valve.split()[1]
    flowRate = int(flowRate)
    tunnels = tunnels.replace(',', '')
    tunnels = tunnels.split()[4:]

    if valve in name_to_valve:
        valve = name_to_valve[valve]
    else:
        valve = Valve(valve)
        name_to_valve[valve.name] = valve

    valve.flowRate = flowRate

    for tunnel in tunnels:
        if tunnel in name_to_valve:
            tunnel = name_to_valve[tunnel]
        else:
            tunnel = Valve(tunnel)
            name_to_valve[tunnel.name] = tunnel

        if tunnel not in valve.neighbors:
            valve.neighbors.append(tunnel)

for key in name_to_valve.keys():
    print(name_to_valve[key])

def calculatePressure(location, roundNum, roundPressure):
    if roundNum > 30:
        print(f"Returning pressure of: {roundPressure}")
        return roundPressure

    print(f"Round: {roundNum}")

    canidates = []
    for neighbor in location.neighbors:
        canidates.append(roundPressure + calculatePressure(neighbor, roundNum + 1, roundPressure))

    if not location.open:
        canidates.append(roundPressure + calculatePressure(location, roundNum + 1, roundPressure + location.flowRate))

    return max(canidates)


def part1():
    pressure = calculatePressure(name_to_valve['AA'], 1, 0)
    print(f"Final pressure released: {pressure}")

part1()
