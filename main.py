"""
Interesting artpiece randomly generated each time.

author: <Hosun and Aarsh>
date:  <12/5/2024>
course: ICS3UC

"""

import pygame
import random
import time

# Model

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PINK = (255, 192, 203)
BLUE = (0, 0, 200)
blue = (0, 0, 255)
SKYBLUE = (103, 200, 255)
PURPLE = (128, 0, 128)
YELLOW = (255, 255, 0)
BEIGE = (220, 201, 170)
DARKBEIGE = (217, 179, 130)
WALL = (233, 237, 185)
BROWN = (200, 170, 90)
FILE = (252, 242, 124)

import os

# Change the working directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))


pygame.init()

# Set the width and height of the screen [width, height]
size = (2000, 1000)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Scene initialization
scene = 0

# fonts
font = pygame.font.Font(None, 50)
fontH = pygame.font.SysFont("comicsansms", 160)
fontF = pygame.font.SysFont("cosmicsansms", 30)
fontF1 = pygame.font.SysFont("cosmicsansms", 25)
fontF2 = pygame.font.SysFont("cosmicsansms", 20)

# text
hallMoniter = fontH.render("Hall Monitor", True, BLACK)
play = font.render("Play", True, BLACK)

Easy = font.render("Easy", True, BLACK)
Medium = font.render("Medium", True, BLACK)
Hard = font.render("Hard", True, BLACK)

# images
# heart = pygame.image.load("heart.png").convert()
# heart = pygame.transform.scale(heart, (300, 300))
# heart.set_colorkey(blue)

def menuScene():
    screen.fill(SKYBLUE)
    pygame.draw.rect(screen, BEIGE, [300, 100, 1390, 800])
    screen.blit(hallMoniter, [540, 120])

    screen.blit(play, [965, 400])
    pygame.draw.rect(screen, BLACK, [830, 350, 350, 150], 5)


def scene1():
    screen.fill(BLUE)


# person lists

personNameList = ["Jerry", "Aryan", "Jordan", "Ram", "Daniel", "Jayden", "Brandon", "Jorvin", "Ben",
                  "Joshua", "Zain", "Alyssa", "Navyaa", "Nayalie", "Anikka"]

isGeneratedPerson = False


def difficultyScreen():
    screen.fill(BEIGE)
    pygame.draw.rect(screen, GREEN, [800, 150, 400, 200])
    pygame.draw.rect(screen, BLACK, [800, 150, 400, 200], 1)
    screen.blit(Easy, [955, 240])
    pygame.draw.rect(screen, YELLOW, [800, 400, 400, 200])
    pygame.draw.rect(screen, BLACK, [800, 400, 400, 200], 1)
    screen.blit(Medium, [935, 490])
    pygame.draw.rect(screen, RED, [800, 650, 400, 200])
    pygame.draw.rect(screen, BLACK, [800, 650, 400, 200], 1)
    screen.blit(Hard, [955, 740])


