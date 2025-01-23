def process_numbers(numbers):
    vysledek = []
    for num in numbers:
        if num == 10:
            break
        if num > 5:
            vysledek.append(num * 2)
    return vysledek
    pass

def test_process_numbers():
    assert process_numbers([1, 6, 3, 10, 8]) == [12]
    assert process_numbers([7, 8, 10, 12]) == [14, 16]
    assert process_numbers([1, 2, 3, 4]) == []
    assert process_numbers([5, 6, 7, 15]) == [12, 14, 30]


if __name__ == "__main__":
    test_process_numbers()
    print("Test proběhl v pořádku")