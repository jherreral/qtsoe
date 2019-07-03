# class MapRequest:
#     def __init__(self,rq):
#         for zone,state


class Request:
    def __init__(self):
        pass


class ClickRequest(Request):
    def __init__(self, zones, n):
        self.goal = n
        self.current = 0
        self.availableZones = zones
        self.selectedZones = dict(zip(zones, [0]*len(zones)))
        self.hold = False

    def update(self, ev):
        self.selectedZones[ev] += 1
        self.current += 1

    def check(self):
        if self.current == self.goal:
            return self.selectedZones
        else:
            return None
