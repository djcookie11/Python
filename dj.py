import webbrowser as wb
import pyautogui as pg
import time as t
points = 0
show = pg.prompt ("What is your favorite tv show? ")
if show == "Spongebob":
    pg.alert (" Your favorite show is " + show)             
    points += 5
    t.sleep(2)
    wb.open("https://www.youtube.com/watch?v=GK00aC7gJaE")
elif show == "Tom and Jerry":
    pg.alert (" Your favorite ahow is " + show)
    points += 10
    t.sleep(2)
    wb.open("https://www.youtube.com/watch?v=PLLqGbPvXSM")
elif show == "Family Guy" :
    pg.alert ("Love that show!")
    points += 5
    t.sleep(2)
    wb.open ("https://en.wikipedia.org/wiki/Family_Guy")
elif show == "American Dad" :
    pg.alert ("Terrible show")
    points -= 5
    t.sleep(2)
    wb.open ("https://en.wikipedia.org/wiki/Family_Guy")
elif show == "Barbie Life in the Dream house" :
    pg.alert ("Really, horrible show")
    points -= 5
    t.sleep(2)
    wb.open ("https://www.netflix.com/title/70294800")
else:
    pg.alert (" Your favorite show is " + show)
    points += 5

food = pg.prompt (" What is your favorite food")

if food == "Sushi":
    pg.alert (" Sweet")
    points += 5
    t.sleep(2)
    wb.open("https://halfoff.adspayusa.com/product/lins-little-china-sushi-lhc/")
elif food == "pasta":
    pg.alert (" Same!")
    points += 5
    t.sleep(2)
    wb.open("https://thestayathomechef.com/pasta-pomodoro/")
elif food == "pizza":
    pg.alert (" I like that too")
    points += 5
    t.sleep(2)
    wb.open("https://store.cincyfavorites.com/larosas-cheese-pizza-p599.aspx")
elif food == "hot dog" :
    pg.alert ("nice")
    points += 5
    t.sleep(2)
    wb.open ("https://leitesculinaria.com/96037/recipes-the-best-hot-dog.html")
elif food == "cheeseburger" :
    pg.alert ("awesome")
    points += 5
    t.sleep(2)
    wb.open ("https://en.wikipedia.org/wiki/Cheeseburger")
elif food == "tacos" :
    pg.alert ("cool")
    points += 5
    t.sleep(2)
    wb.open ("https://www.inspiredtaste.net/36140/ground-pork-tacos-recipe/")
else:
    pg.alert (" Your favorite show is " + food)
    points += 5


dessert = pg.prompt ("What is your favorite dessert? ")

if dessert == " funnel cake" :
    pg.alert (" Or choclate cake?")
    points += 5
    t.sleep(2)
    wb.open("https://www.youtube.com/watch?v=y4xqIWxa0Kc")
elif dessert == "Funnel cake":
    pg.alert (" Thats disgusting")
    points -= 5
    t.sleep(2)
    wb.open("https://www.youtube.com/watch?v=2Ivrbs-iCHk")
elif dessert == " Vanilla ice cream":
    pg.alert ("Same, except I like chocolate")
    points += 3
    t.sleep(2)
    wb.open("https://www.youtube.com/watch?v=vEqrnE7XRHk")
elif dessert == "Chocolate cookies" :
    pg.alert ("Ooooooooooh")
    points += 5
    t.sleep(2)
    wb.open("https://www.handletheheat.com/bakery-style-chocolate-chip-cookies/")
elif dessert == "Brownies" :
    pg.alert ("ugh")
    points -= 5
    t.sleep(2)
    wb.open("https://smittenkitchen.com/2012/08/my-favorite-brownies/")
elif dessert == "Applie pie" :
    pg.alert ("yummy!!!!!!!!!!!!!!!")
    points += 5
    t.sleep(2)
    wb.open("https://www.tasteofhome.com/recipes/apple-pie/")
        
else:
    pg.alert (" Your favorite dessert is " + dessert)
    points += 5
    
SpaceJam = pg.prompt (" Who is your favorite character in Space Jam? ")

if SpaceJam == "Yosemite" :
    pg.alert (" Nice")
    points += 5
    t.sleep(2)
    wb.open("https://www.youtube.com/watch?v=ENXZJ4-WtrM")
elif SpaceJam == "Daffy Duck" :
    pg.alert ("Awesome")
    points += 5
    t.sleep(2)
    wb.open ("https://www.youtube.com/watch?v=O5qLMuXylgU")
elif SpaceJam == "Foghorn Leghorn" :
    pg.alert ("Sweet")
    points += 5
    t.sleep(2)
    wb.open("https://www.youtube.com/watch?v=xcsODn_IeC0")
elif SpaceJam == "M. Martian" :
    pg.alert ("cool")
    points += 5
    t.sleep(2)
    wb.open ("https://en.wikipedia.org/wiki/Marvin_the_Martian")
elif SpaceJam == "Bugs" :
    pg.alert ("Love to see it")
    points += 5
    t.sleep(2)
    wb.open ("https://www.youtube.com/watch?v=Z7ay9YX6KKE")
elif SpaceJam == "Tweetie" :
    pg.alert ("Gotta love it")
    points += 5
    t.sleep(2)
    wb.open ("https://www.youtube.com/watch?v=ZtdP7r1kqNw")
else:
    pg.alert ("Your favorite Space Jam character is" + SpaceJam)
    points += 5

FamilyGuy = pg.prompt (" Who is your favorite character in Family Guy")

if FamilyGuy == "Peter" :
    pg.alert (" Hehehe")
    points += 5
    t.sleep(2)
    wb.open("https://www.youtube.com/watch?v=1JTL3DP5E8o")
elif FamilyGuy == "Lois" :
    pg.alert ("Terrible character")
    points -=5
    t.sleep(2)
    wb.open("https://www.youtube.com/watch?v=1JTL3DP5E8o")
elif FamilyGuy == "Brian" :
    pg.alert ("Agreed")
    points += 5
    t.sleep(2)
    wb.open("https://www.youtube.com/watch?v=oY7la9xbxuI")
elif FamilyGuy == "Meg" :
    pg.alert ("Enough is enough")
    points += 5
    t.sleep(2)
    wb.open("https://www.youtube.com/watch?v=zHhZ19_BJYU")
elif FamilyGuy == "Chris" :
    pg.alert ("Yeah, he is funny")
    points += 5
    t.sleep(2)
    wb.open("https://www.youtube.com/watch?v=UsbgiQsy-PA")
elif FamilyGuy == "Steewie" :
    pg.alert ("He's the BEST")
    points +=50
    t.sleep(2)
    wb.open("https://www.youtube.com/watch?v=LhnRHOYRncc")
else:
    pg.alert ("Your favorite Family Guy character is" + FamilyGuy)
    points += 5

pg.alert ("You scored: ")
pg.alert (points)
    
    
