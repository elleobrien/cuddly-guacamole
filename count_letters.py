import sys

def count_letters(input_string):
    count = 0
    for char in input_string:
        if char.isalpha():
            count += 1
    return count

if __name__ == '__main__':
    input_string = sys.argv[1]
    print(count_letters(input_string))
