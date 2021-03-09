import random
cards_list = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def deal_card():
  card = random.choice(cards_list)
  return int(card)
 
user_cards = []
computer_cards = []
user_total = 0
computer_total = 0
for _ in range(2):
  user_cards.append(deal_card())
  computer_cards.append(deal_card())

print(user_cards)
print(computer_cards[0])
user_total = sum(user_cards)
computer_total = sum(computer_cards)
print(user_total)

if user_total == 21:
    print("YOU WIN!")
elif 11 in user_cards and user_total > 21:
  user_cards.remove(11)
  user_cards.append(1)
  user_total = sum(user_cards)

elif computer_total == 21:
    print("YOU LOOSE!")
    


def calculate_score(user,comp):
    #user_total 
    #computer_total 
  sum = 0
  for num in user:
    sum += num
    if 11 in user and sum > 21:
      user.remove(11)
      user.append(1)
      user = sum(user)
  if user_total == 21:
    print('win')
  elif user_total > 21:
    print("you loose")
  elif user_total > computer_total:
    print('win')
  elif user_total < computer_total:
    print('loose')
  elif user_total == computer_total:
    print('draw')

show = False
while show == False:
  user_choice = input("Do you Like to add 'y' or show your card 's'")
  if user_choice == 'y':
    user_cards.append(deal_card())
    user_total = sum(user_cards)
    print(user_cards)
    print(user_total)
    if 11 in user_cards and user_total > 21:
      user_cards.remove(11)
      user_cards.append(1)
      user_total = sum(user_cards)
    elif user_total > 21:
        print("You Loose!")
        break
    print(user_cards)
    print(user_total)
    
  elif user_choice == 's':
    result = calculate_score(user_cards,computer_cards)
    show = True
  