from collections import defaultdict, deque


def find_message_start(filename, message_marker_len):
    with open(filename, 'r') as f:
        for line in f:
            window = deque()
            for idx,char in enumerate(line):
                if len(window) < message_marker_len:
                    window.append(char)
                else:
                    window.popleft()
                    window.append(char)

                if len(set(window)) == message_marker_len:
                    print(f"First message_start: {idx + 1}")
                    return

def main():
    print("Part 1")
    find_message_start('input.txt', 4)
    print("Part 2")
    find_message_start('input.txt', 14)


if __name__ == '__main__':
    main()
