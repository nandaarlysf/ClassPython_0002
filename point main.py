from point import *
p1=point(30, 40)
p1.nama="Titik satu"
print(p1.nama+"\{"+str(p1.x)+","+str(p1.y)+"}")
p2=point(3,4)
print(p2)
print(p2.distance_from_origin())

p3=point(60,80)
print("jarak 2 titik"+str(p2.distance(p3)))