P = True   # ან False
Q = False  # ან True

P_and_not_Q = P and not Q
not_P_and_Q = not P and Q
P_xor_Q = (P and not Q) or (not P and Q)

print(P_and_not_Q)
print(not_P_and_Q)
print(P_xor_Q)