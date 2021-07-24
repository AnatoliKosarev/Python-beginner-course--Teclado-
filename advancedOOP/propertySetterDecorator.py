from typing import List


class Segment:
    def __init__(self, departure, destination):
        self.departure = departure
        self.destination = destination


class Flight:
    def __init__(self, segments: List[Segment]):
        self.segments = segments

    def __repr__(self):
        """
        returns string in the format of 'departure point -> stop 1 -> stop 2 ...'
        """
        # stops = [self.segments[0].departure, self.segments[0].destination]
        # for segment in self.segments[1:]:
        #     stops.append(segment.destination)
        stops = [self.segments[0].departure] + [segment.destination for segment in self.segments]
        return ' -> '.join(stops)

    @property
    def departure_point(self):
        return self.segments[0].departure

    @departure_point.setter  # allows to change value for functions as if it's a class property
    def departure_point(self, new_dep_point):
        # self.segments[0].departure = new_dep_point
        destination = self.segments[0].destination
        self.segments[0] = Segment(new_dep_point, destination)


flight = Flight([Segment('GLA', 'LHR'), Segment('LHR', 'CAN')])
print(flight.departure_point)
print(flight)

flight.departure_point = 'EDI'  # calls departure_point(self, new_dep_point) via @departure_point.setter
print(flight.departure_point)
print(flight)