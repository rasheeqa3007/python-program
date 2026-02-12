def anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    s1_sorted = sorted(s1)
    s2_sorted = sorted(s2)
    return s1_sorted == s2_sorted


if __name__ == "__main__":
    s1 = "rain"
    s2 = "ainr"
    if anagram(s1, s2):
        print("it is anagram")
    else:
        print("it is not a anagram")
