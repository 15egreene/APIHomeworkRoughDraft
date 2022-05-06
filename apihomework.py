from re import A
import requests as r
get_api = r.get("https://pokeapi.co/api/v2/pokemon/")
abilities = r.get("https://pokeapi.co/api/v2/pokemon/ditto/")
if get_api.status_code == 200:
    get_api = get_api.json()
    abilities = abilities.json()
# print(get_api)


# def ability_getter(pokemon_name):
#     ability_list = []
#     api_call = abilities
#     for i in api_call['abilities']:
#         ability_list.append(i['ability']['name'])
#     return ability_list

# print(ability_getter('pikachu'))



# def get_the_name():
#     enrique = []
#     new_api = get_api
#     for i in new_api:
#         enrique.append(i)
#     return enrique

# print(get_the_name())



