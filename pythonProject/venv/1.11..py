birth = 7
death= 13
immigration = 45
population = 312032486
second_in_a_year = 365 *24 * 60 * 60

firstyear= population + (second_in_a_year// birth)+ (second_in_a_year// immigration) - (second_in_a_year// death)
print("first year's population is", firstyear)
secondyear=firstyear+((second_in_a_year// birth)+ (second_in_a_year//immigration) - (second_in_a_year// death))
print("second  year's population is", secondyear)
thirdyear=secondyear+ ((second_in_a_year// birth)+ (second_in_a_year// immigration) - (second_in_a_year// death))
print("third year's population is", thirdyear)
fourthyear = thirdyear + ((second_in_a_year// birth)+ (second_in_a_year// immigration) - (second_in_a_year// death))
print("fourth year's population is", fourthyear)
fifthyear= fourthyear + ((second_in_a_year// birth)+ (second_in_a_year// immigration) - (second_in_a_year// death))
print("fifth year's population is", fifthyear)

