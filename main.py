def reverse_string(s):
    return s[::-1]

if __name__ == "__main__":
    user_input = input("Введіть рядок: ")
    print("Інверсія:", reverse_string(user_input))
