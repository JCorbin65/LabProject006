
def vignere_sq():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    size = len(alphabet)

    print("|   | " + " | ".join(alphabet) + " |")
    print("|---|" + "|".join(["---"] * size) + "|")

    for i in range(size):
        row = alphabet[i:] + alphabet[:i]  # Shift the alphabet for the current row
        print(f"| {alphabet[i]} | " + " | ".join(row) + " |")

vignere_sq()