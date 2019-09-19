from graph import *

windowSize(600, 400)
canvasSize(600, 400)

penSize(0)
brushColor(238, 246, 12)
rectangle(0, 260, 600, 400)
brushColor(68, 35, 223)
rectangle(0, 160, 600, 260)
brushColor(161, 245, 255)
rectangle(0, 0, 600, 160)
brushColor(255, 247, 29)
circle(540, 60, 40)

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
penColor(146, 179, 183)
brushColor("white")
for i in range(2):
    circle(170 + i * 15, 70, 15)
for i in range(3):
    circle(160 + i * 15, 80, 15)
circle(170 + 2 * 15, 70, 15)
circle(160 + 3 * 15, 80, 15)







# лодка

brushColor(222, 213, 153)
polygon([[400,110], [450,150], [420,150]])
polygon([[400,190], [450,150], [420,150]])
penSize(0)
brushColor(0, 0, 0)
rectangle(395, 110, 400, 190)
brushColor(186, 80, 5)
penColor(186, 80, 5)
polygon([[320,190], [500,190], [450,220], [320,220]])
circle(320,190,30)
brushColor(68, 35, 223)
rectangle(0, 160, 370, 190)
brushColor(0, 0, 0)
circle(460, 200, 8)
brushColor(255, 255, 255)
circle(460, 200, 5)

# зонтик

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







run()