"""
Request classes that interact with Map to get the users input.
"""


class Request:
    def __init__(self):
        pass


class OneClickRequest(Request):
    def __init__(self, zones, n):
        self.goal = n
        self.current = 0
        self.availableZones = zones
        self.selectedZones = dict(zip(zones, [0]*len(zones)))
        self.hold = False

    def update(self, zoneName):
        self.selectedZones[zoneName] += 1
        self.current += 1

    def check(self):
        if self.current == self.goal:
            return self.selectedZones
        else:
            return None

    def doneMessage(self):
        msg = 'Selected'
        for k in self.selectedZones.keys():
            msg += '\n' + k + ' ' + str(self.selectedZones[k])
        return msg


class MultiClickRequest(Request):
    def __init__(self, zones, n):
        self.goal = n
        self.availableZones = zones
        self.selectedZones = set()

    def update(self, zoneName):
        if zoneName not in self.selectedZones:
            self.selectedZones.add(zoneName)

    def check(self):
        if len(self.selectedZones) == self.goal:
            return self.selectedZones
        else:
            return None
