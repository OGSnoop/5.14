# Type all other functions here

def print_menu(usrStr):
    menuOp = ' '
    print("MENU")
    print('c - Number of non-whitespace characters')
    print('w - Number of words')
    print('f - Fix capitalization')
    print('r - Replace punctuation')
    print('s - Shorten spaces')
    print('q - Quit')
    print()
    menuOp = input('Choose an option:\n')

    while menuOp != 'q':
        if menuOp == 'c':
            def get_num_of_non_WS_characters(usrStr):
                usrStr = usrStr.replace(" ", "")
                usrStr = usrStr.replace("   ", "")
                print('Number of non-whitespace characters:', len(usrStr))
            get_num_of_non_WS_characters(usrStr)
            return
        
        elif menuOp == 'w':
            def get_num_of_words(usrStr):
                wordcount = 1
                usrStr = usrStr.replace("  ", " ")
                for character in usrStr:
                    if character == " ":
                        wordcount += 1
                    
                    else:
                        pass
                print('Number of words:', wordcount)
            get_num_of_words(usrStr)
            return
            
        elif menuOp == 'f':
            def fix_capilization(usrStr):
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
                print('Number of letters capitalized:', capitals)
                print('Edited text:', revised_usrStr)
            fix_capilization(usrStr)
            return
        
        elif menuOp == 'r':
            def replace_punctuation(usrStr):
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
                print('exclamatioCount:', exclamationCount)
                print('semicolonCount:', semicolonCount)
                print('Edited text:', revised_usrStr)
            replace_punctuation(usrStr)
            return
                
        elif menuOp == 's':
            def shorten_space(usrStr):
                revised_usrStr = ''
                word_list = usrStr.split()
                
                
                for word in word_list:
                
                    if revised_usrStr == '':
                        revised_usrStr = word
                        
                    elif revised_usrStr != '':
                        revised_usrStr = revised_usrStr + ' ' + word
                        
                print('Edited text:', revised_usrStr)
                
            shorten_space(usrStr)
            return
        
        else:
            menuOp = input('INVALID, please choose a proper option:\n')
            
    while menuOp == 'q':
        break
    
    return menuOp, usrStr


if __name__ == '__menu__':
    usrStr = input('Enter a sample text:\n')
    print()
    print('You entered:', usrStr)
    print()
    print_menu(usrStr)
 
