import math

def bold_first_half(string):
    x = len(string)
    # for case 1
    if x < 4:
        y = math.floor(x / 2)
    # for case 2
    else:
        y = math.ceil(x / 2)

    # Creating the output with the first 'y' characters in bold
    bolded_string = "**" + string[:y] + "**" + string[y:]
    return bolded_string

def process_string(input_string):
    # Splitting the string into words
    words = input_string.split()

    # Applying the bold_first_half function to each word
    bolded_words = [bold_first_half(word) for word in words]

    # Joining the words back into a single string with spaces
    output_string = " ".join(bolded_words)
    return output_string

# Test the function
print(process_string("Hi how are you"))
