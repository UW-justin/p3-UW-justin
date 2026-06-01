import urllib.error, urllib.request, json

# any colons or spaces should be hyphenated

def get_pokemon_data(name):
        baseurl = "https://pokeapi.co/api/v2/pokemon/"
        poke_request = baseurl + name

        req = urllib.request.Request(poke_request,
                                    headers={'User-Agent': 'Mozilla/5.0'}
                                    )
        response = urllib.request.urlopen(req)
        poke_response_str = response.read().decode()
        poke_data = json.loads(poke_response_str)
        return poke_data


def print_poke_facts(poke_data):
    if poke_data == None:
        return None

    name = poke_data["forms"][0]["name"]
    id = poke_data["id"]
    height = poke_data["height"]

    if len(poke_data["types"]) == 2:
        type_message = "This is a {} and {} type pokemon.".format(poke_data["types"][0]["type"]["name"],poke_data["types"][1]["type"]["name"])
    elif len(poke_data["types"]) == 1:
        type_message = "This is a {} type pokemon.".format(poke_data["types"][0]["type"]["name"])
    else:
        type_message = "This pokemon has more than two types! That's crazy."

    return "balls I love miranda = wife"