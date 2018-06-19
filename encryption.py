alphabet = 'abcdefghijklmnopqrstuvwxyz'
message = input('Enter message >>>')
print('Enter the key for encryption (1 to 26)')
key = int(input())
output = ''
for character in message:
  position = alphabet.find(character)
  newposition = (position + key)%26
  output += alphabet[newposition]

print('The encrypted message is >>>', output)
