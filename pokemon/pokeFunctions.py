import requests

def pega_pokemon(id_usuario: str):
    url = f"https://pokeapi.co/api/v2/pokemon/{id_usuario}"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()

        poke_data = resposta.json()

        nome = poke_data["name"]
        habilidades = _monta_abilities(poke_data["abilities"])

        return {"pokemon": nome, "habilidades": habilidades}

    except requests.exceptions.HTTPError as http_err:
        print(http_err)

def _monta_abilities(abilities: list) -> list:
    urls = []
    resposta = {}

    for ability in abilities:
        urls.append(ability["ability"]["url"])

    for url in urls:
        lista_nomes = []
        lista_efeitos = []
        lista_flavor = []
        lista_pokemons = []
        
        response = requests.get(url)
        ability_data = response.json()

        ability_name = ability_data["name"]

        # Nomes
        for nomes in ability_data["names"]:
            lista_nomes.append((nomes["name"], nomes["language"]["name"]))

        # Efeitos
        for efeitos in ability_data["effect_entries"]:
            if efeitos["language"]["name"] == "en":
                lista_efeitos.append(efeitos["short_effect"])
                break

        # Flavors
        for flavor in ability_data["flavor_text_entries"]:
            if flavor["language"]["name"] == "en":
                lista_flavor.append(flavor["flavor_text"].replace('\n', '').strip())
                break

        # Pokemons
        for pokemon in ability_data["pokemon"]:
            lista_pokemons.append(pokemon["pokemon"]["name"])

        resposta[ability_name] = {
            "nomes": lista_nomes,
            "efeitos": lista_efeitos,
            "flavors": lista_flavor,
            "pokemons": lista_pokemons
        }
    
    return resposta
