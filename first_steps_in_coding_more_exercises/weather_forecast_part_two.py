degrees = float(input())

if degrees > 35:
    print("unknown")
elif degrees >= 26:
    print("Hot")
elif degrees >= 20.1:
    print("Warm")
elif degrees >= 15:
    print("Mild")
elif degrees >= 12:
    print("Cool")
elif degrees >= 5:
    print("Cold")
else:
    print("unknown")
