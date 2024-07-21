card_number = "5011054488597827"

sum_odd_numbers = 0 
sum_even_numbers = 0 

for index, value in enumerate(reversed(card_number)):
    value = int(value)
    if index % 2 == 0:
        sum_odd_numbers += value
    else:
        value = value * 2
        if value >= 10:
            first_number = value // 10
            second_number = value % 10
            sum_even_numbers +=  first_number + second_number
        else:
            sum_even_numbers += value

if(sum_odd_numbers + sum_even_numbers) % 10 == 0:
    print("Karta je platná")
else:
    print("Karta je neplatná")

