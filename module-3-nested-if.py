answer_a = input('Do you like travelling? y/n: ')
if answer_a == 'y':
    answer_b = input('And do you like Asia? y/n: ')
    if answer_b == 'y':
        print('Excellent! You can win a ticket to Thailand!')
    else:
        print('Sorry to hear that!')
else:
    print('Sorry to hear that!')


# Ask the user for the necessary information
days_since_purchase = int(input('How many days ago have you purchased the item? '))
used_item = input('Have you used the item at all [y/n]? ')
item_broken = input('Has the item broken down on its own [y/n]? ')

# Determine refund eligibility
if days_since_purchase <= 10 and used_item == 'n':
    print('You can get a refund.')
elif item_broken == 'y':
    print('You can get a refund.')
else:
    print('You cannot get a refund.')
