import requests

endpoint="http://localhost:8000/apiCandidat/candidats"

def respond(message):
    # Concatenate the user's message to the end of a standard bot respone
    bot_message = "I can hear you! You said: " + message
    # Return the result
    return bot_message

#get_response = requests.get(endpoint,json={'date':'2022-07-20','time_start':'09:00:00','time_end':'10:00:00'})
#print(get_response.status_code)

get_response = requests.post(endpoint,json={'type':'condidat'})
response = get_response.json()

print(response)
