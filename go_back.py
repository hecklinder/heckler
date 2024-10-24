import time
import random

# Constants
WINDOW_SIZE = 4
TOTAL_FRAMES = 10
TIMEOUT = 2

def send_frame(frame_number):
    print(f"Sender: Sending frame {frame_number}")
    return random.random() > 0.2  # 80% chance of success

def receive_ack(frame_number):
    ack_received = random.random() > 0.1  # 90% chance of ACK success
    if ack_received:
        print(f"Receiver: Acknowledged frame {frame_number}")
    else:
        print(f"Receiver: No ACK for frame {frame_number} (timeout)")
    return ack_received

def go_back_n_protocol():
    current_frame = 0

    while current_frame < TOTAL_FRAMES:
        # Send frames in the window
        for i in range(current_frame, min(current_frame + WINDOW_SIZE, TOTAL_FRAMES)):
            if send_frame(i + 1):  # Sending frame
                if not receive_ack(i + 1):  # Check for acknowledgment
                    print("Sender: Timeout occurred, resending frames.")
                    break
            else:
                print("Sender: Failed to send frame. Will resend.")
                break

        # Simulate timeout and go back
        current_frame += 1
        time.sleep(TIMEOUT)

if __name__ == "__main__":
    go_back_n_protocol()
