def main():
    user_input = int(input("Enter the number: "))
    print(square(user_input))

def square(num):
    return num * num

if __name__ == "__main__":
    main()