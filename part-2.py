# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if len(array) == 0:
        return False
    
    if array[0] == query:
        return True
    
    return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    if len(text) == 0 or len(text) == 1:
        return True
    
    if text[0] != text[-1]:
        return False
    
    return is_palindrome(text[1:-1])


# digit_match
def digit_match(num1, num2):
    return calculate_match(num1, num2)

def calculate_match(num1, num2, match=0):
    if (num1 % 10 == num1) or (num2 % 10 == num2):
        if num1 % 10 == num2 % 10:
            match += 1
        return match      
    
    if num1 % 10 == num2 % 10:
        match += 1
    
    return calculate_match(num1 // 10, num2 // 10, match)


