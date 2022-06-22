from ursina import *
from random import *
from ursina import curve
import csv
from idk import *

app = Ursina()
camera.orthographic = True
camera.fov = 350
window.fullscreen = True
window.fps_counter.enabled = False
speedbg = 3
speedast = 6
rot = 700
scoreasd = 0
txt = 0
txtd = 0
txta = 0

list_rocket = [""] * 8
list_rocket[0] = r"data\rocket0.png"  # 1 phase
list_rocket[1] = r"data\rocket1.png"  # 2 phase
list_rocket[2] = r"data\rocket2.png"  # 3 phase
list_rocket[3] = r"data\rocket3.png"  # 4 phase
list_rocket[4] = r"data\rocket4.png"  # go forward 1
list_rocket[5] = r"data\rocket5.png"  # go forward 2
list_rocket[6] = r"data\rocket6.png"  # go backward 1
list_rocket[7] = r"data\rocket7.png"  # go backward 2

list_asteroid = [""] * 4
list_asteroid[0] = r"data\asteroid0.png"
list_asteroid[1] = r"data\asteroid1.png"
list_asteroid[2] = r"data\asteroid2.png"
list_asteroid[3] = r"data\asteroid3.png"

rocket = Entity(
    model="quad",
    collibar="box",
    scale=(150, 40),
    hit=True,
    z=0
)

score = Text(
    wordwrap=0.1,
    x=-0.8,
    y=-0.45
)


rocket.collider = 'box'

road1 = Entity(
    model="quad",
    texture=r"data\bg.png",
    collibar="box",
    scale=(1400, 500),
    z=1
)

road2 = duplicate(road1, x=1050)
pair = [road1, road2]

enemies = []


def newEnemy():
    global rot
    asd = randint(-400, 400)
    a = randint(0, 3)
    new = duplicate(
        rocket,
        model="quad",
        rotation_z=0,
        collibar="box",
        texture=list_asteroid[a],
        scale=(40, 40),
        y=asd,
        hit=True,
        x=rot
    )
    enemies.append(new)
    invoke(newEnemy, delay=0.5)


newEnemy()

lasers = []


def newLaser():
    global rocket
    if held_keys["space"]:
        print("sadasd")
        lasers = duplicate(
            rocket,
            y=0,
            x=0,
            model="quad",
            collibar="box",
            scale=(20, 5),
            hit=True,
        )
        lasers.append(lasers)
        invoke(newLaser, delay=0.5)


newLaser()

rocket.x = -100


def update():
    global speedbg, speedast, randast, rocket, enemies, rot, enemy, laser, lasers, list_rocket, list_asteroid, timer, rocketspeedy, rocketspeedx, menu, score, scoreasd, txt, txtd, txta
    timer = 0  # timer
    d = 0  # change rocket textures w
    rocketspeedx = 170
    rocketspeedy = 200

    rand = randint(0, 4)

    speedbg += 0.01  # bg speed ++++
    speedast += 0.001  # asteroid speed ++++
    timer += 0.1  # timer ++++

    score.text = "Счёт: " + str(scoreasd)

    if rocket.x < 100 and held_keys["d"]:
        rocket.x += held_keys["d"] * rocketspeedx * time.dt
        rocket.texture = list_rocket[txtd // 12 + 4]
        txtd = (txtd + 1) % 24
    else:
        rocket.rotation_z = 0

    if rocket.x > -230 and held_keys["a"]:
        rocket.x -= held_keys["a"] * rocketspeedx * time.dt
        rocket.texture = list_rocket[txta // 12 + 6]
        txta = (txta + 1) % 24
    else:
        rocket.rotation_z = 0

    if held_keys["w"]:
        if rocket.y < 150:
            rocket.y += held_keys["w"] * rocketspeedy * time.dt
            rocket.rotation_z = -10
            rocket.texture = list_rocket[txt // 6]
            txt = (txt + 1) % 24
        else:
            rocket.rotation_z = 0

    if held_keys["s"]:
        if rocket.y > -150:
            rocket.y -= held_keys["s"] * rocketspeedy * time.dt
            rocket.rotation_z = 10
            rocket.texture = list_rocket[txt // 6]
            txt = (txt + 1) % 24
        else:
            rocket.rotation_z = 0

    if held_keys["w"] or held_keys["a"] or held_keys["s"] or held_keys["d"]:
        print()
    else:
        rocket.rotation_z = 0
        rocket.texture = list_rocket[txt // 6]
        txt = (txt + 1) % 24

    for enemy in enemies:  # enemies speed
        enemy.x -= 20 * speedast * time.dt
        if enemy.x < -400:
            enemies.remove(enemy)
            destroy(enemy)
            print('111111111')
            scoreasd += 1

    for laser in lasers:  # lasers speed
        laser.x += 20 * time.dt
        if laser.x < 400:
            lasers.remove(laser)
            destroy(laser)

    if Entity.intersects(self=rocket).hit:  # enemy hit rocket || loose
        rocket.shake()
        score = Text(
            text="Вы проиграли",
            x=0,
            y=0
        )
        with open("username.txt", "r") as f:
            username = f.read()
            print(username)
        with open("leaderboard.csv", "a", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writerow({'name': username, 'score': scoreasd})
        quit(10)

    if Entity.intersects(self=enemy).hit:  # delete excess enemies
        enemies.remove(enemy)
        destroy(enemy)

    for road in pair:
        road.x -= speedbg * time.dt
        if road.x < -700:
            road.x += 2100

    sys.stdout.write(str(score))


app.run()
