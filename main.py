import json
import turtle
import urllib.request
import time


def updatescreen():
    urlUpdate = 'http://api.open-notify.org/iss-now.json'
    responseUpdate = urllib.request.urlopen(urlUpdate)
    resultUpdate = json.loads(responseUpdate.read())

    locationUpdate = resultUpdate['iss_position']
    latUpdate = locationUpdate['latitude']
    lonUpdate = locationUpdate['longitude']
    iss.goto(float(lonUpdate), float(latUpdate))
    print('Location Updated')
    time.sleep(5)
    updatescreen()


# for people currently in space
url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print('People in space: ', result['number'])
people = result['people']
for p in people:
    print(p['name'])

# gives new line
print()

# url2 is for iss positioning
url2 = 'http://api.open-notify.org/iss-now.json'
response2 = urllib.request.urlopen(url2)
result2 = json.loads(response2.read())

location = result2['iss_position']
lat = location['latitude']
lon = location['longitude']
print('ISS Position')
print('Longitude: ', lon)
print('Latitude: ', lat)

# setting up screen for gui
screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic("map.gif")

screen.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)

iss.penup()
iss.goto(float(lon), float(lat))

kentLat = 41.18
kentLon = -81.55

locationPoint = turtle.Turtle()
locationPoint.penup()
locationPoint.color('yellow')
locationPoint.goto(float(kentLon), float(kentLat))
locationPoint.dot(5)
locationPoint.hideturtle()


url = 'http://api.open-notify.org/iss-pass.json?lat=41.18&lon=-81.55'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
over = result['response'][1]['risetime']
# print(over)

style = ('Arial', 10, 'bold')
locationPoint.write(time.ctime(over), font=style)

updatescreen()
turtle.mainloop()