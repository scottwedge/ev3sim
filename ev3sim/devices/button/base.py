class ButtonMixin:

    device_type = 'brick_button'

    pressed = False

    def _getObjName(self, port):
        return 'button' + port

    def toObject(self):
        data = {
            'address': self._interactor.port,
            'driver_name': 'ev3sim-button',
            'pressed': self.pressed,
        }
        return data