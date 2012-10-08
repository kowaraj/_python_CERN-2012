from pytest import mark

from Colour import Colour

@mark.parametrize(('r','g','b'),
                  ((0,0,0),
                   (1,1,1),
                   (0.5,0.5,0.5),
                   (0.2,0.4,0.6)))
def test_rgb_float_0_1_round_trip_should_be_invariant(r,g,b):
    c = Colour.rgb01(r,g,b)
    assert c.as_rgb01 == (r,g,b)

@mark.parametrize('string',
                  ('000', 'fff', 'abc', '19d'))
def test_rgb_hex_string_3_digit_round_trip_should_be_invariant(string):
    c = Colour.hex(string)
    assert c.as_hex3 == string
    

@mark.parametrize('string',
                  ('000000', 'ffffff', 'abcdef', '1a293d'))
def test_rgb_hex_string_6_digit_round_trip_should_be_invariant(string):
    c = Colour.hex(string)
    assert c.as_hex6 == string
    

