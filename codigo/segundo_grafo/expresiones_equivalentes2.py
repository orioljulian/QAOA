import itertools
import numpy as np


def are_equal(nbits=11):
    n = nbits
    is_wrong = False
    min_res = np.inf
    min_bits = None
    for z in itertools.product([-1, 1], repeat=n):
        var_dict = dict()
        for i in range(n):
            var_dict[f"z_{i}"] = z[i]

        res1 = eval(exp1, dict({"P": 27}, **var_dict))
        res2 = eval(exp2, var_dict)
        if res1 != res2:
            is_wrong = True
            print("Error: ", f"{z}", res1, res2)
        elif res1 < min_res:
            min_res = res1
            min_bits = z

    if not is_wrong:
        print("Las expresiones son equivalentes")

    print(f"Min path: {min_res} - {min_bits}")


exp1 = "\
+ 2*(1-z_0)/2 \
+ 1*(1-z_1)/2 \
+ 5*(1-z_2)/2 \
+ 2*(1-z_3)/2 \
+ 3*(1-z_4)/2 \
+ 3*(1-z_5)/2 \
+ 1*(1-z_6)/2 \
+ 1*(1-z_7)/2 \
+ 5*(1-z_8)/2 \
+ 1*(1-z_9)/2 \
+ 2*(1-z_10)/2 \
+ P * ((1-z_0)/2 + (1-z_1)/2 + (1-z_2)/2 - 1)**2 \
+ P * ((1-z_8)/2 + (1-z_10)/2 - 1)**2 \
+ P * ((1-z_0)/2 - (1-z_3)/2 - (1-z_4)/2)**2 \
+ P * ((1-z_1)/2 + (1-z_3)/2 - (1-z_5)/2 - (1-z_6)/2)**2 \
+ P * ((1-z_2)/2 + (1-z_4)/2 + (1-z_5)/2 + (1-z_9)/2 - (1-z_7)/2 \
     - (1-z_8)/2)**2 \
+ P * ((1-z_6)/2 + (1-z_7)/2 - (1-z_9)/2 - (1-z_10)/2)**2"

exp2 = "\
- 1*z_0 - 14*z_1 - 43*z_2 - 14.5*z_3 - 42*z_4 - 28.5*z_5 - 0.5*z_6 + 26.5*z_7 \
+ 24.5*z_8 - 27.5*z_9 - 1*z_10 \
+ 13.5*z_0*z_1 \
+ 13.5*z_0*z_2 \
- 13.5*z_0*z_3 \
- 13.5*z_0*z_4 \
+ 13.5*z_1*z_2 \
+ 13.5*z_1*z_3 \
- 13.5*z_1*z_5 \
- 13.5*z_1*z_6 \
+ 13.5*z_2*z_4 \
+ 13.5*z_2*z_5 \
- 13.5*z_2*z_7 \
- 13.5*z_2*z_8 \
+ 13.5*z_2*z_9 \
+ 13.5*z_3*z_4 \
- 13.5*z_3*z_5 \
- 13.5*z_3*z_6 \
+ 13.5*z_4*z_5 \
- 13.5*z_4*z_7 \
- 13.5*z_4*z_8 \
+ 13.5*z_4*z_9 \
+ 13.5*z_5*z_6 \
- 13.5*z_5*z_7 \
- 13.5*z_5*z_8 \
+ 13.5*z_5*z_9 \
+ 13.5*z_6*z_7 \
- 13.5*z_6*z_9 \
- 13.5*z_6*z_10 \
+ 13.5*z_7*z_8 \
-   27*z_7*z_9 \
- 13.5*z_7*z_10 \
- 13.5*z_8*z_9 \
+ 13.5*z_8*z_10 \
+ 13.5*z_9*z_10 \
+ 13.5*z_0**2 \
+ 13.5*z_1**2 \
+ 13.5*z_2**2 \
+ 13.5*z_3**2 \
+ 13.5*z_4**2 \
+ 13.5*z_5**2 \
+ 13.5*z_6**2 \
+ 13.5*z_7**2 \
+ 13.5*z_8**2 \
+ 13.5*z_9**2 \
+ 13.5*z_10**2 \
+ 53.5"

if __name__ == "__main__":
    are_equal()
