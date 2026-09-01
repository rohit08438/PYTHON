"""
Calibration Log Synthesizer
Coding for AI - Week 5

Manual backward traversal:
For a batch of length L, the readings are processed from right to left.
The actual index is calculated using:
target_index = batch_length - i

The outer loop uses a walrus-controlled while loop.
A one-item slice of calibration_feed is checked each time.
When feed_cursor reaches the end, the slice becomes empty,
which makes the while condition False automatically.
"""

print("===== CALIBRATION LOG SYNTHESIZER =====")

calibration_feed = [
    [201, 6.0, 9.5, "IGNORE", 4.0],
    [],
    [202, 11.2, "FAULT", 7.8, 5.5],
    [203, 14.0, 3.5, 8.25],
    [204, 2.75, "HALT", 6.0]
]

feed_cursor = 0

total_valid_readings = 0
global_max = None
global_min = None
total_checksum = 0.0

emergency_halt = False


while (current_slice := calibration_feed[feed_cursor:feed_cursor + 1]):

    batch = current_slice[0]

    print()

    # Check for an empty batch
    if not batch:
        print("Batch", feed_cursor, "is EMPTY. Proceeding.")
        feed_cursor += 1
        continue

    calibration_id = batch[0]

    print("Evaluating Batch", feed_cursor, "(ID:", calibration_id, ")...")

    # Manually calculate batch length
    batch_length = 0

    for item in batch:
        batch_length += 1

    batch_sum = 0.0

    # Process readings from right to left
    for i in range(1, batch_length):

        target_index = batch_length - i

        reading = batch[target_index]

        # IGNORE signal
        if reading == "IGNORE":
            print("Signal IGNORE encountered at Batch", calibration_id)
            continue

        # FAULT signal
        if reading == "FAULT":
            print(
                "Signal FAULT detected. Suppressing batch",
                calibration_id
            )
            break

        # HALT signal
        if reading == "HALT":
            print(
                "Signal HALT detected. Executing emergency protocol."
            )

            emergency_halt = True

            break

        # Valid numerical reading
        batch_sum += reading
        total_valid_readings += 1

        # Manual global maximum
        if global_max is None:
            global_max = reading
        elif reading > global_max:
            global_max = reading

        # Manual global minimum
        if global_min is None:
            global_min = reading
        elif reading < global_min:
            global_min = reading

    else:
        # This executes only if the inner loop
        # finishes normally without break.

        if calibration_id % 2 == 0:
            adjusted_sum = batch_sum * 1.5
        else:
            adjusted_sum = batch_sum * 0.8

        total_checksum += adjusted_sum

    # Stop the outer loop if HALT was detected
    if emergency_halt:
        break

    feed_cursor += 1


print()
print("========================================")
print("CALIBRATION COMPLETE :", end=" ")

if emergency_halt:
    print("EMERGENCY TERMINATION")
else:
    print("SUCCESSFULLY")

print("========================================")

print("Total Valid Readings Processed :", total_valid_readings)
print("Global Calibration Checksum :", total_checksum)
print("Maximum Reading Encountered :", global_max)
print("Minimum Reading Encountered :", global_min)
