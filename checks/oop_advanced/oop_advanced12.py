result = Vector(1, 2) + Vector(3, 4)
assert isinstance(result, Vector), "Adding two Vector instances should return a Vector"
assert (result.x, result.y) == (4, 6), "Vector(1,2) + Vector(3,4) should be (4, 6)"
print("oop_advanced12 ok")
