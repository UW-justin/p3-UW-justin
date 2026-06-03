import urllib.error, urllib.request, json

# any colons or spaces should be hyphenated

def get_pokemon_data(name):
        baseurl = "https://pokeapi.co/api/v2/pokemon/"
        poke_request = baseurl + name

        try:
            req = urllib.request.Request(poke_request,
                                        headers={'User-Agent': 'Mozilla/5.0'}
                                        )
            response = urllib.request.urlopen(req)
            poke_response_str = response.read().decode()
            poke_data = json.loads(poke_response_str)
        except urllib.error.HTTPError:
             return None
        except urllib.error.URLError:
             return None
        
        return poke_data


def pokemon_types(poke_data):
    poke_types = []
    if len(poke_data["types"]) == 2:
        poke_types.append(poke_data["types"][0]["type"]["name"])
        poke_types.append(poke_data["types"][1]["type"]["name"])
    elif len(poke_data["types"]) == 1:
        poke_types.append(poke_data["types"][0]["type"]["name"])
    else:
         # This should only happen if there was ever a pokemon with 3+ types, which isn't currently in any game
         # It would be a good idea to keep this here in case the game created new mechanics which allowed for it
         # That would be pretty game breaking though ...
         return None
    
    return poke_types


def weakness_calc(poke_types):

    # weakness multiplier calculator
    # weakness[0] -> normal type
    # weakness[1] -> fighting type
    # weakness[2] -> flying type
    # weakness[3] -> poison type
    # weakness[4] -> ground type
    # weakness[5] -> rock type
    # weakness[6] -> bug type
    # weakness[7] -> ghost type
    # weakness[8] -> steel type
    # weakness[9] -> fire type
    # weakness[10] -> water type
    # weakness[11] -> grass type
    # weakness[12] -> electric type
    # weakness[13] -> psychic type
    # weakness[14] -> ice type
    # weakness[15] -> dragon type
    # weakness[16] -> dark type
    # weakness[17] -> fairy type

    weakness = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    types = ["Normal", "Fighting", "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel",
             "Fire", "Water", "Grass", "Electric", "Psychic", "Ice", "Dragon", "Dark", "Fairy"]

    for i in range(len(poke_types)):
        if poke_types[i] == "normal":
            weakness[1] = weakness[1] * 2 # if pokemon is normal type, fighting type (weakness[1]) attacks do 2x damage to them
            weakness[7] = weakness[7] * 0
        elif poke_types[i] == "fighting":
            weakness[2] = weakness[2] * 2
            weakness[13] = weakness[13] * 2
            weakness[6] = weakness[6] * 0.5
            weakness[5] = weakness[5] * 0.5
            weakness[16] = weakness[16] * 0.5
            weakness[17] = weakness[17] * 2
        elif poke_types[i] == "flying":
            weakness[11] = weakness[11] * 0.5
            weakness[12] = weakness[12] * 2
            weakness[14] = weakness[14] * 2
            weakness[1] = weakness[1] * 0.5
            weakness[4] = weakness[4] * 0
            weakness[6] = weakness[6] * 0.5
            weakness[5] = weakness[5] * 2
        elif poke_types[i] == "poison":
            weakness[11] = weakness[11] * 0.5
            weakness[1] = weakness[1] * 0.5
            weakness[3] = weakness[3] * 0.5
            weakness[4] = weakness[4] * 2
            weakness[13] = weakness[13] * 2
            weakness[6] = weakness[6] * 0.5
            weakness[17] = weakness[17] * 0.5
        elif poke_types[i] == "ground":
            weakness[10] = weakness[10] * 2
            weakness[11] = weakness[11] * 2
            weakness[12] = weakness[12] * 0
            weakness[14] = weakness[14] * 2
            weakness[3] = weakness[3] * 0.5
            weakness[5] = weakness[5] * 0.5
        elif poke_types[i] == "rock":
            weakness[0] = weakness[0] * 0.5
            weakness[9] = weakness[9] * 0.5
            weakness[10] = weakness[10] * 2
            weakness[11] = weakness[11] * 2
            weakness[1] = weakness[1] * 2
            weakness[3] = weakness[3] * 0.5
            weakness[4] = weakness[4] * 2
            weakness[2] = weakness[2] * 0.5
            weakness[8] = weakness[8] * 2
        elif poke_types[i] == "bug":
            weakness[9] = weakness[9] * 2
            weakness[11] = weakness[11] * 0.5
            weakness[1] = weakness[1] * 0.5
            weakness[4] = weakness[4] * 0.5
            weakness[2] = weakness[2] * 2
            weakness[5] = weakness[5] * 2
        elif poke_types[i] == "ghost":
            weakness[0] = weakness[0] * 0
            weakness[1] = weakness[1] * 0
            weakness[3] = weakness[3] * 0.5
            weakness[6] = weakness[6] * 0.5
            weakness[7] = weakness[7] * 2
            weakness[16] = weakness[16] * 2
        elif poke_types[i] == "steel":
            weakness[0] = weakness[0] * 0.5
            weakness[9] = weakness[9] * 2
            weakness[11] = weakness[11] * 0.5
            weakness[14] = weakness[14] * 0.5
            weakness[1] = weakness[1] * 2
            weakness[3] = weakness[3] * 0
            weakness[4] = weakness[4] * 2
            weakness[2] = weakness[2] * 0.5
            weakness[13] = weakness[13] * 0.5
            weakness[6] = weakness[6] * 0.5
            weakness[5] = weakness[5] * 0.5
            weakness[15] = weakness[15] * 0.5
            weakness[8] = weakness[8] * 0.5
            weakness[17] = weakness[17] * 0.5
        elif poke_types[i] == "fire":
            weakness[9] = weakness[9] * 0.5
            weakness[10] = weakness[10] * 2
            weakness[11] = weakness[11] * 0.5
            weakness[14] = weakness[14] * 0.5
            weakness[4] = weakness[4] * 2
            weakness[6] = weakness[6] * 0.5
            weakness[5] = weakness[5] * 2
            weakness[17] = weakness[8] * 0.5
            weakness[8] = weakness[17] * 0.5
        elif poke_types[i] == "water":
            weakness[9] = weakness[9] * 0.5
            weakness[10] = weakness[10] * 0.5
            weakness[11] = weakness[11] * 2
            weakness[12] = weakness[12] * 2
            weakness[14] = weakness[14] * 0.5
            weakness[8] = weakness[8] * 0.5
        elif poke_types[i] == "grass":
            weakness[9] = weakness[9] * 2
            weakness[10] = weakness[10] * 0.5
            weakness[11] = weakness[11] * 0.5
            weakness[12] = weakness[12] * 0.5
            weakness[14] = weakness[14] * 2
            weakness[3] = weakness[3] * 2
            weakness[4] = weakness[4] * 0.5
            weakness[2] = weakness[2] * 2
            weakness[6] = weakness[6] * 2
        elif poke_types[i] == "electric":
            weakness[12] = weakness[12] * 0.5
            weakness[4] = weakness[4] * 2
            weakness[2] = weakness[2] * 0.5
            weakness[8] = weakness[8] * 0.5
        elif poke_types[i] == "psychic":
            weakness[1] = weakness[1] * 0.5
            weakness[13] = weakness[13] * 0.5
            weakness[6] = weakness[6] * 2
            weakness[7] = weakness[7] * 2
            weakness[16] = weakness[16] * 2
        elif poke_types[i] == "ice":
            weakness[9] = weakness[9] * 2
            weakness[14] = weakness[14] * 0.5
            weakness[1] = weakness[1] * 2
            weakness[5] = weakness[5] * 2
            weakness[8] = weakness[8] * 2            
        elif poke_types[i] == "dragon":
            weakness[9] = weakness[9] * 0.5
            weakness[10] = weakness[10] * 0.5
            weakness[11] = weakness[11] * 0.5
            weakness[12] = weakness[12] * 0.5
            weakness[14] = weakness[14] * 2
            weakness[15] = weakness[15] * 2
            weakness[17] = weakness[17] * 2            
        elif poke_types[i] == "dark":
            weakness[1] = weakness[1] * 2
            weakness[13] = weakness[13] * 0
            weakness[6] = weakness[6] * 2
            weakness[7] = weakness[7] * 0.5
            weakness[16] = weakness[16] * 0.5
            weakness[17] = weakness[17] * 2
        elif poke_types[i] == "fairy":
            weakness[1] = weakness[1] * 0.5
            weakness[3] = weakness[3] * 2
            weakness[6] = weakness[6] * 0.5
            weakness[15] = weakness[15] * 0
            weakness[16] = weakness[16] * 0.5
            weakness[8] = weakness[8] * 2
    
    four_times = []
    two_times = []
    half_times = []
    zero_times = []
    
    index = 0
    for i in weakness:
        if i != 1:
            if i == 4:
                four_times.append(types[index])
            elif i == 2:
                two_times.append(types[index])
            elif i == 0.5:
                half_times.append(types[index])
            elif i == 0:
                zero_times.append(types[index])
        index = index + 1
    
    weakness_dict = {4: four_times,
                    2:two_times,
                    0.5:half_times,
                    0:zero_times}

    return weakness_dict