## Pokemon Game (Python)

### Description

In this project, I will be using Python Classes to create a game system similar to the game Pokemon.

### How it works

I have used Python and the Django framework for this project. This app is not playable and is only printed to the console after the class methods are hard coded into the program. There is no interactivity yet.

### The Program classes are defined in pokemon/pokemon/pokemonapp/models.py. I have used Gitbhub for version control to document each step along with adding comments in the code. Here are the corisponding steps from the program:

001 - To create a pokemon constructor class, I will give it a name, type, and level perameters. Its max health will be determined by its level. I will give it a default level of 5. Its starting health is its max health and it is not knocked out when it starts.

002 - I will use the __repr__ (representation) method to print a string of a created pokemon that interpolates its stats.

003 - Now I will create some class functionality. I will create a method that decreases the Pokémon’s health and a method for regaining health. I will also create a method that will knock out a Pokémon (when its health became 0) and another method to revive a knocked out Pokémon. Each method will show the health score of the pokemon after the method is run and if the health is not zero it will print a string to the console explaining the current health of that Pokemon.

Each method will show the health score of the pokemon after the method is run and if the health is not zero it will print a string to the console explaining the current health of that Pokemon.

Add lose_health() function.

004 - Add gain_health() function.

005 - Add knock_out() function.

006 - Add revive() function.

007 - Create an attack method. This method takes another Pokemon as an argument and deals damage to that Pokemon.

008 - Add three classes that are subclasses of Pokemon. Charmander is a fire type, Squirtle is a Water type, and Bulbasaur is a Grass type.

009 - # Create a trainer, a trainer has a list of pokemon, a number of potions and a name. When the trainer gets created, the first pokemon in their list of pokemons is the active pokemon (number 0)

010 - Create a switch_active_pokemon method.

011 - # Create a use_potion method.

012 - # Create attack_other_trainer method.

013 - Make six pokemon variables that are made with different levels. (If no level is given, it is level 5)

014 - Two trainers are created. The first three pokemon are given to trainer 1, the second three are given to trainer 2.

015 - Testing attacking, giving potions, and switching pokemon.

016 - I would like to add interactivity to the application but it is beyond my skillset at this present time.