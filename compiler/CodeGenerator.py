class CodeGenerator(object):
    def generate_code(tokens):
        code = ''
        indent_level = 0
        if_counter = 0
        inside_while = False
        skip_semicolon = False
        for i, (token_type, token_value) in enumerate(tokens):
            if token_type == 'TOKEN_IF':
                code += 'IF '
                if_counter += 1
            elif token_type == 'TOKEN_WHILE':
                code += 'WHILE '
                inside_while = True
            elif token_type == 'TOKEN_ID':
                if skip_semicolon:
                    skip_semicolon = False
                else:
                    code += token_value + ' '
            elif token_type == 'TOKEN_GT':
                code += '> '
            elif token_type == 'TOKEN_LT':
                code += '< '
            elif token_type == 'TOKEN_NUMBER':
                code += token_value + ' '
            elif token_type == 'TOKEN_STRING':
                code += token_value + '\n'
            elif token_type == 'TOKEN_ELSEIF':
                code += '\t' * indent_level + 'ELSE IF '
                if_counter += 1
            elif token_type == 'TOKEN_ELSE':
                code += '\t' * indent_level + 'ELSE\n\t'
            elif token_type == 'TOKEN_INT':
                code += 'INTEGER '
            elif token_type == 'TOKEN_FLOAT':
                code += 'FLOAT '
            elif token_type == 'TOKEN_PLUS':
                code += '+ '
            elif token_type == 'TOKEN_MINUS':
                code += '- '
            elif token_type == 'TOKEN_DIV':
                code += '/ '
            elif token_type == 'TOKEN_MULT':
                code += '* '
            elif token_type == 'TOKEN_ATTR':
                code += '= '
                skip_semicolon = True
            elif token_type == 'TOKEN_RBRACKET':
                code += '\n\t'
            elif token_type == 'TOKEN_PRINT':
                code += 'PRINT '
            elif token_type == 'TOKEN_PCOMMA':
                code = code.rstrip()
                code += '\n'
            elif token_type == 'TOKEN_RBRACE':
                indent_level -= 1
                if inside_while:
                    code += '\t' * indent_level + 'END WHILE'
                    inside_while = False
                else:
                    if_counter -= 1
                    try:
                        if tokens[i + 1][1] is not 'else' and tokens[i + 1][1] is not 'else':
                            continue
                    except IndexError:
                        code += '\t' * indent_level + 'END IF'
        
        print('The generated code is:\n')
        print(code)

