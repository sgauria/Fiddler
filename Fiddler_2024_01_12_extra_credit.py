# Extra Credit
# 
# Julien’s puzzle idea didn’t stop there. Instead of two people sitting at the table, now suppose there are three.
# 
# Again, all three randomly pick one die from their respective bags and roll them at the same time. For example, suppose the three dice selected are a d4, a d20, and a d12. The players roll them, and let’s further suppose that the d4 comes out as 4, the d20 comes out as 13, and the d12 comes out as 4. In this case, there are two distinct numbers (4 and 13) among the three rolls.
#
# On average, how many distinct numbers would you expect to see among the three rolls?

def reorder_tuple(p,q,r):
    return tuple(sorted([p,q,r]))
assert(reorder_tuple(2,1,4) == (1,2,4))
    
def expected_distinct_numbers(p,q,r):
    # a <= b <= c
    a,b,c = reorder_tuple(p,q,r)
    total_outcomes = a*b*c
    outcomes_with_1_value = a*1*1
    outcomes_with_2_values = a*1*(c-1) + a*(b-1)*1 + (a-1)*a*1 + a*(b-a)*1
    outcomes_with_3_values = total_outcomes - outcomes_with_1_value - outcomes_with_2_values
    result = (1 * outcomes_with_1_value + 2 * outcomes_with_2_values + 3 * outcomes_with_3_values ) / total_outcomes
    return result

dice = [4,6,8,10,12,20]
exp_sum = 0
for p in dice:
    for q in dice:
        for r in dice:
            exp_sum += expected_distinct_numbers(p,q,r)

final_result = exp_sum/(len(dice) ** 3)
print(final_result)
