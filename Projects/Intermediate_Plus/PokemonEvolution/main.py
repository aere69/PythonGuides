# https://challenges.hackajob.co/pokeapi/docs/v2/#pokemon-species

import requests

class Pokemon:

    def Evolutions(self,pokemonName):
        r = requests.get(f"https://challenges.hackajob.co/pokeapi/api/v2/pokemon-species/{pokemonName}/")

        pokemon = r.json()
        evo_chain_url = pokemon["evolution_chain"]["url"]

        r = requests.get(evo_chain_url)
        evolution_chain = r.json()
        evolution_chain = evolution_chain["chain"]

        evolution_items = []

        while evolution_chain:
            evolution_name = evolution_chain["species"]["name"]
            evolution = {"name":evolution_name, "chain":[]}
            evolution_items.append(evolution)
            next_evolution = evolution_chain["evolves_to"]
            if next_evolution:
                evolution_chain = next_evolution[0]
            else:
                evolution_chain = []

        return evolution_items
    
    def Evolution(self,pokemonName):
        evolutions = self.Evolutions(pokemonName)
        idx = len(evolutions)-1
        while idx > 0:
            evolutions[idx-1]["chain"].append(evolutions[idx])
            idx -= 1

        return evolutions[0]
    
    def EvolutionNames(self,pokemonName):
        evolutions = self.Evolutions(pokemonName)
        names = []
        for i in range(0,len(evolutions)):
            names.append(evolutions[i]["name"])
        return names



pokemon = Pokemon()
print(pokemon.Evolution("caterpie"))
print(pokemon.Evolution("squirtle"))
print(pokemon.Evolution("bulbasaur"))
print(pokemon.Evolution("charizard"))

print(pokemon.EvolutionNames("caterpie"))
print(pokemon.EvolutionNames("squirtle"))
print(pokemon.EvolutionNames("bulbasaur"))
print(pokemon.EvolutionNames("charizard"))

