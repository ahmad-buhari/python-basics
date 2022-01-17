#practice custom function

def get_deposit():
  cash_input = int(input('Enter Starting Capital\n$'))
  if cash_input < 100:
    raise ValueError('Value Can be less then $100')
  return cash_input

def get_invest_time():
  invest_t = int(input('Enter Duration of Investment in months\n')) 
  if invest_t < 6:
    raise ValueError('Duration to small\n')
  return invest_t




