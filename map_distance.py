from itertools import permutations
import random
from math import sqrt
import picture
import time

def distance(point1, point2):
    #point1 and point2 are tuples that contain coordinates
    return sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

def total_distance(points):
    total_distance = 0
    return sum([distance(point, points[index + 1]) for index, point in enumerate(points[:-1])])

def optimize(points):
    perm = list(permutations(points))
    return min(perm, key=total_distance)

def make_points(number_of_points):
    points = []
    for i in range(number_of_points):
        x = random.randint(0,800)
        y = random.randint(0,800)
        points.append((x,y))
    return points

def main():
    num = int(input("Enter number of points: "))
    start_time = time.time()
    points = make_points(num)
    fastest = optimize(points)
    elapsed_time = time.time() - start_time
    canvas = picture.Picture(800,800)
    canvas.setFillColor(0,0,0)
    for point in fastest:
        canvas.drawCircleFill(point[0],point[1],4)
    canvas.setOutlineColor(255,0,0)
    for index, point in enumerate(fastest[:-1]):
        canvas.drawLine(point[0], point[1], fastest[index+1][0], fastest[index+1][1])
    canvas.display()
    print(elapsed_time)
    input()

main()
