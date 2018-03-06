import requests

response = requests.get('https://httpbin.org/ip')

print('Your IP is {0}'.format(response.json()['origin'])+'\n')

response = requests.get('https://anapioficeandfire.com/api/characters/583')
print(response.content + '\n')
print("The name of the character requested is " + response.json()['name'])
print("The character is " + response.json()['gender'])
print("The character's titles:")
for title in response.json()['titles']:
    print title