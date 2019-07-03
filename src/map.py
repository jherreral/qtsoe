from PySide2.QtWidgets import (
    QWidget
)
from PySide2.QtCore import Slot

from zone import Zone
from request import ClickRequest


class Map(QWidget):
    """
    Holds all interactive zones
    """

    def __init__(self, parent=None, width=400, height=450):
        super(Map, self).__init__(parent)
        self.scale = width / 826.0
        self.zones = {}
        self.parent = parent
        self.request = None

        self.loadFromAssets()
        self.setAllZones(False)

        z = ['Chile', 'Argen', 'Ingla']
        self.setRequest(ClickRequest(z, 6))

# Requests...
# Map should set the state of the zones it is interested in, and receive
# their feedback until the request criteria is met.
# So each request type is defined by its criteria/goal, the possible zones
# and the current progress.
#
# For example, a request like 'CLick 5 countries in South America' could be:
# Request
# self.goal = 5
# self.current = 0
# self.zonesList = ['Chile','Argen',...]
# for zone in self.zonesList:
#     zone.selectable = True
#     zone.hold = False
#
# In Map add updateCurrentRequest() as a slot. Connect all zone.ZoneActivated
# signals to that slot, so that it checks and updates the conditions.
#
    def setRequest(self, r):
        self.request = r
        self.setZones(r.availableZones, True)
        for zoneName in r.availableZones:
            self.zones[zoneName].zoneSelected.connect(
                self.updateCurrentRequest)

    @Slot(str)
    def updateCurrentRequest(self, zoneName):
        self.request.update(zoneName)
        print("Updating with +1 to "+zoneName)
        result = self.request.check()
        if result:
            # Send signal to GM or PlayerView.
            print('Request done')
            self.setAllZones(False)
            self.request = None

    def loadFromAssets(self):
        self.createBackground()
        self.createZones()

    def createZones(self):
        """
        100mm are equal to 378 px.
        'Real' width is 680 px
        """
        with open('assets/mapCoords.csv', 'r') as f:
            f.readline()
            for line in f:
                (name, x, y, w, h) = line.split(",")
                x = int(x)
                y = int(y)
                w = int(w)
                h = int(h)
                zone = Zone(self, name, (x, y), (w, h), self.scale)
                zone.zoneActivated.connect(self.parent.log.addEntry)
                self.zones[name] = zone

    def createBackground(self):
        pass

    def setZones(self, zoneList, value):
        for zoneName in zoneList:
            self.zones[zoneName].selectable = value

    def setAllZones(self, value):
        for zoneName in self.zones:
            self.zones[zoneName].selectable = value
