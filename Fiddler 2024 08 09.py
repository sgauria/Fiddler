# Fiddler 2024 08 09

for points_per_side in [11, 23, 53, 79, 101]:
    total_points = points_per_side ** 4
    coordinates = [(10 * ((i + 0.5)/points_per_side)) for i in range(points_per_side)]
    total_count = 0
    interesting_count = 0
    for X in coordinates:
        for Y in coordinates:
            sum_XY = X + Y
            prod_XY = X * Y
            for Z in coordinates:
                sum_XYZ = sum_XY - Z
                for W in coordinates:
                    sum_diff_XYZW = sum_XYZ - W
                    prod_diff_XYZW = prod_XY - Z * W
                    total_count += 1
                    if (sum_diff_XYZW < 0 and prod_diff_XYZW >= 0 or sum_diff_XYZW >= 0 and prod_diff_XYZW < 0):
                        interesting_count += 1
    print (points_per_side, (interesting_count/total_count))


