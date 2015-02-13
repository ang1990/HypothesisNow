# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 09:42:29 2015

@author: USER
"""

import Typedef

class Parser(object):
    
    operators = ['+', '-', '*', '/']
    brackets = ['(', ')']
    whitespaces = [' ', '\n', '\t']
    commas = ['\"']
       
    # The parse function receives infix expressions and converts them into RPN.
      
    def __init__(self, dataManager = None):
        self.dataManager = dataManager
    
    def verifyExpression(self, stmt):
        tokens = self.collectTokens(stmt)
        error = self.verifyVars(tokens)
        if error:
            return error
        error = self.shuntingYard(list(tokens))
        if type(error) is not None and type(error) is not list:
            return error
        else:
            return None
            
    
    def parse(self, stmt):
        tokens = self.collectTokens(stmt)
        error = self.verifyVars(tokens)
        if error:
            return None
        else:
            return self.shuntingYard(list(tokens))
    
    def shuntingYard(self, tokens):
        operatorStack = []
        outputQueue = []
        for token in tokens:
            if self.isOperator(token):
                while operatorStack:
                    #print(operatorStack)
                    if self.isOperator(operatorStack[-1]):
                        if token == '+' or token == '-':
                            outputQueue.append(operatorStack.pop())
                        elif token == '*' or token == '/':
                            if operatorStack[-1] == '*' or operatorStack[-1] == '/':
                                outputQueue.append(operatorStack.pop())
                            else:
                                break
                    else:
                        break
                operatorStack.append(token)
            elif token == '(':
                operatorStack.append(token)
            elif token == ')':
                while operatorStack:
                    poppedOperator = operatorStack.pop()
                    if poppedOperator == '(':
                        break
                    else:
                        outputQueue.append(poppedOperator)
                        if not operatorStack:
                            return "Error, mismatched parentheses."
            # This can be alphanumeric or anything else. Just catch everything else in case variable names somehow contain
            # unusual characters.
            else:
                outputQueue.append(token)
        while operatorStack:
            outputQueue.append(operatorStack.pop())
            if outputQueue:
                if outputQueue[-1] == '(':
                    return 'Error, too many left parentheses.'
        return outputQueue
    
    # Verify that all variables exist within the data.    
    
    def verifyVars(self, tokens):
        if not self.dataManager:
            return ''
        if not tokens:
            return 'No tokens found.'
        for token in tokens:
            if token[0].isalpha():
                if token not in self.dataManager.getColumnNames():
                    return 'Token: "' + token + '" not found in database.'
                elif self.dataManager.getColType(token) == Typedef.text:
                    return 'Token "' + token + '" cannot be evaluated as it is a text variable.'
                    
        return ''
    
    # This function tokenizes the input expression string, returning the tokenized string as a list of strings.
    
    def collectTokens(self, stmt):
        invertedCommasOn = False
        tokens = []
        newestToken = ''
        for char in stmt:   
    # In case variable names contain special tokens, use inverted commas to denote variable names (For example, "Score - Last Year").
     
            if self.isInvertedCommas(char):
                invertedCommasOn = not invertedCommasOn
                if newestToken:
                    tokens.append(newestToken.strip())
                    newestToken = ''
    # If inverted commas are activated, just add wholesale to the var name.
            elif invertedCommasOn:
                newestToken += char
    # If inverted commas are not on, then we continue normally...
                
            # If the char is a whitespace:
            #   IF the newestToken is an operator or bracket, push it anyway.
            #   Ignore the whitespace since it doesn't belong in the token list.
            #   IF the newestToken is part of a var name, add it to the token.
            #        - All var names will only use normal whitespaces (No \t or \n)
            #          As a result, we will ignore all \t or \n.

                
            elif self.isWhitespace(char):
                if self.isOperator(newestToken) or self.isBracket(newestToken):
                    tokens.append(newestToken)
                    newestToken = ''
                elif char == ' ' and len(newestToken) > 0:
                    newestToken += char
            # If the char is an operator, we've reached a new token.
            # Push newestToken into the list, and replace it with char.
            # Treat brackets the same way.
            elif self.isOperator(char) or self.isBracket(char):
                #print(newestToken)
                if newestToken:
                    tokens.append(newestToken.strip())
                newestToken = char
            # If the char is alphanumeric or a decimal point, it's part of a
            # var name or number token.
            # If the previous token was an operator or bracket, we've reached a new token.
            # Push newestToken into list and replace it with char.
            elif char.isalnum() or char == '.':
                if self.isOperator(newestToken) or self.isBracket(newestToken):
                    tokens.append(newestToken)
                    newestToken = char
                else:
                    newestToken += char
        if newestToken:
            tokens.append(newestToken)
        return tokens
        
    def isInvertedCommas(self, char):
        return char in self.commas        
        
    def isOperator(self, char):
        return char in self.operators
    
    def isBracket(self, char):
        return char in self.brackets
    
    def isWhitespace(self, char):
        return char in self.whitespaces
            
for i in range(5000):
    parser = Parser()
    testString = '0.123 * (Salary Before + Salary After) + After 24 Hours'
    tokens = parser.parse(testString)
    #print(tokens)

                
                
            