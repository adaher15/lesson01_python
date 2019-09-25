r_1 = r_2 = g_1 = g_2 = y_1 = y_2 = False
def change_light():
     print("Function that will turn light on when value is True")

#step 0
r_1 = g_2 = True
change_light()
time.sleep(5)
#step 1
y_2 = True
g_2 = False
change_light()
time.sleep(1)

#step 2
r_1 = y_2 = False
g_1 = r_2 = True
change_light()
time.sleep(5)
#step 4
g_1 = False
y_1 = True
change_light()
time.sleep(1)
#step 5
r_1 = g_2 = True
y_1 = r_2 = False
time.sleep(5)
