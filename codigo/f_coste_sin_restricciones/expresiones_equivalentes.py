import itertools


def are_equal(e1, e2, nbits=5):
    n = nbits
    is_wrong = False
    for z in itertools.product([-1, 1], repeat=n):
        vars = dict()
        for i in range(n):
            vars[f"z_{i}"] = z[i]

        res1 = eval(e1, vars)
        res2 = eval(e2, vars)
        if res1 != res2:
            is_wrong = True
            print("Error: ", f"{z}", res1, res2)
    if not is_wrong:
        print("Las expresiones son equivalentes")


# nbits = 4
exp_qubo = "-7*x_0 + 3*x_1 + 5*x_2 - 4*x_3"
exp_orig = "-7*(1 - z_0)/2 + 3*(1 - z_1)/2 + 5*(1 - z_2)/2 - 4*(1 - z_3)/2"

exp = "3.5*z_0 - 1.5*z_1 - 2.5*z_2 + 2*z_3 - 1.5"

if __name__ == "__main__":
    print("exp_orig == exp_27: ", end="")
    are_equal(exp_orig, exp, nbits=4)
