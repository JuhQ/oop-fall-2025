try:

    import requests
    import json

    hakusana = "rick and morty"


    url = "https://api.tvmaze.com/search/shows?q=" + hakusana
    url = f"https://api.tvmaze.com/search/shows?q={hakusana}"

    response = requests.get(url)

    print(response)

    json_data = response.json()

    print(json_data)

    show = json_data[0]['show']
    genres = show['genres']

    print(json_data[0])
    print(json_data[0]['show'])
    print(json_data[0]['show']['name'])
    print(json_data[0]['show']['genres'])
    print(json_data[0]['show']['genres'][0])
    print(json_data[0]['show']['genres'][-1])


    print(show)
    print(show['name'])
    print(genres)
    print(genres[0])
    print(genres[-1])

    for data in json_data:
        print(data)

    print(json.dumps(json_data, indent=2))
except requests.exceptions.RequestException as e:
    print("Ollaan virhekäsittelijässä")

print("Juupelis joo ja suoritus jatkuu")