def gameScene(name, grade, time, correct, attendance, attendance2, daycounter, livecounter, day):
    screen.fill(WALL)
    image = pygame.image.load(str(person.name) + ".png").convert()
    image.set_colorkey(BLACK)
    screen.blit(image, [700,140])
    pygame.draw.polygon(screen, BROWN, [[0, 650], [600, 550], [1400, 550], [2000, 650]])
    pygame.draw.polygon(screen, BLACK, [[0, 650], [600, 550], [1400, 550], [2000, 650]], 5)
    pygame.draw.rect(screen, BROWN, [0, 645, 2000, 145])
    pygame.draw.line(screen, BLACK, [0, 700], [2000, 700], 5)
    pygame.draw.line(screen, BLACK, [0, 790], [2000, 790], 5)
    if fileUp == False:
        for i in range(fileNum):
            pygame.draw.polygon(screen, FILE,
                                [[300, 610 - 5 * i], [610, 560 - 5 * i], [750, 565 - 5 * i], [520, 620 - 5 * i]])
            pygame.draw.polygon(screen, BLACK,
                                [[300, 610 - 5 * i], [610, 560 - 5 * i], [750, 565 - 5 * i], [520, 620 - 5 * i]], 2)
    elif fileUp == True and fileNum > 0:
        for i in range(fileNum - 1):
            pygame.draw.polygon(screen, FILE,
                                [[300, 610 - 5 * i], [610, 560 - 5 * i], [750, 565 - 5 * i], [520, 620 - 5 * i]])
            pygame.draw.polygon(screen, BLACK,
                                [[300, 610 - 5 * i], [610, 560 - 5 * i], [750, 565 - 5 * i], [520, 620 - 5 * i]], 2)
        pygame.draw.rect(screen, FILE, [300, 450, 300, 400])
        pygame.draw.rect(screen, BLACK, [300, 450, 300, 400], 3)
        screen.blit(name, [330, 470])
        screen.blit(time, [330, 510])
        if day > 1:
            screen.blit(grade, [330, 540])
        if day > 3:
            screen.blit(attendance, [330, 570])
            screen.blit(attendance2, [330, 587])

    lives = fontF.render("Lives", True, BLACK)
    screen.blit(correct, [1500, 800])
    screen.blit(daycounter, [950, 200])
    screen.blit(lives, [300, 800])
    xIncrement = 0
    # for i in range(livecounter):
    #     screen.blit(heart, [220+xIncrement*25, 630])
    #     xIncrement+=1

    pygame.draw.rect(screen, FILE, [1400, 15, 500, 300])
    pygame.draw.rect(screen, BLACK, [1400, 15, 500, 300], 2)
    textControls = fontF.render("Controls", True, BLACK)
    textF = fontF2.render("F: Open top file", False, BLACK)
    textY = fontF2.render("Y: Vote yes for skipping", False, BLACK)
    textN = fontF2.render("N: Vote no for not skipping", False, BLACK)

    textSKIPPINGGUIDE = fontF.render("Hall Monitor Guide", True, BLACK)
    textRULE1 = fontF2.render("1. Normal students are back in class within 10 minutes", False, BLACK)
    if day > 1:
        textRULE2 = fontF2.render("2. Normal students have at least a 65 average", False, BLACK)
        textRULE3 = fontF2.render("3. If either rule 1 or rule 2 is broken, that student is skipping", False, BLACK)
    if day > 3:
        textRULE3 = fontF2.render("3. Normal students are absent 2 days at most", False, BLACK)
        textRULE4 = fontF2.render("4. Normal students don't break more than 2 of those rules", False, BLACK)



    screen.blit(textControls, [1410, 30])
    screen.blit(textF, [1410, 50])
    screen.blit(textY, [1410, 70])
    screen.blit(textN, [1410, 90])

    screen.blit(textSKIPPINGGUIDE, [1410, 130])
    screen.blit(textRULE1, [1410, 150])
    if day > 1:
        screen.blit(textRULE2, [1410, 170])
        screen.blit(textRULE3, [1410, 190])
    if day > 3:
        screen.blit(textRULE3, [1410, 190])
        screen.blit(textRULE4, [1410, 210])
    return isGeneratedPerson

def checker(response):
    if response == "y" and person.skipping == True:
        isCorrect = True
    elif response == "n" and person.skipping == False:
        isCorrect = True
    else:
        isCorrect = False

        currentGame.lives-=1
        
    isGeneratedPerson = False
    return isGeneratedPerson, isCorrect


# Class initialization

class person():

    def __init__(self):
        self.personSprite = str
        self.skipping = bool
        self.grades = int
        self.timeOutOfClass = int
        self.name = str
        self.attendance = list



class game:
    def __init__(self):
        self.difficulty = str
        self.numDays = int
        self.lives = int

    def difficultyInit(self):
        if self.difficulty == "easy":
            self.numDays = 3
            self.lives = 5
        elif self.difficulty == "medium":
            self.numDays = 4
            self.lives = 3
        elif self.difficulty == "hard":
            self.numDays = 5
            self.lives = 1

    def createPerson(self, day):
        currentPerson = person()
        index = random.randint(0, 14)
        person.name = personNameList[index]
        # person.personSprite = personNameList[random.randint(0, 2)]
        person.timeOutOfClass = random.randint(1, 20)
        person.grades = random.randint(30, 99)
        pCount = 0
        attendance = []
        for i in range(4):
            currAttendance = random.randint(0, 1)
            if currAttendance == 0:
                pCount += 1
                attendance.append("Present")
            elif currAttendance == 1:
                attendance.append("Absent")

            person.attendance = attendance
            
        
            
        
        if day == 1 or day == 0:
            if person.timeOutOfClass >= 10:
                person.skipping = True
            else:
                person.skipping = False
        if day > 1 and day < 4:
            if person.grades < 65 or person.timeOutOfClass >= 10 or person.grades < 65 and person.timeOutOfClass >= 10:
                person.skipping = True
            else:
                person.skipping = False
        if day > 3:
            if person.grades < 65 and person.timeOutOfClass >= 10 or person.grades < 65 and pCount < 2 or person.timeOutOfClass >= 10 and pCount < 2:
                person.skipping = True
            else:
                person.skipping = False
                
        return person.name, person.grades, person.timeOutOfClass, person.skipping, person.attendance


