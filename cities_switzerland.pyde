import csv

citiesData = None

einwohner = 10

def setup():
    global citiesData
    size(900, 600)
    citiesFileHandle = open("cities.csv")
    citiesData = list(csv.DictReader(citiesFileHandle))
    background(0, 0, 0)
            
def draw():
    global einwohner
    for row in citiesData:
        lat = float(row["lat"])
        lng = float(row["lng"])
        population = row["population"]
        ortXY(lat, lng, population)
        print (population)
                                    
def ortXY(lat, lng, population):
    x = 80 + (5.9789 - lng) * -180
    y = ((47.7493 - lat) * 200) + 100
    fill (mouseX/3, mouseX/2 ,mouseY)
    circle (x, y, 7)
    

    

"""ellipse (x, y, (5.9789 - lng) * 4, (47.7493 - lat) * 4)"""
"""ellipse (x, y, 4, 4)"""
"""if population >= 5000:"""
"""else rect (10, 10, 4, 4)"""
"""textSize(50)"""
"""text(mouseX, mouseX, mouseY)"""
""""""
""""""
     
