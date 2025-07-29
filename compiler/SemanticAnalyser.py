class SemanticAnalyser(object):
    def type_checker(tokens):
        for index, token in enumerate(tokens):
            if token[0] == 'TOKEN_INT':
                if index < len(tokens) - 1:
                    next_token = tokens[index + 3]
                    
                    if not next_token[1].isdigit():
                        raise Exception(f"Invalid value {token[0]} assigned to integer variable")

            if token[0] == 'TOKEN_FLOAT':
                if index < len(tokens) - 1:
                    next_token = tokens[index + 3]
                    
                    try:
                        float(next_token[1])
                    except ValueError:
                        raise Exception(f"Invalid value {token[0]} assigned to float variable")

            print('Semantic analyser successful!\n')
            return



