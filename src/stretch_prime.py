import sys
from typing import List


def check_prime(number: int) -> bool:
    prime = True
    p = 2
    number_set = [x for x in range(2, number + 1)]

    def sift_number_set(start: int, updated_number_set: List[int]) -> List[int]:
        nonlocal prime
        for i in range(start, number + 1, start)[1:]:
            if i in updated_number_set:
                if i == number:
                    prime = False
                else:
                    updated_number_set.remove(i)

        return updated_number_set

    def increment_p(updated_p: int) -> int:
        for val in number_set:
            if val > updated_p:
                return val

    while p < number_set[-1] and prime is True:
        sift_number_set(p, number_set)
        p = increment_p(p)

    return prime


if __name__ == "__main__":
    print(check_prime(int(sys.argv[1])))
