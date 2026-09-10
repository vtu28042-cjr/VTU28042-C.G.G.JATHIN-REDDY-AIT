R1 = 30
R2 = 70

total = R1 + R2

P1 = R1 / total
P2 = R2 / total

percentage1 = P1 * 100
percentage2 = P2 * 100

print("Path 1 Probability:", percentage1, "%")
print("Path 2 Probability:", percentage2, "%")

if percentage1 > percentage2:
    print("Most ants follow Path 1.")
    print("Path 1 has the higher chance:", percentage1, "%")
else:
    print("Most ants follow Path 2.")
    print("Path 2 has the higher chance:", percentage2, "%")

print("\n----- ANT COLONY PATH GRAPH -----")

print("\nStart")
print("  |")
print("  +-------- Path 1 --> Goal")
print("  |           30%")
print("  |")
print("  +==========================> Goal")
print("              Path 2")
print("              70%")

print("\nProbability Graph:")
print("Path 1 | " + "#" * int(percentage1 / 5) + " 30%")
print("Path 2 | " + "#" * int(percentage2 / 5) + " 70%")

OUTPUT 
Path 1 Probability: 30.0 %
Path 2 Probability: 70.0 %

Most ants follow Path 2.
Path 2 has the higher chance: 70.0 %

----- ANT COLONY PATH GRAPH -----

Start
  |
  +-------- Path 1 --> Goal
  |           30%
  |
  +==========================> Goal
              Path 2
              70%

Probability Graph:
Path 1 | ###### 30%
Path 2 | ############## 70%
