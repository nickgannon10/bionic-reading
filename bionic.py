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
string = """Once upon a time, in a small town tucked between the gentle hills, lived a young boy named Liam. He was known for his curiosity and his penchant for exploration, often found with a dirty pair of jeans and a spirit humming with adventure.

One spring afternoon, as the sun painted a golden hue across the town, Liam set out for his daily expedition. Today's destination was the old meadow, a vast expanse of green that was a stone's throw away from his house, yet an area he'd never fully explored.

The meadow was brimming with life, a harmony of dancing butterflies, buzzing bees, and chirping birds. However, what caught Liam's eye was not the typical allure of the meadow but a field of seemingly endless yellow blooms. They looked like a thousand tiny suns, a sea of gold amidst the green."""

print(process_string(string))
