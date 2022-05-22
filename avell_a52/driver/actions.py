"""
Copyright (c) 2019, Petryx.
License MIT
Created on August 19, 2019
@author: @petryx
"""

from .constants import Colors, Brightness, Speed, Directions


class Actions():

    def __init__(self, dev, save=0):
        self.dev = dev
        self.save = save

    def turnOff(self):
        self.dev.sendCommand(0x08, 0x01, 0x0, 0x0, 0x0, 0x0, 0x0, self.save)

    def monocolor(self, color, brightness):
        for i in range(1, self.dev.n_cols+1):
            self.dev.sendCommand(
                0x14, 0x00, i, *Colors[color].value, 0x00, self.save)
        self.brightness(brightness)

    def brightness(self, level):
        self.dev.sendCommand(0x08, 0x02, 0x01, 0x05,
                             Brightness[level].value, 0x08, 0x00, self.save)

    def _rainbowColors(self):
        self.dev.sendCommand(0x14, 0x00, 0x01, *
                             Colors.red.value, 0x00, self.save)
        self.dev.sendCommand(0x14, 0x00, 0x02, *
                             Colors.green.value, 0x00, self.save)
        self.dev.sendCommand(0x14, 0x00, 0x03, *
                             Colors.blue.value, 0x00, self.save)
        self.dev.sendCommand(0x14, 0x00, 0x04, *
                             Colors.fuchsia.value, 0x00, self.save)

    def _defaultColors(self):
        self.dev.sendCommand(0x14, 0x00, 0x01, *
                             Colors.red.value, 0x00, self.save)
        self.dev.sendCommand(0x14, 0x00, 0x02, *
                             Colors.orange.value, 0x00, self.save)
        self.dev.sendCommand(0x14, 0x00, 0x03, *
                             Colors.yellow.value, 0x00, self.save)
        self.dev.sendCommand(0x14, 0x00, 0x04, *
                             Colors.green.value, 0x00, self.save)
        self.dev.sendCommand(0x14, 0x00, 0x05, *
                             Colors.blue.value, 0x00, self.save)
        self.dev.sendCommand(0x14, 0x00, 0x06, *
                             Colors.fuchsia.value, 0x00, self.save)
        self.dev.sendCommand(0x14, 0x00, 0x07, *
                             Colors.olive.value, 0x00, self.save)

    def rainbow(self, speed, directions, brightness):
        self._rainbowColors()
        self.dev.sendCommand(
            0x08, 0x02, 0x05, Speed[speed].value, Brightness[brightness].value, 0x08, Directions[directions].value, self.save)

    def waving(self, speed, directions, brightness):
        self._defaultColors()
        self.dev.sendCommand(
            0x08, 0x02, 0x03, Speed[speed].value, Brightness[brightness].value, 0x08, Directions[directions].value, self.save)

    def breathing(self, speed, directions, brightness):
        self._defaultColors()
        self.dev.sendCommand(
            0x08, 0x02, 0x02, Speed[speed].value, Brightness[brightness].value, 0x08, Directions[directions].value, self.save)

    def flash(self, speed, directions, brightness):
        self._defaultColors()
        self.dev.sendCommand(
            0x08, 0x02, 0x12, Speed[speed].value, Brightness[brightness].value, 0x08, Directions[directions].value, self.save)

    def mix(self, speed, directions, brightness):
        self._defaultColors()
        self.dev.sendCommand(
            0x08, 0x02, 0x13, Speed[speed].value, Brightness[brightness].value, 0x08, Directions[directions].value, self.save)
