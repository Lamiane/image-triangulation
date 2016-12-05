import numpy as np
from itertools import product


def length(edge):
    pass


def get_points_on_edge(n, edge):
    pass


# assume triangle is: ((x1, y1), (x2, y2), (x3, y3))
def get_points_in_triangle(triangle):
    sorted_triangle = sorted(triangle)

    x = 0
    y = 1
    a, b, c = sorted_triangle[0], sorted_triangle[1], sorted_triangle[2]  # vertices

    if a[x] != b[x]:
        x1 = xrange(a[x], b[x]+1)  # +1 - inclusive

    if b[x] != c[x]:
        x2 = xrange(b[x], c[x]+1)

    # y = kx + m
    if a[x] != b[x]:
        k_ab = float(a[y]-b[y])/(a[x]-b[x])
        m_ab = a[y] - k_ab * a[x]

    if b[x] != c[x]:
        k_bc = float(b[y]-c[y])/(b[x]-c[x])
        m_bc = b[y] - k_bc * b[x]

    # if all three vertices have same x means we have a line not a triangle
    if c[x] == a[x]:
        return set([])

    k_ca = float(c[y]-a[y])/(c[x]-a[x])
    m_ca = c[y] - k_ca * c[x]

    points = []
    if a[x] != b[x]:
        for xx in x1:
            y_s = sorted((k_ab*xx+m_ab, k_ca*xx+m_ca))
            y_range = xrange(int(np.ceil(y_s[0])), int(y_s[1])+1)  # +1 inclusive
            points.extend(product([xx], y_range))

    if b[x]!=c[x]:
        for xx in x2:
            y_s = sorted((k_ca*xx+m_ca, k_bc*xx+m_bc))
            y_range = xrange(int(np.ceil(y_s[0])), int(y_s[1])+1)  # +1 inclusive
            points.extend(product([xx], y_range))

    return set(points)
