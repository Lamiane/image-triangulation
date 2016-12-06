class Edge(object):
    def __init__(self, ends, triangles):
        assert isinstance(triangles, list) or isinstance(triangles, tuple)
        assert 1 <= len(triangles) <= 2
        for x in triangles:
            assert isinstance(x, list) or isinstance(x, tuple)
            assert len(x) == 2

        self.ends = ends
        self.triangles = triangles
