import pgzrun
import random
HEIGHT  = 700
WIDTH = 1000
player=Actor("ufo1")
player.x = 90
player.y = HEIGHT//2
player.frame=2
tick=Actor("tick")
tick.x=405
tick.y=375
tick1=Actor("tick")
tick1.x=700
tick1.y=375
triple_bullet=Actor("power_bullet")
triple_bullet.top=0
triple_bullet.left=random.randint(0,WIDTH-400)
final_score=0
level_reached=0
score=0
level='0'
bullets=[]
bullets1=[]
asteroids=[]
lives=[]
game_over = False
level_failed=False
level_display=False
tom=False
jerry=False
spacemusic1=True
power_enabled=False
Colour=(255, 0, 102)
def draw():
    global score,level,level_display,spacemusic1,final_score,level_reached,asteroids,power_enabled
    if game_over and not level_failed:
        screen.clear()
        screen.blit("bg1",(0,0))
        screen.draw.text(str(high_score),(865,20),fontsize=90,color=(255, 191, 0))
        if not tom:
            tick.draw()
        if tom:
            tick1.draw()
        power_enabled=False
    if game_over and level_failed:
        score=0
        level='0'
        screen.clear()
        screen.blit("bg",(0,0))
        screen.draw.text(str(high_score),(WIDTH-250,15),fontsize=90,color='blue')
        screen.draw.text(str(final_score),(WIDTH-250,111),fontsize=90,color='blue')
        screen.draw.text(str(level_reached),(WIDTH-340,185),fontsize=90,color='blue')
        asteroids=[]
        power_enabled=False
        triple_bullet.image="power_bullet"
    if not game_over:
        screen.clear()
        screen.blit("background3",(0,0)) 
        player.draw() 
        screen.draw.text("SCORE : "+str(score),(WIDTH-200,10),fontsize=30,color='white')
        screen.draw.text("LEVEL : "+str(level),(WIDTH-200,50),fontsize=30,color='white')
        if level_display:
            i=0
            while i<10:
                screen.draw.text("level  "+str(int(level)-1)+"  completed",(250,50),fontsize=60,color='red')
                i+=1
            level_display=False
        for bullet in bullets:
            bullet.draw()
        for asteroid in asteroids:
            asteroid.draw()
        for life in lives:
            life.draw()
        if score>=10:
            triple_bullet.draw()
        final_score=score
        level_reached=level
def update():
    global game_over,level_failed,player,high_score,level,level_display,spacemusic1,asteroids
    if game_over and not level_failed:
        sounds.spacemusic.play()
        triple_bullet.image="power_bullet"
    if not game_over:
        sounds.spacemusic.stop()
        move_player()
        player_boundary()
        move_bullet()
        move_asteroid()
        animate_player(player)
        player_asteroid_collision()
        if score != 0:
            if (score%10)==0:
                l=str(score)
                level=str(l[:-1])
                level_display=True
                power_bullet_collision()
                move_power_bullet()
        if len(asteroids)<int(level)+1:
            create_asteroids()

        if len(bullets) != 0:
            bullet_collision()
        if len(lives)==0:
            game_over=True
            level_failed=True
            create_life()
            player.x = 90
            player.y = HEIGHT//2
            player.frame=2
    f=open("c:/Users/AJAY SHARON/.spyder-py3/programmingclub/jerry/high_score.txt",'r')
    high_score=int(f.read())
    f.close()
    if high_score < score:
            f=open("c:/Users/AJAY SHARON/.spyder-py3/programmingclub/jerry/high_score.txt",'w')
            f.write(str(score))
            f.close()
def on_key_down(key):
    global game_over,level_failed,player,tom
    if game_over and not level_failed:
        if keyboard.t==True:
            tom=True
        if keyboard.j==True:
            tom=False
    if game_over and level_failed:
        if keyboard.h==True:
            level_failed = False
    if game_over:
        if key == keys.SPACE:
            game_over=False
    if not game_over:
        if key == keys.SPACE:
            create_bullet()
def move_power_bullet():
     triple_bullet.y += 5           
def power_bullet_collision():
    global power_enabled
    if player.colliderect(triple_bullet):
        triple_bullet.image="blank"
        triple_bullet.y += 5  
        power_enabled=True
def move_asteroid():
    for asteroid in asteroids:
        asteroid.x -= 5
        if asteroid.right < 0:
            asteroids.remove(asteroid)
            if len(lives) != 0:
                lives.pop()
def move_player():
    if keyboard.left:
        player.x -= 10
    if keyboard.right:
        player.x += 10
    if keyboard.up:
        player.y -= 10
    if keyboard.down:
        player.y += 10
def animate_player(player):
    if tom:
        if True:
            player.image="ufo{}".format(player.frame)
        player.frame+=1
        if player.frame > 24:
            player.frame=16
    if not tom:
        if True:
            player.image ="ufo{}".format(player.frame)
        player.frame+=1
        if player.frame >=9:
            player.frame=2
def player_boundary():
    if player.left<0:
        player.left=0
    if player.right>WIDTH:
        player.right=WIDTH
    if player.top<0:
        player.top=0
    if player.bottom>HEIGHT:
        player.bottom=HEIGHT
def create_bullet():
    sounds.bulletsound.play()
    bullet=Actor("bullet")
    bullet.x = player.right+25
    bullet.y = player.y
    bullets.append(bullet)
    if power_enabled:
        bullet=Actor("bullet")
        bullet.x = player.right+25
        bullet.y = player.y+25
        bullets.append(bullet)
        bullet=Actor("bullet")
        bullet.x = player.right+25
        bullet.y = player.y-25
        bullets.append(bullet)
def create_asteroids():
    asteroid=Actor("asteroid1")
    asteroid.right=WIDTH
    asteroid.y =random.randint(100,HEIGHT-100)
    asteroids.append(asteroid)
    asteroid.frame=1
def animate_asteroid(asteroid):
    if True:
        asteroid.image ="asteroid{}".format(asteroid.frame)
    asteroid.frame+=1
    if asteroid.frame > 30:
        asteroid.frame=1
def create_life():
    for i in range(3):
        life=Actor("life")
        life.left = i * 80
        life.top=0
        lives.append(life)
def move_bullet():
    for bullet in bullets:
        if bullet.left > WIDTH:
            bullets.remove(bullet)
        else:
            bullet.x += 10
def player_asteroid_collision():
    for asteroid in asteroids:
        animate_asteroid(asteroid)
        if player.colliderect(asteroid):
            asteroids.remove(asteroid)
            if len(lives) != 0:
                lives.pop()
def bullet_collision():
    global score
    for bullet in bullets:
        for asteroid in asteroids:
            if bullet.colliderect(asteroid):
                score +=1
                bullets.remove(bullet)
                asteroids.remove(asteroid)
    if len(asteroids)==0:
        create_asteroids()
create_life()
create_asteroids()
pgzrun.go()