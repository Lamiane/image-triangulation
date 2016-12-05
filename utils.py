import numpy as np
from itertools import product
# IMPORTANT: we assume all coordinates will be non-negative
# assume triangle is: ((x1, y1), (x2, y2), (x3, y3))
# assume edge is: ((x1, y1), (x2, y2))
x = 0
y = 1


def length(edge):
    x_length = np.abs(edge[0][0]-edge[1][0])
    y_length = np.abs(edge[0][1]-edge[1][1])
    return np.sqrt(x_length**2 + y_length**2)


# TODO testing!
def get_points_on_edge(n, edge):

    interval_x = np.float(np.abs(edge[0][x]-edge[1][x]))/(n+1)  # +1 we want n points INSIDE edge
    interval_y = np.float(np.abs(edge[0][y]-edge[1][y]))/(n+1)

    min_x = np.min([v[x] for v in edge])
    min_y = np.min([v[y] for v in edge])

    x_coordinates = [min_x + i*interval_x for i in xrange(1, n+1)]
    y_coordinates = [min_y + i*interval_y for i in xrange(1, n+1)]

    x_coordinates = [np.int(xc) for xc in x_coordinates]
    y_coordinates = [np.int(yc) for yc in y_coordinates]

    if calculate_slope(edge)>0:
        return zip(x_coordinates, y_coordinates)
    else:
        return zip(x_coordinates, reversed(y_coordinates))


def calculate_slope(edge):
    a, b = edge
    if a[x] == b[x]:
        return None
    if a[y] == b[y]:
        return 0
    return float(a[y]-b[y])/(a[x]-b[x])


# http://stackoverflow.com/questions/8957028/getting-a-list-of-locations-within-a-triangle-in-the-form-of-x-y-positions
# punkty na krawedziach moga byc uwzglednione badx nie w zaleznosci od tego jak python zaokragli!
def get_points_in_triangle(triangle):
    sorted_triangle = sorted(triangle)

    a, b, c = sorted_triangle[0], sorted_triangle[1], sorted_triangle[2]  # vertices
    points = []

    # y = kx + m
    # if all three vertices have same x, it means we have a line not a triangle
    if c[x] == a[x]:
        return set([])

    k_ca = calculate_slope((c, a))
    m_ca = c[y] - k_ca * c[x]

    if a[x] != b[x]:
        x1 = xrange(a[x], b[x]+1)  # +1 - inclusive
        k_ab = calculate_slope((a, b))
        m_ab = a[y] - k_ab * a[x]
        for xx in x1:
            y_s = sorted((k_ab*xx+m_ab, k_ca*xx+m_ca))
            y_range = xrange(int(np.ceil(y_s[0])), int(y_s[1])+1)  # +1 inclusive
            points.extend(product([xx], y_range))

    if b[x] != c[x]:
        x2 = xrange(b[x], c[x]+1)
        k_bc = calculate_slope((b, c))
        m_bc = b[y] - k_bc * b[x]
        for xx in x2:
            y_s = sorted((k_ca*xx+m_ca, k_bc*xx+m_bc))
            y_range = xrange(int(np.ceil(y_s[0])), int(y_s[1])+1)  # +1 inclusive
            points.extend(product([xx], y_range))

    return set(points)
