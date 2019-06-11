word = input("Input a sentence to reverse: ")

for char in range(split(len(word) - 1, -1, -1)):
  print(word[char], end="")
