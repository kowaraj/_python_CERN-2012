class Colour(object):

    @staticmethod
    def rgb01(r,g,b):
        c = Colour()
        c.rgb_components = (r,g,b)
        return c

    @property
    def as_rgb01(self):
        return self.rgb_components

    @staticmethod
    def hex(string):
        c = Colour()
        if len(string) == 3:
            c.rgb_components = tuple(map(hex_N_digits_to_01(1), string))
        elif len(string) == 6:
            c.rgb_components = tuple(map(hex_N_digits_to_01(2), string))
        else:
            raise ValueError('Colour.hex requires 3 or 6 hexadecimal digts; got %d'
                             % len(string))
        return c

    @property
    def as_hex3(self):
        return ''.join(map(hex_N_digits_from_01(1), self.rgb_components))

    @property
    def as_hex6(self):
        return ''.join(map(hex_N_digits_from_01(2), self.rgb_components))


def hex_N_digits_to_01(N):
    biggest = float(16**N)
    def hex_digits_to_01(digit):
        return (int(digit, 16) + 0.5) / biggest
    return hex_digits_to_01

def hex_N_digits_from_01(N):
    def hex_digits_from_01(real):
        return hex(int(real * 16**N))[2:]
    return hex_digits_from_01
