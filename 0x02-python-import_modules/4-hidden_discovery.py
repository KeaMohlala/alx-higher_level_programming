#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    names = dir(hidden_4)
    filtered_names = []
    for name in names:
        if not name.startswith("__"):
            filtered_names.append(name)
    filtered_names.sort()
    for i in range(len(filtered_names)):
        print(filtered_names[i])