fileUp = False
fileNum = 0
numCorrect = 0
numAnswered = 0
dayCounter = 0
totalDays = 1
currentGame = game()
currentGame.lives = 1
while not done:
    # Mouse pos
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]

    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # play button
            if scene == 0 and x > 830 and x < 1180 and y > 350 and y < 500:
                scene = 2

            # easy mode
            elif scene == 2 and x > 800 and x < 1200 and y > 150 and y < 350:
                currentGame.difficulty = "easy"
                currentGame.difficultyInit()
                totalDays = currentGame.numDays
                scene = 3

            # medium mode
            elif scene == 2 and x > 800 and x < 1200 and y > 400 and y < 600:
                scene = 3
                currentGame.difficulty = "medium"
                currentGame.difficultyInit()
                totalDays = currentGame.numDays

            # hard mode
            elif scene == 2 and x > 800 and x < 1200 and y > 650 and y < 850:
                scene = 3
                currentGame.difficulty = "hard"
                currentGame.difficultyInit()
                totalDays = currentGame.numDays

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f and scene == 3 and fileNum > 0:
                if fileUp == False:
                    fileUp = True
                elif fileUp == True:
                    fileUp = False
            if event.key == pygame.K_y and scene == 3 and fileUp == True:
                isGeneratedPerson, isCorrect = checker("y")
                fileUp = False
                fileNum -= 1
                if isCorrect == True:
                    numCorrect += 1
                numAnswered += 1
            if event.key == pygame.K_n and scene == 3 and fileUp == True:
                isGeneratedPerson, isCorrect = checker("n")
                fileUp = False
                fileNum -= 1
                if isCorrect == True:
                    numCorrect += 1
                numAnswered += 1

    if not isGeneratedPerson:
        personName, personGrade, personTimeOut, personSkipping, personAttendance = currentGame.createPerson(dayCounter)
        textName = fontF.render("Name: " + personName, True, BLACK)
        textGrade = fontF1.render("Grade Average: " + str(personGrade), True, BLACK)
        textTime = fontF1.render("Time out of class: " + str(personTimeOut) + " minutes. ", True, BLACK)
        textAttendance = fontF1.render(
            "Attendance: " + str(personAttendance[0]) + ", " + str(personAttendance[1]) + ", ", True, BLACK)
        textAttendance2 = fontF1.render(str(personAttendance[2]) + ", " + str(personAttendance[3]), True, BLACK)
        isGeneratedPerson = True

    textDayCounter = fontF.render("Day: " + str(dayCounter) + "/" + str(totalDays), True, BLACK)

    textCorrect = fontF.render("Number Correct: " + str(numCorrect), True, BLACK)
    screen.fill(BLACK)
    if scene == 0:
        menuScene()
    elif scene == 1:
        scene1()
    elif scene == 2:
        difficultyScreen()
    elif scene == 3:
        gameScene(textName, textGrade, textTime, textCorrect, textAttendance, textAttendance2, textDayCounter,  currentGame.lives, dayCounter)

    pygame.display.flip()

    # game code
    if currentGame.lives > 0:
        if fileNum == 0 and dayCounter < totalDays:
            fileNum = 3 + dayCounter
            dayCounter = dayCounter + 1
        elif fileNum == 0 and dayCounter == totalDays:
            scene = 0
            numCorrect = 0
            dayCounter = 0
    else:
        scene = 0
        numCorrect = 0
        dayCounter = 0
        currentGame.lives = 1

    clock.tick(60)

pygame.quit()