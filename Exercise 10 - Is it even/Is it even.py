def check_even_odd(number):
    if number % 2==0:
        return "The number is even."
    else:
        return "The number is odd."
    
def main():
    user_input=input("Enter a number:")
    number=int(user_input)
    result=check_even_odd(number)
    print(result)

if __name__ == "__main__":
    main()
