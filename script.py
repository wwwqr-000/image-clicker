import pyautogui

question_list = ['greencircle', 'redcircle', 'bluesquare', 'redtriangle']

user_input = input('Where should I click? ')

while user_input not in question_list:
    print('Incorrect input, available options: greencircle, redcircle, bluesquare, redtriangle')
    user_input = input('Where should I click?')

location = pyautogui.locateOnScreen(user_input + '.png')
pyautogui.click(location)