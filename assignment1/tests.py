from starter import add_numbers

def test_add():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(10, 20) == 30

if __name__ == "__main__":
    test_add()
    print("All tests passed!")
