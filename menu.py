def get_num_of_non_WS_characters(usrStr):
    char_count = 0
    usrStr = usrStr.replace(" ", "")
    usrStr = usrStr.replace("\t", "")
    
    for character in usrStr:
        if character != '!' or character != '?' or character != '.' or character != ' ' or character != ',' or character != ';' or character != "'":
            char_count += 1
        else:
            pass
    print('Number of non-whitespace characters:', char_count)
    return char_count

def get_num_of_words(usrStr):
    wordcount = 1
    usrStr = usrStr.replace("  ", " ")
    usrStr = usrStr.replace("  ", " ")
    for character in usrStr:
        if character == " ":
            wordcount += 1
                    
        else:
            pass
    print('Number of words:', wordcount)
    return wordcount

def fix_capitalization(usrStr):
    capitals = 0
    char_list = []
    char_id = 0
    revised_usrStr = ''
    cap_me = 'false'
    usrStr = usrStr.lower()
                
    for character in usrStr:
        char_list.append(character)
                    
        if char_list[0].islower():
            char_list[0] = usrStr[0].upper()
            capitals += 1
                    
    for character in char_list:
                    
        if cap_me == 'true' and character != ' ' and character != '\t':
            char_list[char_id] = usrStr[char_id].upper()
            capitals += 1
            cap_me = 'false'
                        
        elif character == '.' or character == '!' or character == '?':
            cap_me = 'true'
        char_id += 1
                
    for character in char_list:
        revised_usrStr += character
        
    revised_usrStr =revised_usrStr.replace(" i ", " I ")
    print('Number of letters capitalized:', capitals)
    print('Edited text:', revised_usrStr)
    return revised_usrStr, capitals

def replace_punctuation(usrStr, exclamationCount, semicolonCount):
    revised_usrStr = ''
    exclamationCount = 0
    semicolonCount = 0
    for character in usrStr:
                
        if character == '!':
            exclamationCount += 1
                        
        elif character == ';':
            semicolonCount += 1
                        
    revised_usrStr = usrStr.replace('!', '.')
    revised_usrStr = revised_usrStr.replace(';', ',')
    print('Punctuation replaced')
    print('exclamationCount:', exclamationCount)
    print('semicolonCount:', semicolonCount)
    print('Edited text:',revised_usrStr)
    return (revised_usrStr, exclamationCount, semicolonCount)

def shorten_space(usrStr):
    revised_usrStr = ''
    word_list = usrStr.split()
                
                
    for word in word_list:
                
        if revised_usrStr == '':
            revised_usrStr = word
                        
        elif revised_usrStr != '':
            revised_usrStr = revised_usrStr + ' ' + word
                        
    print('Edited text:', revised_usrStr)
    return revised_usrStr

def print_menu(usrStr):
    global menuOp
    print("MENU")
    print('c - Number of non-whitespace characters')
    print('w - Number of words')
    print('f - Fix capitalization')
    print('r - Replace punctuation')
    print('s - Shorten spaces')
    print('q - Quit')
    print()
    menuOp = input('Choose an option:\n')
    while menuOp != 'c' and menuOp != 'w' and menuOp != 'f' and menuOp != 'r' and menuOp != 's' and menuOp != 'q':
        menuOp = input('Choose an option:')
    return menuOp


if __name__ == '__main__':
    usrStr = input('Enter a sample text:\n')
    print()
    print('You entered:', usrStr)
    print()
    
    menuOp = ''
    while menuOp != 'q':
        print_menu(usrStr)
        if menuOp == 'c':
            get_num_of_non_WS_characters(usrStr)
            print()
           
        elif menuOp == 'w':
            get_num_of_words(usrStr)
            print()

        elif menuOp == 'f':
            fix_capitalization(usrStr)
            print()
            
        
        elif menuOp == 'r':
            replace_punctuation(usrStr, 0, 0)
            print()

        elif menuOp == 's':    
            shorten_space(usrStr)
            print()

        elif menuOp == 'q':
            break
            
   
