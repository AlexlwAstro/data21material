"""
introduction to OOP in Python - classes, methods, etc.

Create a car class. Give the vehicle a maximum speed, and keep track of the current speed of the vehicle.
It doesn't make sense for the speed to be adjusted directly,
so put an underscore in front of it and implement a speed getter as well as accelerate and
brake setter methods that change the speed in a logical way.
Do your methods make sense? Does braking past 0 cause the speed to increase?
Can you accelerate past the car's top speed?
"""

class Car:
    def __init__(self, m_kg, p_bhp, listed_top_speed, max_occ):
        self.mass = m_kg
        self.engine_power_bhp = p_bhp
        self.max_occupants = max_occ
        self.top_speed = listed_top_speed

    # USING the metric horsepower, which is approximately 735.5 watts, for engine power
    def calc_dynamics(self, pick_weight):
        p_w = 735.5*self.engine_power_bhp
        # assume constant drag coefficient, b where F_drag = b x speed
        # calculate using max. speed case, where F_drag = F_engine = engine power / top speed
        # units are bhp/(mph^2)
        drag_coefficient = self._bhp / (self.listed_top_speed ** 2)
        pick_weight = input('How full will your car be when travelling? (0 = empty, 1 = half-full, 2 = fully loaded)')
        if pick_weight == 0:  # minimum kerb weight

        elif pick_weight == 1:  # half full

        elif pick_weight == 2: # gross vehicle weight (max. weight)

        else:
            print(f"}")


        return p_w, drag_coefficient
"""
Ford Focus Estate 1.0 EcoBoost 100 Zetec Nav 5dr
(https://www.autoexpress.co.uk/ford/focus/estate/prices-specs/83608/1.0-ecoboost-100-zetec-nav-5dr):

Engine Power - BHP	100
Top Speed	114 mph
-------------------------------------
Length	4668 mm
Wheelbase	2700 mm
Width	1825 mm
Width (including mirrors)	1979 mm
-------------------------------------
Fuel Tank Capacity (Litres)	52
Gross Vehicle Weight	1925 kg
Luggage Capacity (Seats Down)	1620 l
Luggage Capacity (Seats Up)	575 l
Max. Loading Weight	617 kg (= Gross Vehicle Weight - Minimum Kerbweight
Max. Roof Load	75
Max. Towing Weight - Braked	1000
Max. Towing Weight - Unbraked	690
Minimum Kerbweight	1308 kg
"""


ford_focus = Car(1500, 100, 5)


