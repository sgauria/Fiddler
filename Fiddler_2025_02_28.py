# This Week’s Fiddler
# I have a hat with six small toy rabbits: two are orange, two are green, and two purple. I shuffle the rabbits around and randomly draw them out one at a time without replacement (i.e., once I draw a rabbit out, I never put it back in again).
# Your job is to guess the color of each rabbit I draw out. For each guess, you know the history of the rabbits I’ve already drawn. So if we’re down to the final rabbit in the hat, you should be able to predict its color with certainty.
# Every time you correctly predict the color of the rabbit I draw, you earn a point. If you play optimally (i.e., to maximize how many points you get), how many points can you expect to earn on average?

# This Week’s Extra Credit
# Now, instead of two rabbits of each of the three colors, my hat contains 10. That is, it contains 10 orange rabbits, 10 green rabbits, and 10 purple rabbits. As before, every time you correctly predict the color of the rabbit I draw, you earn a point.
# With optimal play, how many points can you expect to earn on average?

saved_results = dict()

def expected_points(a, indent=0, dbg_lvl=0):
    global saved_results
    spaces = " " * indent
    if (dbg_lvl > 0):
        print (spaces, a)

    key_a = tuple(a)
    if (key_a in saved_results):
        ep = saved_results[key_a]
        if (dbg_lvl > 0):
            print (spaces, ":", ep)
        return ep
    
    max_a = max(a)
    min_a = min(a)
    if (min_a < 0 or max_a <= 0):
        saved_results[key_a] = 0
        if (dbg_lvl > 0):
            print(spaces, ":", 0)
        return 0
    
    sum_a = sum(a)
    len_a = len(a)  

    points = (max_a/sum_a)

    for i in range(len_a):
        b = a[:]
        b[i] -= 1
        p_a_to_b = (a[i] / sum_a)
        pts_b = expected_points(sorted(b), indent+4, dbg_lvl-1)
        points += (p_a_to_b * pts_b)
    
    saved_results[key_a] = points
    if (dbg_lvl > 0):
        print(spaces, ":", points)
    return points

expected_points([2,2,2],0,1)

expected_points([10,10,10],0,1)


# for key in saved_results:
#    if (min(key) >= 0):
#        print (key, saved_results[key])


    
