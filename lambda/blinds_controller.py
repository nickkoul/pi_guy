def blinds_handler(event, context):
    angle = event["angle"]
    url = "http://10.0.0.130:5000/blinds/" + str(angle)
    response = requests.get(url)
    return response
