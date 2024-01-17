
prods = {"Prd A": 20, "Prd B": 40, "Prd C": 50}

def calc_disc(ct, tq):
    discs = [
        ("f10", 10 if ct > 200 else 0),
        ("b5", 0.05 * tq * prods[max(cart.items(), key=lambda i: i[1][0])[0]]),
        ("b10", 0.1 * ct if tq > 20 else 0),
        ("t50", sum(0.5 * (q - 15) * p for n, (q, p) in cart.items() if q > 15) if tq > 30 else 0)
    ]
    return max(discs, key=lambda d: d[1])

def calc_fees(c):
    gwf = sum(q for n, (q, p, gw) in c.items() if gw)
    sf = 5 * (sum(q for n, (q, p, gw) in c.items()) // 10 + 1)
    return gwf, sf

cart = {}
for n, p in prods.items():
    q = int(input(f"Enter qty for {n}: "))
    gw = input(f"Wrap {n} as gift? (y/n): ").lower() == "y"
    cart[n] = (q, p, gw)

st = sum(q * p for n, (q, p, gw) in cart.items())
dn, da = calc_disc(st, sum(q for n, (q, p, gw) in cart.items()))
gwf, sf = calc_fees(cart)
tot = st - da + gwf + sf

print("\nOrder Summary:")
for n, (q, p, gw) in cart.items():
    print(f"{n}: {q} units, Total: ${q * p:.2f}")
print(f"Subtotal: ${st:.2f}")
print(f"Discount ({dn}): -${da:.2f}")
print(f"Gift Wrap Fee: ${gwf:.2f}")
print(f"Shipping Fee: ${sf:.2f}")
print(f"Total: ${tot:.2f}")

