def guess(guessed_year, correct_year, years):

    guessed_index = 0
    correct_index = 0
    years.sort()
    for i in range(len(years)):
        if guessed_year < years[i]:
            guessed_index += 1
        if correct_year < years[i]:
            correct_index += 1
    if guessed_index == correct_index:
        return True
    else:
        return False
