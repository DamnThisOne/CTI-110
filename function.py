def HATE(num1, num2):
    answer = num1 + num2
    print(f'{num1} + {num2} = {answer}')
    return answer

def checker(name, letter):
    if letter in name:
        return True
    else:
        return False


def main():
    answer1 = HATE(8,4)
    print(answer1)

    HATE(7,4)
    
    checker_result = checker("Jay","J")
    print(checker_result)

if __name__ == "__main__":
    main()