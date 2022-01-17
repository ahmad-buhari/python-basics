#practices using modules

import mod_dividen


user_input = ''
while user_input !='q':
  try:
    print('Investment Calculator')
    captial = mod_dividen.get_deposit()
    duration = mod_dividen.get_invest_time()

    #Calculating

    cash_returns = (captial * duration) * 0.5
    print('Return Investment: $',cash_returns)
  
  except ValueError as xxx:
    print(xxx)
    print('Unable to calculate value, please try again')
  
  finally:
    print('\nProcess Completed')
    print(__name__)
  
  user_input = input('\nPress any key to contuine or q to quit\n')

