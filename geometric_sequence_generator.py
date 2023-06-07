def generator(n0: int, g_of_n0: float, n1: int, g_of_n1: float):
    n = sorted([n0, n1])
    mapped = {n0: g_of_n0, n1: g_of_n1}

    print(f"r^({n[1] - n[0]}) = g({n1})/g({n0})")
    print(f"r^({n[1] - n[0]}) = {mapped[n1]}/{mapped[n0]}")
    r = f"({mapped[n1]}/{mapped[n0]})^(1/{n[1] - n[0]})"
    print(f"r = {r}")

    gn = f"{mapped[n[0]]}*(r^(n-{n[0]}))"
    print(f"g(n) = {gn}")

    gn = f"{mapped[n[0]]}*(({r})^(n-{n[0]}))"
    print(f"g(n) = {gn}")

    return gn
