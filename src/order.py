# encoding: utf-8


class Order:
  def __init__(self, _L):
    self._L = _L
    pass

  def announce(self):
    self._L.info('#\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t#')
    self._L.info('#\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t#')
    self._L.info('#\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t#')
    self._L.info('# O R D E R   S U B M I T T E D       ')
    self._L.info('#\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t#')
    self._L.info('#\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t#')
    self._L.info('#\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t#')
