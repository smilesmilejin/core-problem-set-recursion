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
count = 0
def reverse(text):
    if len(text) == 1:
        return text
    if not text:
        return ""
    
    global count
    
    text_list = list(text)

    if count == len(text) // 2:
        return ''.join(text_list)
    
    temp = text_list[count]
    text_list[count]= text_list[- count - 1]
    text_list[- count - 1] = temp

    count += 1

    return reverse(text_list)

# bunny
def bunny(count):
    if count == 0:
        return 0 

    return bunny(count-1) + 2

# is_nested_parens
def is_nested_parens(parens):
    return calculate_count(parens)

def calculate_count(parens, count=0, index=0):
    if index == len(parens):
        return count == 0
    if count < 0:
        return False
    
    if parens[index] == '(':
        count += 1
    elif parens[index]== ')':
        count -= 1

    return calculate_count(parens, count, index+1)
