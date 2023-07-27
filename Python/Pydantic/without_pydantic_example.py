import json
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main() -> None:
    with open("./data.json") as file:
        data = json.load(file)
        print(data[0])


if __name__ == "__main__":
    main()
