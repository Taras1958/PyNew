# input_string = "2 неудовлетворительно удовлетворительно хорошо отлично"
# i_s = "1 ужасно неудовлетворительно удовлетворительно прилично отлично"
i_s = input()

# Split the input string into a list of words
words = i_s.split()
print(words, len(words))
d = {int(words[0]): words[1]}

d = {(int(words[0]) + 1): words[2]}
print(d)

# Create a dictionary using dictionary comprehension
# d = {i: w for i, w in enumerate(words, start=2)}
#
# # Display the value with key 4
# print(d[4])
