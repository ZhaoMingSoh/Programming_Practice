# Whenever we're dealing with strings or characters lexicographical ordering, use comparator.
def isAlienSorted(words: list[str], order: str) -> bool:
    # We're always going to compare 2 words at once
    for i in range(1,len(words)):
        # If the ascii val difference between the words is :
        #   - +, w1 > w2, therefore w1 should come after w2, wrong ordering
        if compare(words[i-1], words[i], order) > 0:
            return False
    # - -, w1 < w2, therefore they are in the correct ordering
    # - 0, w1 == w2, therefore either ordering does not matter
    return True

def compare(w1,w2, order):
        ptr1 = 0
        ptr2 = 0

        char_compare_val = 0 # track the difference in ascii val

        # loop through each char individually and compare the chars that are in the same index.
        while ptr1 < len(w1) and ptr2 < len(w2) and char_compare_val == 0:
            # Find the char relative ascii value via its index val in the order list.
            char_compare_val = order.find(w1[ptr1]) - order.find(w2[ptr2])
            ptr1 += 1
            ptr2 += 1

        # If all of the characters of the 2 words are the same, then we check which one is longer.
        # - +, len(w1) > len(w2), wrong ordering
        # - -, len(w1) < len(w2), correct ordering
        if char_compare_val == 0:
            return len(w1) - len(w2)
        else:
            return char_compare_val

if __name__ == "__main__":
    words = ["hello","leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"

    print(f"Are the words : {words} order lexicographically ? {isAlienSorted(words, order)}")
    print(f'Are the words : {["word","world","row"]} order lexicographically ? {isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz")}')
    print(f'Are the words : {["apple","app"]} order lexicographically ? {isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz")}')
