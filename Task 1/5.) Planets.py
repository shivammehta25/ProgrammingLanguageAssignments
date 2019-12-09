#!/usr/bin/env python
from math import sqrt, pow, cos

class Constants:
    GCONSTANT = 6.673 * (10 ** -11)
    GACCEL = 9.8
    AU_TO_KM = 149598000


class Planet:

    def __init__(self, name, mass, coordinates):
        self.name = name
        self.mass = mass
        self.coordinates = coordinates

class GravitationalField:

    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def distance_between_planets_x(self, p1, p2):
        return p2.coordinates[0] - p1.coordinates[0]

    def distance_between_planets_y(self, p1, p2):
        return p2.coordinates[1] - p1.coordinates[1]

    def sum_of_vectors_in_a_direction_for_a_planet(self,planet, a,b):
        return a+b

    def calculate_acceleration_by_force_and_mass(self, fx, fy, mass):
        ax = fx / mass
        ay = fy / mass
        return ax, ay

    def calculate_force(self, p1, p2):
        dist_x = self.distance_between_planets_x(p1, p2)
        dist_y = self.distance_between_planets_y(p1, p2)
        fx = abs(Constants.GCONSTANT * self.p1.mass * self.p2.mass / pow(dist_x * Constants.AU_TO_KM , 2))
        fy = abs(Constants.GCONSTANT * self.p1.mass * self.p2.mass / pow(dist_y * Constants.AU_TO_KM , 2))
        return fx, fy

    @staticmethod
    def calculate_displacement_by_acceleration_and_time(ax, ay, time):
        displacementx = 1/2 * ax * (time**2)
        displacementy = 1/2 * ay * (time ** 2)
        return displacementx, displacementy

    @staticmethod
    def magnitude_of_vector_in_two_dimentional_plane(sx , sy):
        return sqrt(sx**2 + sy**2)

    @staticmethod
    def print_motion_of_planet(motion_of_planets_at_each_step):
        for planet in motion_of_planets_at_each_step:
            print('{0} {1}'.format(planet, ' '.join(list(map(str, motion_of_planets_at_each_step[planet])))))

    def run(self, steps):
        motion_of_planets_at_each_step = { self.p1.name: [], self.p2.name: [], self.p3.name : []}
        for step in range(steps):
            f12x, f12y = self.calculate_force(self.p1, self.p2)
            f23x, f23y = self.calculate_force(self.p2, self.p3)
            f31x, f31y = self.calculate_force(self.p3, self.p1)

            a1x, a1y = self.calculate_acceleration_by_force_and_mass(f12x, f12y,self.p1.mass)
            a2x, a2y = self.calculate_acceleration_by_force_and_mass(f23x, f23y, self.p2.mass)
            a3x, a3y = self.calculate_acceleration_by_force_and_mass(f31x, f31y, self.p3.mass)

            s1x, s1y = self.calculate_displacement_by_acceleration_and_time(a1x, a1y, step)
            s2x, s2y = self.calculate_displacement_by_acceleration_and_time(a2x, a2y, step)
            s3x, s3y = self.calculate_displacement_by_acceleration_and_time(a3x, a3y, step)

            s1 = self.magnitude_of_vector_in_two_dimentional_plane(s1x, s1y)
            s2 = self.magnitude_of_vector_in_two_dimentional_plane(s2x, s2y)
            s3 = self.magnitude_of_vector_in_two_dimentional_plane(s3x, s3y)

            motion_of_planets_at_each_step[self.p1.name].append('{0:.2f}'.format(s1))
            motion_of_planets_at_each_step[self.p2.name].append('{0:.2f}'.format(s2))
            motion_of_planets_at_each_step[self.p3.name].append('{0:.2f}'.format(s3))

        self.print_motion_of_planet(motion_of_planets_at_each_step)

def main():
    earth = Planet('Earth', 5.972 * (10 ** 24), [0, 0, 1, 2])
    mars = Planet('Mars', 6.39 * (10 ** 23), [2, 3, 4, 5])
    venus = Planet('Venus', 4.867 * (10 ** 24), [4, 5, 6, 7])

    model = GravitationalField(earth, mars, venus)
    steps = int(input('Step: '))
    model.run(steps)


if __name__ == '__main__':
    main()
