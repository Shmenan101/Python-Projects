def C_to_F (C):
    """Convert Celcius to Farenheit
    """
    F = ( C * 1.8 ) + 32
    return F


def test_C_to_F ():
    assert C_to_F (1) == 33.8
    assert C_to_F (15) == 59
    assert C_to_F (25) == 77
    assert C_to_F (30) == 86
    
