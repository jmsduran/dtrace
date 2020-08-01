class Tuple:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

def is_point(t):
    return True if t.w else False

def is_vector(t):
    return True if not t.w else False
