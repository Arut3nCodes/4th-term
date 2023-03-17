# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def fileReader(fileName, lines):
    with open(fileName, encoding='utf-8') as file:
        for line in file:
            lines.append(str(line))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    allOfTheInformation = []
    fileReader('NASA', allOfTheInformation)
    print(allOfTheInformation[0])
    splitInfo = allOfTheInformation[0].split()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
