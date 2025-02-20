print('WELCOME TO PHYSICS CLASS')





def calculate_velocity(distance, time):
    return distance / time


def calculate_acceleration(velocity, time):
    return velocity / time


def area_of_a_circle(r):
    return float(2 * 3.14 * (r * r))


def gravitational_force(m1, m2, G, r):
    return float((m1 * m2 * G) / (r * r))


def work_done time, force, distance():
    return float((force * distance) / (time))


options = """ here are the list of available formulas
1. velocity
2. acceleration
3.area of a circle
4.gravitational force
5.work_done"""

prompt = 'What do you want to solve'
print(options)
print(prompt)

question = int(input("Enter the alphabet letter A to E of the equation you want to solve:"))

if question == 'A' or question == 'a':
    print('Enter the following information to calculate velocity.')

    distance = float(input('Enter the specified distance here:'))
    time = int(input('Enter the specified time here:'))

    print(calculate_velocity(distance, time))

elif question == 'B' or question == 'b':
    print("Enter the following information to calculate acceleration.")

    velocity = float(input('Enter the specified velocity here:'))
    time = int(input('Enter the specified time here:'))

    print(calculate_acceleration(velocity, time))

elif question == 'C' or question== 'c':
    print("Enter the following information to calculate the area of a circle.")

    radius = float(input("Enter the specified radius here:."))

    print(area_of_a_circle(radius))

elif question == 'D' or question== 'd':
    print("Enter the following information to calculate gravitational force.")

    m1 = int(input('Enter the first mass here:'))
    m2 = int(input('Enter the second mass here:'))
    G = int(input('Enter the gravity here:'))
    radius = float(input('Enter the radius here:'))

    print(gravitational_force(m1.m2.G.r))

elif question == 'E' or question== 'e':
    print("Enter the following information to calculate work done below.")

    time = int(input('Enter the specified time here:'))
    distance = float(input('Enter the specified distance here:'))
    force = float(input('Enter the specified force here:'))

    print(work_done(time, force, distance))


else:
    print("Ooops!!This is not part of the given")