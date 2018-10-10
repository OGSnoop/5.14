def get_num_of_characters(inputStr):
    count = 0
    for character in inputStr:
        count += 1
    return count
    
def output_without_whitespace(inputStr):
    new = inputStr.replace(" ", "")
    new = new.replace("    ", "")
    return new




if __name__ == '__main__':
    inputStr = input('Enter a sentence or phrase:')
    print()
    print()
    print('You entered:', inputStr)
    print()
    print('Number of characters:', get_num_of_characters(inputStr))
    print('String with no whitespace:', output_without_whitespace(inputStr))
