# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError('The input n must be greater than or equal to 0')
    
    if n == 0:
        return 1
    
    return n * factorial(n-1)

# reverse
def reverse(text, output_text="", index=-1):
    if index == - len(text)- 1:
        return output_text
    
    output_text = output_text + text[index]

    return reverse(text, output_text, index-1)

# bunny
def bunny(count):
    if count == 0:
        return 0 

    return bunny(count-1) + 2

# is_nested_parens
def is_nested_parens(parens,count=0):
    if not parens:
        return count == 0
    if count < 0:
        return False
    if parens[0] == '(':
        return is_nested_parens(parens[1:], count+1)
    elif parens[0]== ')':
        return is_nested_parens(parens[1:], count-1)
