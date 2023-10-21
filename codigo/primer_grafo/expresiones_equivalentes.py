import itertools


def are_equal(e1, e2, nbits=5, p=27):
    n = nbits
    is_wrong = False
    for z in itertools.product([-1, 1], repeat=n):
        vars = dict()
        for i in range(n):
            vars[f"z_{i}"] = z[i]

        res1 = eval(e1, dict({"P": p}, **vars))
        res2 = eval(e2, vars)
        if res1 != res2:
            is_wrong = True
            print("Error: ", f"{z}", res1, res2)
    if not is_wrong:
        print("Las expresiones son equivalentes")


exp_orig = "\
5*(1 - z_0)/2 + \
8*(1 - z_1)/2 + \
2*(1 - z_2)/2 + \
7*(1 - z_3)/2 + \
4*(1 -  z_4)/2 + \
P * ((1 - z_0)/2 + (1 - z_1)/2 - 1)**2 + \
P * ((1 - z_0)/2 - (1 - z_2)/2 - (1 - z_3)/2)**2 + \
P * ((1 - z_1)/2 + (1 - z_2)/2 - (1 - z_4)/2)**2"

exp_27 = "\
 11   * z_0 \
-17.5 * z_1 \
-28   * z_2 \
-17   * z_3 \
+11.5 * z_4 \
+13.5 * (+ z_0*z_1 - z_0*z_2 - z_0*z_3 + z_1*z_2 \
         - z_1*z_4 + z_2*z_3 - z_2*z_4) \
+(13.5*(z_0**2 + z_1**2 + z_2**2) + 6.75*(z_3**2 + z_4**2)) \
+26.5"


exp_orig_mas_restricc = "\
5*(1 - z_0)/2 + \
8*(1 - z_1)/2 + \
2*(1 - z_2)/2 + \
7*(1 - z_3)/2 + \
4*(1 - z_4)/2 + \
P * ((1 - z_0)/2 + (1 - z_1)/2 - 1)**2 + \
P * ((1 - z_3)/2 + (1 - z_4)/2 - 1)**2 + \
P * ((1 - z_0)/2 - (1 - z_2)/2 - (1 - z_3)/2)**2 + \
P * ((1 - z_1)/2 + (1 - z_2)/2 - (1 - z_4)/2)**2"

exp_27_mas_restricc = "\
11 * z_0 - 17.5 * z_1 - 28 * z_2 - 17 * z_3 + 11.5 * z_4 \
+ 13.5 * (z_0*z_1 + z_1*z_2 + z_2*z_3 - z_0*z_2 - z_0*z_3 + z_3*z_4 \
        - z_1*z_4 - z_2*z_4) \
+ 13.5 * (z_0**2 + z_1**2 + z_2**2 + z_3**2 + z_4**2) \
+ 26.5"


if __name__ == "__main__":
    # Sin restriccion extra
    print("exp_orig == exp_27: ", end="")
    are_equal(exp_orig, exp_27, p=27)

    # Con restriccion extra
    print("exp_orig_mas_restricc == exp_27_mas_restricc: ", end="")
    are_equal(exp_orig_mas_restricc, exp_27_mas_restricc, p=27)
