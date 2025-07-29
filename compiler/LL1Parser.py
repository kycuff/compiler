from typing import Optional


class LL1Parser(object):
    def parser(tokens):
        #terminal rules(columns)
        terminals = [
            'IF',
            'LBRACKET',
            'RBRACKET',
            'LBRACE',
            'RBRACE',
            'ELSE',
            'ELSEIF',
            'WHILE',
            'GT',   
            'LT', 
            'EQ',
            'NE', 
            'STRING',
            'NUMBER',
            'INT',
            'FLOAT',
            'STRINGTYPE',
            'PRINT',
            'ID',
            'PCOMMA',
            'ATTR',
            'PLUS',
            'MINUS',
            'MULT',
            'DIV']

        #non- teminal rules(rows)
        non_terminals = [
            '<if_statement>',
            '<else_clause>',
            '<else_clause>',
            '<else_clause>',
            '<while_loop>',
            '<exp>',
            '<exp>',
            '<exp>',
            '<value>',
            '<value>',
            '<variable>',
            '<assign_statement>',
            '<print_statement>',
            '<statement>',
            '<identifier>',
            '<comparison_operator>',
            '<type>']
        
        #representation of parsing table and the rule number that use them
        parsing_table = [
            [1,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,4,2,3,None,None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,5,None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None,None,None,6,8,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None,None,None,10,9,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None,None,None,None,None,11,11,11,None],
            [None,None,None,None,None,None,None,None,None,None,None,None,12,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,13],
            [1,None,None,None,None,None,None,None,None,None,None,None,12,None,None,None,None,13],
            [None,None,None,None,None,None,None,None,None,None,None,None,15,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,16,16,16,16,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None,None,None,None,None,17,17,17,None],
        ]

        stack = LL1Parser.get_rule(tokens) #get the rule being parsed
        token_index = 0 # keep track of the current token
        column_indices = LL1Parser.get_indices(terminals)
        row_indices = LL1Parser.get_indices(non_terminals)

        while stack:
            #try to catch index out of range error which occurs for an epsilon case with an else clause
            try:
                top = stack[-1]
                token = tokens[token_index][0].replace('TOKEN_','') #remove the token pre-fix to use as terminal comparison
                lookahead = LL1Parser.get_lookahead(tokens,token_index)

                if top in non_terminals:
                    column_number = LL1Parser.getFirst(top,token) # get the column number of the production rule
                    row_index = row_indices[top]
                    column_index = column_number

                #consumes the terminals
                if top.upper() in terminals:
                    if top == token: #compare the top of the stack with the current terminal token
                        stack.pop()
                        token_index += 1
                    else:
                        print("Unexpected token:", token)
                        exit()
                else:
                    production = parsing_table[row_index][column_index]
                    if production is None:
                        print("Unexpected token:", token)
                        exit()
                    else:
                        stack.pop() # removes non terminal rules before appending the production rules for the non-terminal
                        LL1Parser.push_production(stack,production,lookahead,tokens[token_index][0].replace('TOKEN_',''))
            
            except IndexError:
                stack.pop()

        #Once each token has been consumed the 'Parsing successful' message will show, otherwise it will display a failure
        if token_index == len(tokens):
            print("Parsing successful!")
        else:
            print("Parsing failed!")

    #method to find lookahead if any
    def get_lookahead(tokens,token_index):
        try:
            return tokens[token_index + 1][0].replace('TOKEN_','')
        except IndexError:
            return None

    #method tho append the correct production rules for a given rule
    def push_production(stack,prod_rule,lookahead,optional_token =""):
        match prod_rule:
            case 1:
                    stack.append('<else_clause>')
                    stack.append('RBRACE')
                    stack.append('<statement>')
                    stack.append('LBRACE')
                    stack.append('RBRACKET')
                    stack.append('<exp>')
                    stack.append('LBRACKET')
                    stack.append('IF')
            case 2:
                    stack.append('<else_clause>')
                    stack.append('RBRACE')
                    stack.append('<statement>')
                    stack.append('LBRACE')
                    stack.append('RBRACKET')
                    stack.append('<exp>')
                    stack.append('LBRACKET')
                    stack.append('ELSEIF')
            case 4:
                    stack.append('RBRACE')
                    stack.append('<statement>')
                    stack.append('LBRACE')
                    stack.append('ELSE')
            case 5:
                    stack.append('RBRACE')
                    stack.append('<statement>')
                    stack.append('LBRACE')
                    stack.append('RBRACKET')
                    stack.append('<exp>')
                    stack.append('LBRACKET')
                    stack.append('WHILE')
            case 6:
                    stack.append('<value>')
                    stack.append('<comparison_operator>')
                    stack.append('<identifier>')
            case 9:
                    if lookahead == 'PLUS':
                        stack.append('NUMBER')
                        stack.append('PLUS')
                        stack.append('NUMBER')
                    else:
                        stack.append('NUMBER')
            case 10:
                    stack.append('STRING')
            case 11:
                    stack.append('<assign_statement>')
                    stack.append('<type>')
            case 12:
                    stack.append('PCOMMA')
                    stack.append('<value>')
                    stack.append('ATTR')
                    stack.append('<identifier>')
            case 13:
                    stack.append('PCOMMA')
                    stack.append('RBRACKET')
                    stack.append('<value>')
                    stack.append('LBRACKET')
                    stack.append('PRINT')
            case 15:
                    stack.append('ID')
            case 16:
                if optional_token == 'GT':
                    stack.append('GT')
                elif optional_token == 'LT':
                    stack.append('LT')
                elif optional_token == 'EQ':
                    stack.append('EQ')
                else:
                    stack.append('NE')
            case 17:
                if optional_token == 'INT':
                    stack.append('INT')
                elif optional_token == 'FLOAT':
                    stack.append('FLOAT')
                elif optional_token == 'STRINGTYPE':
                    stack.append('STRINGTYPE')
            case _:
                    raise Exception('No valid rule for non-terminal')

    #method to return the first terminal from the rule
    def getFirst(top,token):
        if top == '<if_statement>':
            return 0
        elif top == '<else_clause>' and token == 'ELSE':
            return 4
        elif top == '<else_clause>' and token == 'ELSEIF':
            return 5
        elif top == '<else_clause>' and token == 'ELSEIF':
            return 6
        elif top == '<exp>' and token == 'ID':
            return 12
        elif top == '<identifier>':
            return 12
        elif top == '<comparison_operator>' and token == 'GT':
            return 8
        elif top == '<comparison_operator>' and token == 'LT':
            return 9
        elif top == '<comparison_operator>' and token == 'EQ':
            return 10
        elif top == '<comparison_operator>' and token == 'NE':
            return 11
        elif top == '<value>' and token == 'STRING':
            return 12
        elif top == '<value>' and token == 'NUMBER':
            return 13
        elif top == '<statement>' and token == 'PRINT':
            return 17
        elif top == '<statement>' and token == 'IF':
            return 0
        elif top == '<while_loop>':
            return 7
        elif top == '<variable>' and token == 'INT':
            return 14
        elif top == '<variable>' and token == 'FLOAT':
            return 15
        elif top == '<variable>' and token == 'STRINGTYPE':
            return 16
        elif top == '<type>' and token == 'INT':
            return 14
        elif top == '<type>' and token == 'FLOAT':
            return 15
        elif top == '<type>' and token == 'STRINGTYPE':
            return 16
        elif top == '<assign_statement>':
            return 12
        elif top == '<print_statement>':
            return 17
        else:
            raise Exception('No valid production rule')
        

    #method to determine the rule being parsed. Exception thrown if it is not valid
    def get_rule(tokens):
        try:
          rule = tokens[0][0]
        except:
          raise Exception('No valid token identified')

        #Get the rule from the first token
        if rule == 'TOKEN_IF':
            return ['<if_statement>']
        elif rule == 'TOKEN_ELSE' or  rule == 'TOKEN_ELSEIF':
            return  ['<else_clause>']
        elif rule == 'TOKEN_WHILE':
            return  ['<while_loop>']
        elif rule == 'TOKEN_PRINT':
            return  ['<print_statement>']
        elif rule == 'TOKEN_INT' or rule == 'TOKEN_FLOAT' or rule == 'TOKEN_STRINGTYPE':
            return  ['<variable>']
        elif rule == 'TOKEN_ID':
            return  ['<assign_statement>']
        elif rule == 'TOKEN_ID': #if not <assign_statement> will default to <exp>
            return  ['<exp>']
        elif rule == 'TOKEN_NUMBER': 
            return  ['<exp>']
        else:
            raise Exception('Parsing error: Unexpected token {}'.format(rule))

    #get_indices returns a dictionery of the list items(terminal or non-terminal) for the list passed along with it's index)
    def get_indices(input):
        input = list(dict.fromkeys(input))
        indices = {}
        count = 0

        for iA in input:
            indices[iA] = count
            count = count +1

        return indices



