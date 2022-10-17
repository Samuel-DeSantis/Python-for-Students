import lesson_2

def test_variable_exists ():
    assert lesson_2.create_variable() != None, "VARIABLE NOT CREATED"
    print("SUCCESS: VARIABLE CREATED")


def test_is_string ():
    assert type(lesson_2.create_string()) == str, "STRING NOT RETURNED"
    print("SUCCESS: STRING RETURNED")


def test_is_integer ():
    assert type(lesson_2.create_integer()) == int, "INTEGER NOT RETURNED"
    print("SUCCESS: INTEGER RETURNED")


def test_is_boolean ():
    assert type(lesson_2.create_boolean()) == bool, "BOOLEAN NOT RETURNED"
    print("SUCCESS: BOOLEAN RETURNED")


def test_is_list ():
    assert type(lesson_2.create_list()) == list, "LIST NOT RETURNED"
    print("SUCCESS: LIST CREATED")

