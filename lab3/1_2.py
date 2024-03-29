from graph import *
import math

windowSize(600, 400)
canvasSize(600, 400)

penSize(0)
brushColor(238, 246, 12)
rectangle(0, 255, 600, 400)          # zemlya
brushColor(68, 35, 223)
rectangle(0, 160, 600, 255)          # more
brushColor(161, 245, 255)
rectangle(0, 0, 600, 160)            # nebo

#
        # берег

penColor(68, 35, 223)
for i in range(10):
    for j in range(600):
        if (i - 5 < 5 * math.sin(j / 50 * math.pi)):
            point(j, i + 255)


        # облака

    # 1 стак облаков

penSize(1)
penColor(146, 179, 183)
brushColor("white")
for i in range(2):
    circle(170 + i * 15, 70, 15)
for i in range(3):
    circle(160 + i * 15, 80, 15)
circle(170 + 2 * 15, 70, 15)
circle(160 + 3 * 15, 80, 15)

    # 2 стак облаков

penSize(1)
penColor(92, 124, 128)
brushColor("white")
for i in range(2):
    oval(70 + i * 20, 100, 110 + i * 20, 125)
for i in range(3):
    oval(55 + i * 20, 110, 95 + i * 20, 135)
oval(70 + 2 * 20, 100, 110 + 2 * 20, 125)
oval(55 + 3 * 20, 110, 95 + 3 * 20, 135)

    # 3 стак облаков

penSize(1)
penColor(92, 124, 128)
brushColor("white")
for i in range(2):
    oval(270 + i * 25, 15, 310 + i * 25, 70)
for i in range(3):
    oval(250 + i * 25, 40, 290 + i * 25, 95)
oval(270 + 2 * 25, 15, 310 + 2 * 25, 70)
oval(250 + 3 * 25, 40, 290 + 3 * 25, 95)


        # лодка

    # лодка 1

penColor(222, 213, 153)
brushColor(222, 213, 153)
polygon([[400,110], [450,150], [420,150]])  # parus
polygon([[400,190], [450,150], [420,150]])  # parus
penSize(0)
brushColor(0, 0, 0)
rectangle(395, 110, 400, 190)  # machta
brushColor(186, 80, 5)
penColor(186, 80, 5)
polygon([[320,190], [500,190], [450,220], [320,220]])  # korpus
circle(320, 190, 30)
brushColor(68, 35, 223)
rectangle(0, 160, 370, 190)
brushColor(0, 0, 0)
circle(460, 200, 8)               # glaz
brushColor(255, 255, 255)
circle(460, 200, 5)

    # лодка 2

penColor(222, 213, 153)
brushColor(222, 213, 153)
polygon([[200,130], [218,150], [208,150]])               # parusa
polygon([[200,170], [218,150], [208,150]])
penSize(0)
brushColor(0, 0, 0)
rectangle(197, 130, 200, 170)                         # machta
brushColor(186, 80, 5)
penColor(186, 80, 5)
polygon([[170,170], [260,170], [230,185], [170,185]])     # korpus
circle(170, 170, 15)
brushColor(68, 35, 223)
rectangle(0, 160, 190, 170)
brushColor(161, 245, 255)
rectangle(0, 150, 190, 160)
brushColor(0, 0, 0)                  # glaz
circle(240, 175, 4)
brushColor(255, 255, 255)
circle(240, 175, 2)

        # solnce
    
penColor(238, 246, 12)
z = []
a = 100
for i in range(a):
    z.append([((math.sin(i / a * 2 * math.pi)) * (35 + 15 * (i % 2)) + 540), ((math.cos(i / a * 2 * math.pi)) * (35 + 15 * (i % 2)) + 60)])
brushColor(238, 246, 12)
polygon(z)
    
        # зонтикs

    # 1 zont
    
penColor(186, 80, 5)
brushColor(227, 130, 25)
rectangle(100, 220, 105, 360)
brushColor(244, 81, 81)
polygon([[100,220], [105,220], [170,250], [35,250]])
for i in range(4):
    line(100, 220, 35 + 18 * i, 250)
line(100, 220, 100, 250)
for i in range(4):
    line(105, 220, 170 - 18 * i, 250)
line(105, 220, 105, 250)

    # 2 zont
    
penColor(186, 80, 5)
brushColor(227, 130, 25)
rectangle(230, 240, 233, 340)
brushColor(244, 81, 81)
polygon([[210,260], [230,240], [233,240], [253,260]])
for i in range(5):
    line(230, 240, 210 + 5 * i, 260)
for i in range(5):
    line(233, 240, 253 - 5 * i, 260)



run()