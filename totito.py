class Tree:
    def __init__(self, value):
        self.value = value
        self.winner = -float('inf')
        self.children = []
        
def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]

    return None


def get_empty_cells(board):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                empty_cells.append((i, j))
    return empty_cells

# crea el árbol
def minimax(node, is_maximizing):
    winner = check_winner(node.value)
    
    if winner is not None:
        if winner == "O":
            node.winner = 1
        elif winner == "X":
            node.winner = -1
        return

    if all(cell != "" for row in node.value for cell in row):
        node.winner = 0
        return

    empty_cells = get_empty_cells(node.value)

    for cell in empty_cells:
        new_board = [row[:] for row in node.value]

        if is_maximizing:
            new_board[cell[0]][cell[1]] = "O"
        else:
            new_board[cell[0]][cell[1]] = "X"

        child_node = Tree(new_board)
        node.children.append(child_node)
        minimax(child_node, not is_maximizing)

# chequea si ese arbol lleva a una victoria
def check_best_move(tree, is_maximizing=True):
    if not tree.children:
        return tree.winner
    
    child_values = []
    for child in tree.children:
        child_values.append(check_best_move(child, not is_maximizing))
    
    if is_maximizing:
        tree.winner = max(child_values)
    else:
        tree.winner = min(child_values)
    
    return tree.winner

# obtiene la posición del mejor movimiento
def get_best_move(board_game):
    empty_cells = get_empty_cells(board_game)
    best_move = None
    best_value = -float('inf')

    for cell in empty_cells:
        new_board = [row[:] for row in board_game]
        new_board[cell[0]][cell[1]] = "O"
        
        tree = Tree(new_board)
        minimax(tree, False)

        move_value = check_best_move(tree, False)

        if move_value > best_value:
            best_value = move_value
            best_move = cell

    return best_move

best_move = get_best_move([
    ["X", "O", "X"],
    ["O", "O", "X"],
    ["X", "X", "O"]
])

print(best_move)
