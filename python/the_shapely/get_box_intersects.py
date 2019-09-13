# -*- coding: utf-8 -* -
"""
获取多边形的重合区域
"""
import numpy as np
import shapely
from shapely.geometry import Polygon,MultiPoint,GeometryCollection

p1 = np.array([2,2,2,4,4,4,4,2]).reshape((4,2))
p2 = np.array([5,5,5,7,7,7,7,5]).reshape((4,2))

p3 = np.array([1,1,1,5,5,5,5,1]).reshape((4,2))
p4 = np.array([3,3,3,5,5,5,5,3]).reshape((4,2))

print(Polygon(p1).intersects(Polygon(p3)))
print(Polygon(p1).intersects(Polygon(p2)))
print(Polygon(p3).intersects(Polygon(p1)))

union_poly_1_2 = np.concatenate((p1,p2))
union_poly_1_3 = np.concatenate((p1,p3))
union_poly_2_3 = np.concatenate((p2,p3))

print(MultiPoint(union_poly_1_2).convex_hull)
print(MultiPoint(union_poly_1_3).convex_hull)
print(MultiPoint(union_poly_2_3).convex_hull)

print(" ====  ")
print(Polygon(p1).intersection(Polygon(p2)).convex_hull)
print(Polygon(p1).intersection(Polygon(p3)).convex_hull)
print(Polygon(p3).intersection(Polygon(p1)).convex_hull)
print(Polygon(p1).intersection(Polygon(p4)).convex_hull)
print(Polygon(p2).intersection(Polygon(p3)).convex_hull)

print("===")
hull = Polygon(p1).intersection(Polygon(p4)).convex_hull
print(list(hull.exterior.coords))
# print(hull.type.geoms is not None)
print(Polygon(p1).intersection(Polygon(p2)).exterior)
