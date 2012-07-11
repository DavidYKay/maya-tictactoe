import sys

NUM_ROWS = 3
NUM_COLUMNS = 3


board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

current_player = 'X'

'''
Print one square, either empty, with an X, or with an O

Examples:
* Empty: [ ]
* X:     [X]
* O:     [O]
'''
def show_square(row, column):
  value = board[row][column]
  return '[ %s ]' % value

def print_board():
  print '----------'
  # print all the squares in the first row
  for row_number in range(0, NUM_ROWS):
    row = ''
    for column_number in range(0, NUM_COLUMNS):
      row += show_square(row_number, column_number)
    print row
  # move to the next row
  # repeat
  print '----------'

def get_distance_from_a(letter):
  return ord(letter.lower()) - ord('a')

def translate_alphabet_to_position(letter):
  # force to be lower case
  column = get_distance_from_a(letter) % (NUM_COLUMNS)
  row    = get_distance_from_a(letter) / (NUM_COLUMNS)

  return (row, column)

def make_move(target_square):
  # translate from ABCDE to (0,0) -> (2,2)
  row, column = translate_alphabet_to_position(target_square)
  print "Moving to row: %d"    % row
  print "Moving to column: %d" % column
  board[row][column] = current_player

def get_next_player(current_player):
  if current_player == 'X':
    return 'O'
  else:
    return 'X'

def detect_winner_horizontal():
  for row in board:
    if row[0] == 'X' and row[1] == 'X' and row[2] == 'X':
      # player X has won!
      print "Congratulations, player X!"
      sys.exit()
  
def detect_winner_vertical():
  pass
def detect_winner_diagonal():
  pass

def detect_winner():
  detect_winner_horizontal()
  detect_winner_vertical()
  detect_winner_diagonal()

while 1 == 1:
  # step 1: show player what the board looks like right now
  print "Player %s's turn." % current_player
  print_board()
  
  # step 2: ask player where he/she wants to move
  print "Where would you like to move?"
  target_square = raw_input()
  print "You wanted to move to: " + target_square
  
  # step 3: take the player's input and fill the square
  make_move(target_square)
  
  # step 4: Repeat for the other player
  current_player = get_next_player(current_player)

  detect_winner()
