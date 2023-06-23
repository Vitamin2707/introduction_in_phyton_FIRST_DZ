def puzzle(text: str, answers: list[str], try_count: int) -> int:
    print(text)
    count_trying = 1

    while count_trying <= try_count:
        answer = input("Что это? ")
        if answer in answers:
            break
        if count_trying != try_count:
            print("Не угадали, пробуем еще раз")
        count_trying += 1
    else:
        count_trying = 0

    return count_trying