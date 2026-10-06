from point import *
from point3D import *
p1=Point(3, 4)
jarak=p1.distance_from_origin()
print("Jarak dari titik asal:",jarak)
pl_lain=Point(10, -10)
jarak_dua_titik=p1.distance(pl_lain)
print("Jarak:", jarak_dua_titik)
print(pl_lain)
p13D=Point3D(10, -12, 3)
print(p13D)
