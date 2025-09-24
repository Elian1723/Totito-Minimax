import tkinter as tk
from tkinter import ttk, messagebox
from minimax import Minimax

class TotitoUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Totito")
        self.resizable(False, False)
        self.minimax = Minimax()
        self.board = [["", "", ""],
                      ["", "", ""],
                      ["", "", ""]]
        self.game_over = False
        self.create_widgets()

    def create_widgets(self):
        self.board_frame = ttk.Frame(self)
        self.board_frame.grid(row=0, column=0, padx=10, pady=10)
        self.buttons = []

        for i in range(3):
            row = []
            for j in range(3):
                btn = ttk.Button(self.board_frame, text="", width=6, command=lambda x=i, y=j: self.mark_cell(x, y))
                btn.grid(row=i, column=j, padx=5, pady=5)
                row.append(btn)
            self.buttons.append(row)

        self.reset_button = ttk.Button(self, text="Reiniciar", command=self.reset_board)
        self.reset_button.grid(row=1, column=0, pady=(0, 10))

    def check_winner(self):
        return self.minimax.check_winner(self.board)
    
    def ai_move(self):
        """Ejecuta el movimiento de la IA usando minimax"""
        if self.game_over:
            return
            
        best_move = self.minimax.get_best_move(self.board)
        
        if best_move:
            i, j = best_move
            # Actualizar la matriz board
            self.board[i][j] = "O"
            # Actualizar el botón visual
            btn = self.buttons[i][j]
            btn['text'] = "O"
            btn.state(['disabled'])
            
            # Verificar si O ganó o hay empate
            winner = self.check_winner()
            if winner:
                self.show_winner(winner)
    
    def get_board_state(self):
        """Devuelve una copia del estado actual del tablero"""
        return [row[:] for row in self.board]
    
    def is_board_full(self):
        """Verifica si el tablero está lleno"""
        return all(cell != "" for row in self.board for cell in row)
    
    def show_winner(self, winner):
        """Muestra el mensaje del ganador y termina el juego"""
        self.game_over = True
        self.disable_all_buttons()
        
        if winner == "X":
            message = "¡Felicidades! Has ganado"
            title = "Victoria del Jugador"
        elif winner == "O":
            message = "La IA ha ganado \n¡Suerte la próxima vez!"
            title = "Victoria de la IA"
        elif winner == "A":
            message = "¡Es un empate!"
            title = "Empate"
        else:
            message = f"Juego terminado\nGanador: {winner}"
            title = "Fin del juego"
            
        messagebox.showinfo(title, message)
    
    def disable_all_buttons(self):
        """Deshabilita todos los botones del tablero"""
        for row in self.buttons:
            for btn in row:
                btn.state(['disabled'])

    def mark_cell(self, i, j):
        # Verificar si el juego ya terminó o la casilla está ocupada
        if self.game_over or self.board[i][j] != "":
            return
            
        # Actualizar la matriz board con X (jugador humano)
        self.board[i][j] = "X"
        # Actualizar el botón visual
        btn = self.buttons[i][j]
        btn['text'] = "X"
        btn.state(['disabled'])
        
        # Verificar si X ganó
        winner = self.check_winner()
        if winner:
            self.show_winner(winner)
            return
            
        # Turno de la IA (O)
        self.ai_move()

    def reset_board(self):
        # Resetear la matriz board
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ""
        
        # Resetear los botones visuales
        for row in self.buttons:
            for btn in row:
                btn['text'] = ""
                btn.state(['!disabled'])
                
        # Resetear el estado del juego
        self.game_over = False

if __name__ == "__main__":
    app = TotitoUI()
    app.mainloop()