# task1 : Exploring Pseudo-Randomness and Collision Resistance.
# Ethan Swenke and HanYu Wu
# CSC-321-03

from Crypto.Hash import SHA256
import random
import string
import matplotlib.pyplot as plt
import time


def custom_hash(data, truncate_bits: int):
    hasher = SHA256.new()
    hasher.update(data)
    truncate_bytes = (truncate_bits + 7) // 8
    truncated_digest = hasher.digest()[:truncate_bytes]

    excess_bits = truncate_bytes * 8 - truncate_bits
    if excess_bits > 0:
        truncated_digest = bytearray(truncated_digest)
        truncated_digest[-1] &= 0xFF << excess_bits
        truncated_digest = bytes(truncated_digest)
    return truncated_digest


def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


def find_collision(bits: int):
    hash_values = set()
    attempts = 0
    while True:
        random_str = generate_random_string(64)
        hashed = custom_hash(random_str.encode(), bits)
        attempts += 1
        if hashed in hash_values:
            return random_str, hashed, attempts
        else:
            hash_values.add(hashed)


def task_b():
    string1 = "a"
    string2 = "b"
    for _ in range(3):
        print(string1)
        hash1 = custom_hash(string1.encode(), 256)
        print(hash1)
        print(string2)
        hash2 = custom_hash(string2.encode(), 256)
        print(hash2)
        string1 = chr(ord(string1) + 2)
        string2 = chr(ord(string2) + 2)


def task_c():
    with open("bit_collision.txt", "w") as f:
        for bits in range(8, 51, 2):
            start_time = time.time()
            original_str, hashed, attempts = find_collision(bits)
            end_time = time.time()
            f.write(f"{bits} {end_time - start_time} {attempts}\n")
            print(f"Bits: {bits}")
            print(f'Original: {original_str}')
            print(f'Hash: {hashed}')


def visualize_data():
    digest_sizes, times, num_inputs = read_data_from_file()

    plt.figure(figsize=(10, 5))
    plt.plot(digest_sizes, times, marker='o')
    plt.title('Digest Size vs Collision Time')
    plt.xlabel('Digest Size (bits)')
    plt.ylabel('Collision Time (seconds)')
    plt.grid(True)
    plt.savefig("collision_time_graph.png")
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.plot(digest_sizes, num_inputs, marker='o')
    plt.title('Digest Size vs Number of Inputs')
    plt.xlabel('Digest Size (bits)')
    plt.ylabel('Number of Inputs')
    plt.grid(True)
    plt.savefig("num_inputs_graph.png")
    plt.show()

def read_data_from_file():
    digest_sizes, times, num_inputs = [], [], []
    try:
        with open("bit_collision.txt", "r") as f:
            for line in f:
                bits, time_taken, attempts = map(float, line.split())
                digest_sizes.append(bits)
                times.append(time_taken)
                num_inputs.append(attempts)
    except FileNotFoundError:
        print("Data file not found. Run task_c() to generate data.")
    return digest_sizes, times, num_inputs


if __name__ == "__main__":
    task_b()
    task_c()
    visualize_data()