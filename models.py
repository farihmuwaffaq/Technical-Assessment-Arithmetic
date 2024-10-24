def generate_arithmetic_sequence(n, start=2, step=3):
    sequence = []
    for i in range(n):
        sequence.append(start + i * step)
    return sequence

if __name__ == "__main__":
    n = int(input("Masukkan jumlah bilangan: "))
    result = generate_arithmetic_sequence(n)
    print(", ".join(map(str, result)))
