import lesson_2

def variable_exists ():
    assert lesson_2.create_variable() != None, "VARIABLE NOT CREATED"
    print("SUCCESS: VARIABLE CREATED")


def is_string ():
    assert type(lesson_2.create_string()) == str, "STRING NOT RETURNED"
    print("SUCCESS: VARIABLE CREATED")


def is_integer ():
    assert type(lesson_2.create_integer()) == int, "INTEGER NOT RETURNED"
    print("SUCCESS: VARIABLE CREATED")


def is_boolean ():
    assert type(lesson_2.create_boolean()) == bool, "BOOLEAN NOT RETURNED"
    print("SUCCESS: VARIABLE CREATED")


def is_list ():
    assert type(lesson_2.create_list()) == list, "LIST NOT RETURNED"
    print("SUCCESS: VARIABLE CREATED")

