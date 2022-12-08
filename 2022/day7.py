class Node:
    def __init__(self, name):
        self.name = name
        self.nextArray = []
        self.parent = None
        self.size = 0
        self.directory = False

def build_filesystem(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f]

    root = Node('/')
    root.directory = True
    current = root
    # Ignore first line because it is always 'cd /' and we constructed a root already
    for line in lines[1:]:
        if '$ ls' in line:
            continue
        elif '$ cd' in line:
            directory = line.split('$ cd ')[1]
            # Ensure this directory has not been added already
            if directory == ".." and current.parent:
                current = current.parent
            else:
                directoryNode = None
                for node in current.nextArray:
                    if node.name == directory:
                        directoryNode = node
                if not directoryNode:
                    directoryNode = Node(directory)
                    directoryNode.parent = current
                    print(f"created directory node: {directoryNode.name}")
                    current.nextArray.append(directoryNode)
                current = directoryNode
        else: # file or directory being listed
            if 'dir' in line[:3]:
                directory = line.split('dir ')[1]
                if directory not in [x.name for x in current.nextArray]:
                    node = Node(directory)
                    node.directory = True
                    node.parent = current
                    current.nextArray.append(node)
            else:
                size, name = line.split(' ')
                if name not in [x.name for x in current.nextArray]:
                    # current.size += int(size)
                    node = Node(name)
                    node.parent = current
                    node.size = int(size)
                    current.nextArray.append(node)
    return root

def updateDirectorySizes(node):
    if not node:
        return 0

    for child in node.nextArray:
        updateDirectorySizes(child)
        node.size += child.size

    return node.size


def printNode(node):
    nodeDir = "dir" if node.directory else "file"
    print(f"- {node.name} ({nodeDir}), size: {node.size}")

def print_filesystem(node, indent):
    if not node:
        return

    for i in range(indent):
        print("  ", end="")
    printNode(node)
    for child in node.nextArray:
        for i in range(indent+1):
            print("  ", end="")
        # printNode(child)
        print_filesystem(child, indent+1)

# Print sum of all directories greater then maxSize
def part1(node, maxSize):
    if not node:
        return 0

    count = 0
    if node.directory and node.size <= maxSize:
        count += node.size

    for child in node.nextArray:
        if child.directory: # and child.size <= maxSize:
            count += part1(child, maxSize)

    return count

def part2(node, spaceNeeded, freeSize, acceptableNodes):
    if not node:
        return

    if node.directory and (freeSize + node.size >= spaceNeeded):
        acceptableNodes.append(node.size)

    for child in node.nextArray:
        if child.directory:
            part2(child, spaceNeeded, freeSize, acceptableNodes)


def main():
    # filesystem = build_filesystem('example.txt')
    filesystem = build_filesystem('input.txt')
    updateDirectorySizes(filesystem)
    print_filesystem(filesystem, 0)

    # print(f"Part 1: {part1(filesystem, 100000)}")
    print("Part 2")
    acceptableNodes = []
    part2(filesystem, 30000000, 70000000-filesystem.size, acceptableNodes)
    sortedNodes = sorted(acceptableNodes)
    print(sortedNodes[0])


if __name__ == '__main__':
    main()
