# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 16:24:11 2014

This code is published under the DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE.
The license text can be seen here, too: http://www.wtfpl.net/about/.

@author: Amarandus
"""

class RC4(object):
    def __init__(self, key, boxlength):
        # Init the Vector
        self._box = list(range(0, boxlength))

        # Scramble the bytevector up
        j = 0
        for i in range(0, boxlength):
            j = (j + self._box[i] + key[i % len(key)]) % len(self._box)
            (self._box[i], self._box[j]) = (self._box[j], self._box[i])

        # self.__box is the scrambled box now, init generation loop now
        (self._i, self._j) = (0, 0)

    def getNextKeybyte(self):
        self._i = (self._i + 1) % len(self._box)
        self._j = (self._j + self._box[self._i]) % len(self._box)

        (self._box[self._i], self._box[self._j]) = (self._box[self._j], self._box[self._i])

        return self._box[(self._box[self._i] + self._box[self._j]) % len(self._box)]