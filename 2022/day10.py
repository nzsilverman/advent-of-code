def readInput(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f]
    return lines

def addNoops(lines):
    newLines = []
    for idx, line in enumerate(lines):
        if "addx" in line:
            newLines.append("noop")

        newLines.append(line)

    return newLines

def printMsg(xVal, cycleIdx):
    if cycleIdx % 40 == 0:
        print("")

    sprite = [xVal, xVal-1, xVal+1]
    if cycleIdx % 40 in sprite:
        print("#", end="")
    else:
        print(" ", end="")

def main():
    # lines = readInput('example.txt')
    # lines = readInput('example2.txt')
    lines = readInput('input.txt')
    noopAdded = addNoops(lines)

    xVals = [1]
    print(len(noopAdded))
    for idx, line in enumerate(noopAdded):
        # cycleNum = idx + 1
        xVal = xVals[-1] if xVals else 1
        printMsg(xVal, idx)
        if 'addx' in line:
            _, val = line.split()
            val = int(val)
            xVal += val

        xVals.append(xVal)

    print("\n")


    # Calculate signal strength
    signalSum = 0
    for cycleNum in range(20, 220 + 1, 40):
        cycleIdx = cycleNum - 1
        signalStrength = xVals[cycleIdx] * cycleNum
        signalSum += signalStrength

    print(f"Signal Sum: {signalSum}")



if __name__ == '__main__':
    main()
