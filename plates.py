def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return (
        starts_with_two_letters(s)
        and max_six_min_two(s)
        and numbers_only_at_end_and_no_leading_zero(s)
        and no_punct(s)
    )


def starts_with_two_letters(s):
    return s[:2].isalpha()


def max_six_min_two(s):
    return 1 < len(s) < 7


def numbers_only_at_end_and_no_leading_zero(s):

    # find first number

    for i in range(len(s)):
        char = s[i]

        # check it's not 0 and no letters after
        if char.isnumeric():
            if char == "0":
                return False
            return s[i:].isnumeric()

    # if no numbers assume valid
    return True


def no_punct(s):
    return s.isalnum()


if __name__ == "__main__":
    main()
