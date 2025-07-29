import re

class LexicalAnalyzer(object):
    def analyze_tokens(input_string,rules,tokens):
        current_index = 0

        while current_index < len(input_string):                                    #loop the input string
            found_match = False
            for token_name, pattern in rules:                                       #loop the rules tuple
                if token_name == 'TOKEN_ONELINECOMMENT' and current_index != 0:     # Skip checking for ONELINECOMMENT if not at the start of the string
                    continue
                match = re.match(pattern, input_string[current_index:])             #identify match and remove the number of character of the current index number from the front of the input string
                if match:
                    tokens.append((token_name, match.group()))                      #append the matching token name and group
                    current_index += len(match.group())                             #add the length of the current match group to the current index
                    found_match = True
                    break
            if not found_match:
                current_index += 1                                                  #add 1 to current index

        #print_tokens(tokens)                                                       #call the print tokens function
        return tokens

    #this function prints the tokens and values to the console in a user friendly format
    def print_tokens(tokens):
        for token_name, match in tokens:
            print("Token:", token_name)
            print("Pattern match:", match)
            print()

    #this function appends any non comments to the stripped_tokens
    def strip_comment_tokens(tokens, stripped_tokens):
        for token_name, match in tokens:
            if token_name != 'TOKEN_ONELINECOMMENT' and token_name != 'TOKEN_MULTILINECOMMENT':
                stripped_tokens.append((token_name, match))
        
        LexicalAnalyzer.print_tokens(stripped_tokens)




