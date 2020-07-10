# keep track of the Pokémon’s name, level, type, maximum health, current health, and whether or not the Pokémon was knocked out.
class Pokemon:
  # initialize specs about Pokemon
  def __init__(self, name, level, type):
    self.name = name
    self.level = level
    self.health = level
    self.max_health = level
    self.type = type
    self.is_knocked_out = False
  
  # string representation
  def __repr__(self):
    return "Pokemon: {name}, level: {level}, type: {type}".format(name = self.name, level = self.level, type = self.type)

  # decreases Pokemon's health
  def lose_health(self, health):
    self.health -= health
    print("{name} now has {health} health".format(name=self.name, health = self.health))

    if(self.health==0):
      knock_out()
  
  # knock out Pokemon
  def knock_out(self):
    self.is_knocked_out = True
    print("{name} is knocked out!".format(name=self.name))

  # revives Pokemon by health
  def gain_health(self, health):
    self.health += health
    print("{name} now has {health} health".format(name=self.name, health = self.health))
  
  # revive a knocked out Pokemon
  def revive(self):
    self.is_knocked_out = False
    self.health = self.max_health

    print("{name} is revived!".format(name=self.name))

  # takes another Pokémon as an argument and deals damage to that Pokémon
  def attack(self, other_pokemon):

    # check if attacker is knocked out
    if(self.is_knocked_out == True):
      print("{name} is knocked out! Can not attack".format(name = self.name))
      return 

    # attacker advantage cases
    if((self.type == "water" and other_pokemon.type == "fire") or (self.type == "fire" and other_pokemon.type == "grass")):
      # damage = twice the attacker's level 
      damage = self.level*2
      other_pokemon.lose_health(damage)
      print("{name} defeated {other}!".format(name=self.name, other = other_pokemon.name))

    # attacker disadvantage cases
    if((self.type == "fire" and other_pokemon.type == "water") or (self.type == "grass" and other_pokemon.type == "fire")):
      # damage = half the attacker's level 
      damage = self.level/2
      self.lose_health(damage)
      print("{other} defeated {name}!".format(name=self.name, other = other_pokemon.name))


# A Trainer can have up to 6 Pokémon, which we stored in a list. A trainer also has a name, and a number of potions they can use to heal their Pokémon. A trainer also has a “currently active Pokémon”, which we represented as a number.
class Trainer:
  def __init__(self, name, potions, current_pokemon, *pokemons):
    self.name = name
    self.pokemons = pokemons
    self.potions = potions
    self.current_pokemon = current_pokemon

  # trainer is able to use a potion and attack another trainer. When a potion is used, it heals the trainer’s currently active Pokémon. when a trainer attacks another trainer, the currently active Pokémon deals damage to the other trainer’s current Pokémon.
  def attack_other_trainer(self, other_trainer):
    # heals trainer's Pokemon
    if(self.potions>0):
      self.potions -= 1
      self.health = self.max_health
    
    # determine the other trainer's pokemon
    other_pokemon = other_trainer.pokemons[other_trainer.current_pokemon]

    # attack pokemon
    print("{name} attacks {other}!".format(name=self.name, other = other_trainer.name))

    self.pokemon[self.current_pokemon].attack(other_pokemon)

  # switch active Pokemon
  def switch_pokemon(self, new_pokemon):
    # deal with pokemon passed as string or int
    current_pokemon = new_pokemon
    
    # this code is not working!
    if(type(current_pokemon) == type(str)):
      for pokemon in self.pokemons:
        if(current_pokemon == pokemon.name):
          current_pokemon = self.pokemons.index(pokemon)
          break

      # index not found
      if(type(current_pokemon) == type(str)): 
          print("Pokemon is not in list")
          return

    # checks if pokemon is knocked out
    if(self.pokemons[current_pokemon].is_knocked_out):
      print("{name} is knocked out! Can not switch".format(name = self.pokemons[current_pokemon]))
      return

    self.current_pokemon = current_pokemon

    print("{name}'s active pokemon is now {pokemon}".format(name=self.name, pokemon = self.pokemons[self.current_pokemon]))

# testing!
class Test_trainer:
  def __init__(self, trainer):
    self.trainer = trainer

  def print_trainer(self):
    # prints initial status
    print(self.trainer.name)
    print(self.trainer.potions)
    print(self.trainer.pokemons)
    print(self.trainer.pokemons[self.trainer.current_pokemon])

class Test_pokemon:
  def __init__(self, pokemon):
    self.pokemon = pokemon

  def print_pokemon(self):
    # prints initial status
    print(self.pokemon.name)
    print(self.pokemon.type)
    print(self.pokemon.level)
    print(self.pokemon.max_health)
    print(self.pokemon.health)
    
pokemon1 = Pokemon("Pikkachu", 6, "fire")
pokemon2 = Pokemon("Eevee", 5, "grass")
trainer_one = Trainer("Anika", 5, 0, pokemon1, pokemon2)

test_trainer1= Test_trainer(trainer_one)
test_trainer1.print_trainer()

test_pok1 = Test_pokemon(pokemon1)
test_pok1.print_pokemon()
test_pok2 = Test_pokemon(pokemon2)
test_pok2.print_pokemon()

pokemon2.attack(pokemon1)
test_pok2.print_pokemon()

trainer_one.switch_pokemon("Eevee")
