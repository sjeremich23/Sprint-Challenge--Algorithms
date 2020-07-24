'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    total = 0
    # base case: if the word is less than two letters than return total count of "th"
    if len(word) < 2:
        return total

    if word[0] == "t":      # if it finds a t in the word
        # if the next letter is an h than...
        if word[1] == "h":
            total += 1      # update total
            # recall count_th if the next letter is h
            return total + count_th(word[2:])
        else:
            # if letter is not h, recall count_th with the parameters of the next letter
            return count_th(word[1:])
    else:
        # if the first letter is not a t recall count_th to the next letter
        return count_th(word[1:])
