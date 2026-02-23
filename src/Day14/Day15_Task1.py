import random

actions = ["Click", "Scroll", "Exit"]

S = []
for a1 in actions:
    for a2 in actions:
        S.append((a1, a2))

print("Sample Space S (Two Consecutive Actions):")
print(S)
print("Total Outcomes:", len(S))

E = []
for outcome in S:
    if "Click" in outcome:
        E.append(outcome)

prob_E = len(E) / len(S)

print("\nEvent E (Click at least once):")
print(E)
print("Total Favorable Outcomes:", len(E))
print("Probability of E:", prob_E)

trials = 1000
count_sum_7 = 0

for i in range(trials):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2

    if total == 7:
        count_sum_7 += 1

experimental_probability = count_sum_7 / trials

print("\nDice Simulation Results:")
print("Trials:", trials)
print("Number of times sum is 7:", count_sum_7)
print("Experimental Probability of sum being 7:", experimental_probability)