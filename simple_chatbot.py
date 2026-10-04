# Simple Chatbot
bot_name: str = 'Bot'
print(f'Hello, I\'m {bot_name}! How may I assist you today?')
print('command - [hi],[add],[sub],[mul],[div],[bye]')

while True:
    user_input: str = input('You: ').lower()
    
    if user_input in ['hi', 'hallo', 'halo', 'hai']:
        print(f'{bot_name}: Hi there! How can I help you?')
    elif user_input in ['bye', 'goodbye', 'see you']:
        print(f'{bot_name}: Goodbye! Have a great day!')
        exit()
    elif user_input in ['+', 'add']:
        print(f'{bot_name}: Sure! Let\'s do some addition! Please enter two numbers.')
        try:
            num1: float = float(input('First number: '))
            num2: float = float(input('Second number: '))
            print(f'{bot_name}: The sum is {num1 + num2}')
        except ValueError:
            print(f'{bot_name}: Oops! It seems you input invalid number. Please try again!')
    elif user_input in ['i', 'sub']:
        print(f'{bot_name}: Sure! Let\'s do some substraction! Please enter two numbers.')
        try:
            num1: float = float(input('First number: '))
            num2: float = float(input('Second number: '))
            print(f'{bot_name}: The substraction result is {num1 - num2}')
        except ValueError:
            print(f'{bot_name}: Oops! It seems you input invalid number. Please try again!')
    elif user_input in ['*', 'mul']:
        print(f'{bot_name}: Sure! Let\'s do some multiplication! Please enter two numbers.')
        try:
            num1: float = float(input('First number: '))
            num2: float = float(input('Second number: '))
            print(f'{bot_name}: The multiplication result is {num1 * num2}')
        except ValueError:
            print(f'{bot_name}: Oops! It seems you input invalid number. Please try again!')
    elif user_input in ['/', 'div']:
        print(f'{bot_name}: Sure! Let\'s do some division! Please enter two numbers.')
        try:
            num1: float = float(input('First number: '))
            num2: float = float(input('Second number: '))
            print(f'{bot_name}: The division result is {num1 / num2}')
        except ValueError:
            print(f'{bot_name}: Oops! It seems you input invalid number. Please try again!')
    else:
        print(f'{bot_name}: I\'m sorry, I don\'t understand that. Please try again!')