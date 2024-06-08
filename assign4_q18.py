#PRAGYA MISHRA 0801IT221158
Str1 = 'they don’t know that we know they know we know'
cleaned_str = Str1.replace("'", "").lower()
words = cleaned_str.split()
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
print("Dictionary with word frequencies:")
print(word_freq)
