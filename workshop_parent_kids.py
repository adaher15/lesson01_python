import time
end = '\033[0m'
row = u'\u2592'
Red = '\033[91m'
Green = '\033[92m'
Blue = '\033[94m'
Cyan = '\033[96m'
White = '\033[97m'
Yellow = '\033[93m'
Magenta = '\033[95m'
Grey = '\033[90m'
Black = '\033[90m'
Default = '\033[99m'
space = ' '*5



def printing_colors(l1, l2):
   p1 = p2 = p3 = d1 = d2 = d3 = Grey
   if l1 == 1 :
       p1 = Red
   elif l1 == 2:
       p2 = Yellow
   else:
       p3 = Green
   if l2 == 1 :
       d1 = Red
   elif l2 == 2:
       d2 = Yellow
   else:
       d3 = Green
   print(f"\n{p1}{row*2}{space}{d1}{row*2}")
   print(f"{p2}{row*2}{space}{d2}{row*2}")
   print(f"{p3}{row*2}{space}{d3}{row*2}")
   
   
cycle= [[1, 3], [1, 2], [3, 1], [2, 1], [1, 3]]
for l in range(0,len(cycle)):
   printing_colors(cycle[l][0], cycle[l][1] )
   time.sleep(1)
