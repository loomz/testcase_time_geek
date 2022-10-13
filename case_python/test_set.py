

def test_type():
    default_headers = {"Content-Type": "application/json; charset=UTF-8"}
    print(type(default_headers))

    default_headers = ("a", "b")
    print(type(default_headers))

    default_headers = ["a", "b"]
    print(type(default_headers))

