def guess(guessed_year, correct_year, years):

    if not years:
        return True
    elif len(years) == 1:
        have_year = int(years[0])
        wrong1 = guessed_year < have_year and correct_year > have_year
        wrong2 = correct_year < have_year and guessed_year > have_year
        if not (wrong1 or wrong2):
            return True
        else:
            return False
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
