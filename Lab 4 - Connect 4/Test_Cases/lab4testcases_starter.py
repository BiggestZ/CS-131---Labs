from connect_four import str_to_board, print_board, has_connect_four, lowest_empty_row

def function_incorrect(board, test_feedback):
    test_feedback.write("Failed on " + str(board))
    #print("FAIL on ")
    #print_board(board)
    return
    
def test_passed(test_feedback):

    test_result = True
    
    # HAS_CONNECT_FOUR TEST CASES

    board = str_to_board('''
    0  | _  _  _  _  _  _  _ |
    1  | _  _  _  _  _  _  _ |
    2  | _  _  _  _  _  _  _ |
    3  | _  _  _  _  _  _  _ |
    4  | _  _  _  _  _  _  _ |
    5  | _  _  _  _  _  _  _ |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if has_connect_four(board):
        function_incorrect(board, test_feedback)
        test_result = False
  

    board = str_to_board('''
    0  | _  _  _  _  _  _  _ |
    1  | _  _  _  _  _  _  _ |
    2  | _  _  _  O  X  _  _ |
    3  | _  _  O  X  X  O  X |
    4  | _  _  X  O  O  O  X |
    5  | _  X  X  O  O  X  O |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if not has_connect_four(board):
        function_incorrect(board)
        test_result = False
        
    board = str_to_board('''
    0  | O  O  O  O  O  O  O |
    1  | O  _  _  _  _  _  O |
    2  | O  _  _  _  _  _  O |
    3  | O  _  _  _  _  _  O |
    4  | O  _  _  _  _  _  O |
    5  | O  O  O  O  O  O  O |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if not has_connect_four(board):
        function_incorrect(board, test_feedback)
        test_result = False
    
    board = str_to_board('''
    0  | _  _  _  _  _  _  _ |
    1  | _  _  _  _  _  _  _ |
    2  | _  _  _  _  _  _  _ |
    3  | _  X  _  _  _  _  _ |
    4  | _  X  _  _  _  _  _ |
    5  | O  X  O  O  O  O  X |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if not has_connect_four(board):
        function_incorrect(board, test_feedback)
        test_result = False
    
    board = str_to_board('''
    0  | O  X  O  X  O  X  O |
    1  | X  O  X  O  X  O  X |
    2  | O  X  O  X  O  X  O |
    3  | X  O  X  O  X  O  X |
    4  | O  X  X  X  X  O  O |
    5  | X  O  X  O  X  O  X |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if not has_connect_four(board):
        function_incorrect(board, test_feedback)
        test_result = False

    board = str_to_board('''
    0  | O  X  O  X  O  X  O |
    1  | X  O  X  O  X  O  X |
    2  | O  X  O  X  O  X  O |
    3  | O  O  X  O  X  O  X |
    4  | O  X  O  X  O  X  O |
    5  | O  O  X  O  X  O  X |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if not has_connect_four(board):
        function_incorrect(board, test_feedback)
        test_result = False
 
    # LOWEST_EMPTY_ROW TEST CASES

    board = str_to_board('''
    0  | _  _  _  _  _  _  _ |
    1  | _  _  _  _  _  _  _ |
    2  | _  _  _  _  _  _  _ |
    3  | _  _  _  _  _  _  _ |
    4  | _  _  _  _  _  _  _ |
    5  | _  _  _  _  _  _  _ |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if lowest_empty_row(board, 0) != 5:
        function_incorrect(board, test_feedback)
        test_result = False

    board = str_to_board('''
    0  | O  O  O  O  O  O  O |
    1  | O  O  O  O  O  O  O |
    2  | O  O  O  O  O  O  O |
    3  | O  O  O  O  O  O  O |
    4  | O  O  O  O  O  O  O |
    5  | O  O  O  O  O  O  O |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if lowest_empty_row(board, 0) != -1:
        function_incorrect(board, test_feedback)
        test_result = False
    
    return test_result

    board = str_to_board('''
    0  | O  O  O  _  O  O  O |
    1  | O  O  O  _  O  O  O |
    2  | O  O  O  _  O  O  O |
    3  | O  O  O  _  O  O  O |
    4  | O  O  O  _  O  O  O |
    5  | O  O  O  _  O  O  O |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if lowest_empty_row(board, 3) != 5:
        function_incorrect(board, test_feedback)
        test_result = False
    
    return test_result

    board = str_to_board('''
    0  | _  _  _  _  O  O  O |
    1  | _  _  _  _  O  O  O |
    2  | _  _  _  _  O  O  O |
    3  | _  _  _  _  O  O  O |
    4  | _  _  _  _  O  O  O |
    5  | O  O  O  O  O  O  O |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if lowest_empty_row(board, 2) != 4:
        function_incorrect(board, test_feedback)
        test_result = False
    
    return test_result

    board = str_to_board('''
    0  | _  _  _  _  O  O  O |
    1  | _  O  _  _  O  O  O |
    2  | _  O  _  _  O  O  O |
    3  | O  O  _  _  O  O  O |
    4  | O  O  _  _  O  O  O |
    5  | O  O  O  O  O  O  O |
       +---------------------+
         0  1  2  3  4  5  6
    ''')
    if lowest_empty_row(board, 1) != 0:
        function_incorrect(board, test_feedback)
        test_result = False
    
    return test_result
            
