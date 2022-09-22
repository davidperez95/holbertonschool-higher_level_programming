#!/usr/bin/python3
import hidden_4


def main():

    new_list = dir(hidden_4)
    for i in range(len(new_list)):
        if new_list[i][:2] != '__':
            print(new_list[i])


if __name__ == "__main__":
    main()
