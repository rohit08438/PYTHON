
"""
Data Rotation Engine Pipeline
Author: ROHIT KUMAR SINGH
Date: 19-08-2026
"""


print("--- Stage 1: Input Validation and Test Data ---")

# Hard-coded packet with 13 elements and two zeros
packet = [14, 27, 0, 6, 31, 18, 42, 9, 0, 23, 35, 11, 28]

if packet and len(packet) >= 10:
    print("Validation passed. Processing packet...")
else:
    print("Validation failed: packet is empty or too short.")


print("\n--- Stage 2: The 'Middle-Out' Swap ---")

midpoint = len(packet) // 2
front_half = packet[:midpoint]
back_half = packet[midpoint:]

# Build the new scrambled list
scrambled = back_half[::-1] + front_half

print(f"Scrambled list: {scrambled}")

# Verify non-destructiveness
print(
    f"Memory check (id(packet) == id(front_half)): "
    f"{id(packet) == id(front_half)} (Expect: False)"
)


print("\n--- Stage 3: In-Place Correction ---")

middle_index = len(scrambled) // 2

# Insert SYNC-BIT if the middle element is an integer
if type(scrambled[middle_index]) is int:
    scrambled.insert(middle_index + 1, "SYNC-BIT")

# Remove all zeros in-place
while 0 in scrambled:
    scrambled.remove(0)

print(f"List after in-place correction: {scrambled}")


print("\n--- Stage 4: Memory Integrity Check ---")

# Print original and final lists side by side
print(f"Original packet: {packet}")
print(f"Final scrambled: {scrambled}")

# Multiple assignment unpacking
first, *middle, last = scrambled

print(
    f"Header: {first} | "
    f"Footer: {last} | "
    f"Body length: {len(middle)}"
)


def scramble(packet):
    """
    Takes a data packet, applies a middle-out swap, inserts a SYNC-BIT,
    and removes all zeros in-place. Returns the final scrambled list.
    """

    # Stage 1: Validation
    if not (packet and len(packet) >= 10):
        print("Validation failed: packet is empty or too short.")
        return None

    # Stage 2: The "Middle-Out" Swap
    midpoint = len(packet) // 2
    front_half = packet[:midpoint]
    back_half = packet[midpoint:]

    scrambled = back_half[::-1] + front_half

    # Stage 3: In-Place Correction
    middle_index = len(scrambled) // 2

    if type(scrambled[middle_index]) is int:
        scrambled.insert(middle_index + 1, "SYNC-BIT")

    while 0 in scrambled:
        scrambled.remove(0)

    # Return the final list instead of printing stages
    return scrambled


# --- Edge Case Testing ---

print("\n--- Stretch Goal Tests ---")


# Test 1: Standard Packet (13 elements)
test_1 = [14, 27, 0, 6, 31, 18, 42, 9, 0, 23, 35, 11, 28]

print(f"Test 1 (Standard): {scramble(test_1)}")


# Test 2: Odd-length Packet (11 elements)
test_2 = [3, 16, 0, 25, 8, 41, 12, 7, 0, 29, 35]

print(f"Test 2 (Odd length): {scramble(test_2)}")


# Test 3: No zeros at all
test_3 = [11, 24, 37, 5, 18, 42, 9, 26, 33, 15]

print(f"Test 3 (No zeros): {scramble(test_3)}")
