import serial


class VFD:
    def __init__(self, port, rtscts=False):
        self.serial = serial.Serial(port, 9600, rtscts=rtscts)

    def reset(self):
        # sending 0x00 on 4800 baud causes reset
        self.serial.close()
        s = serial.Serial(self.serial.port, 4800)
        s.write(b'\x00')
        s.close()
        self.__init__(self.serial.port, self.serial.rtscts)

    def write(self, s):
        self.serial.write(bytes(s, 'ascii'))

    def normal_mode(self):
        self.write('\x1b[CM0')

    def test_mode(self):
        self.write('\x1b[CM1')

    # value from 0 (off) to 5 (100%)
    def brightness(self, value):
        assert 0 <= value <= 5, "Incorrect brightness value! Allowed: [0, 5]"
        self.write('\x1b\\?LD{}'.format(value))

    def backspace(self):
        self.write('\x08')

    def new_line(self):
        self.write('\x0A')

    def carriage_return(self):
        self.write('\x0D')

    def clear_display(self):
        self.write('\x1b[2J')

    # y = 1 - first line
    def set_cursor(self, x, y):
        self.write('\x1b[{};{}H'.format(y, x))

    def delete_to_end_of_line(self):
        self.write('\x1b[0K')

    class CursorMode:
        off = '0',
        blink = '1',
        on = '2',

    def cursor_mode(self, mode: CursorMode):
        self.write('\x1b\\\?LC' + mode)

    class CharacterMode:
        normal = '0'
        blink = '5'
        inverse = '7'

    def character_mode(self, mode: CharacterMode):
        self.write('\x1b[{}m'.format(mode))
