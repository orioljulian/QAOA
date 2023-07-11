import itertools
import numpy as np

def are_equal(e1, e2, nbits=4, p=20):
    n = nbits
    is_wrong = False
    min_val = np.Infinity
    min_bits = None
    for z in itertools.product([-1, 1], repeat=n):
        vars = dict()
        for i in range(n):
            vars[f"z_{i}"] = z[i]

        res1 = eval(e1, dict({"P": p}, **vars))
        res2 = eval(e2, vars)
        if res1 != res2:
            is_wrong = True
            print("Error: ", f"{z}", res1, res2)
        if res1 < min_val:
            min_val = res1
            min_bits = z
    if not is_wrong:
        print("Las expresiones son equivalentes, min=" + str(min_val), min_bits)

exp_orig="\
3*(1-z_0)/2 + \
6*(1-z_1)/2 + \
9*(1-z_2)/2 + \
1*(1-z_3)/2 + \
P*((1 - z_0)/2 + (1 - z_1)/2 - 1)**2 + \
P*((1 - z_2)/2 + (1 - z_3)/2 - 1)**2 + \
P*((1 - z_0)/2 - (1 - z_2)/2)**2 + \
P*((1 - z_1)/2 - (1 - z_3)/2)**2 \
"

exp_20 = "\
-1.5*z_0 - 3*z_1 - 4.5*z_2 - 0.5*z_3 + \
10*z_0*z_1 - 10*z_0*z_2 - 10*z_1*z_3 + 10*z_2*z_3 + \
10*z_0**2 + 10*z_1**2 + 10*z_2**2 + 10*z_3**2 + 49.5 \
"

exp_40 = "\
- 1.5*z_0 - 3*z_1 - 4.5*z_2 - 0.5*z_3 + \
20*z_0*z_1 - 20*z_0*z_2 - 20*z_1*z_3 + 20*z_2*z_3 + \
20*z_0**2 + 20*z_1**2 + 20*z_2**2 + 20*z_3**2 + 9.5 \
"

if __name__ == "__main__":
    print("exp_orig == exp_20: ", end="")
    are_equal(exp_orig, exp_20, p=20)
    print("exp_orig == exp_40: ", end="")
    are_equal(exp_orig, exp_40, p=40)
