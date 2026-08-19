"""
Packet Scrambler
Author: Rohit Singh
"""


# Stage 1: Input Validation and Test Data
packet = [6, 15, 0, 8, 25, 7, 34, 0, 11, 3,1]



if packet and len(packet) >= 10:
    print("Validation passed. Processing packet...")
else:
    print("Validation failed: packet is empty or too short.")


# Stage 2: The "Middle-Out" Swap


midpoint = len(packet) // 2

front_half = packet[:midpoint]
back_half = packet[midpoint:]

scrambled = back_half[::-1] + front_half

print("Original packet:", packet)
print("Front half:", front_half)
print("Back half:", back_half)
print("Scrambled packet:", scrambled)

# Verify that slicing produced new list objects
print("packet and front_half have same ID:", id(packet) == id(front_half))


# Stage 3: In-Place Correction


middle_index = len(scrambled) // 2

if type(scrambled[middle_index]) is int:
    scrambled.insert(middle_index + 1, "SYNC-BIT")

print("After SYNC-BIT insertion:", scrambled)

while 0 in scrambled:
    scrambled.remove(0)

print("After zero removal:", scrambled)


# Stage 4: Memory Integrity Check


first, *middle, last = scrambled

print("Original packet:", packet)
print("Final scrambled packet:", scrambled)

print(
    f"Header: {first} "
    f"Footer: {last} "
    f"Body length: {len(middle)}"
)

print("\nMemory integrity check:")
print("Original packet remains unchanged:", packet)
