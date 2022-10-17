import lesson_1

def test_apple ():
    fruit = lesson_1.myFunction()[0]
    assert fruit.upper() == 'RED', "APPLES ARE RED"
    print('\nSUCCESS: APPLES ARE RED!')


def test_orange ():
    fruit = lesson_1.myFunction()[1]
    assert fruit.upper() == 'ORANGE', "ORANGES ARE ORANGE"
    print('SUCCESS: ORANGES ARE ORANGE!')


def test_banana ():
    fruit = lesson_1.myFunction()[2]
    assert fruit.upper() == 'YELLOW', "BANANAS ARE YELLOW"
    print('SUCCESS: BANANAS ARE YELLOW!')
