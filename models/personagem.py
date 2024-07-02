from random import randint
import requests
import urllib3

urllib3.disable_warnings()

class RandomCharacter:
  random_number = randint(1, 826)
  
  def __init__(self):
    RandomCharacter.sorteio_personagem(self)

  def sorteio_personagem(self):
    random_number = randint(1, 826)
    personagem = requests.get(f"https://rickandmortyapi.com/api/character/{random_number}", verify=False).json()
    self.name =  personagem['name']
    self.status = personagem['status']
    self.specie = personagem['species']
    self.img = personagem ['image']
    return personagem

p1 = RandomCharacter()
print(p1.name)

p1.sorteio_personagem()
print(p1.name)


# def sorteio_personagem():
#   resposta = requests.get(f"https://rickandmortyapi.com/api/character/{randint(1, 826)}", verify=False)
#   return resposta.json()

# personagem = sorteio_personagem()