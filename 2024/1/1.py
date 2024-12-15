import sys


def main(file_name):
    file_name = "2024/1/" + file_name
    with open(file_name, "r") as file:
        content = file.read()
    content = content.split("\n")
    total = 0
    for line in content:
        try:
            line = line.split()
            l = int(line[0])
            r = int(line[-1])
            total += abs(l-r)
        except:
            pass
    print(total)


if __name__ == '__main__':
    # Exclude script name
    args = sys.argv[1:]
    main(args[0])
