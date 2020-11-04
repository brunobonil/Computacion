class TaTeTi():
    def __init__(self, board={}, valid=[], piece=''):
        self.board = {'1.1': '1.1', '1.2': '1.2', '1.3': '1.3',
                      '2.1': '2.1', '2.2': '2.2', '2.3': '2.3',
                      '3.1': '3.1', '3.2': '3.2', '3.3': '3.3'}
        self.valid = ['1.1', '1.2', '1.3',
                      '2.1', '2.2', '2.3',
                      '3.1', '3.2', '3.3']
        self.piece = ''

    def __str__(self):
        tabla_inicial = '1.1|1.2|1.3\n---+---+---\n2.1|2.2|2.3\n'
        tabla_inicial += '---+---+---\n3.1|3.2|3.3'
        return tabla_inicial

    def game(self):
        print(self)
        while not self.win() and len(self.valid) > 0:
            self.board[self.input_position()] = ' ' + self.piece + ' '
            print(self)
            winner = self.piece
            self.piece = 'o' if self.piece == 'x' else 'x'
        if len(self.valid) == 0:
            winner = 'Ninguno'
        return winner

    def input_position(self):
        while True:
            posicion = input("Ingrese la posicion a colocar la ficha: ")
            if posicion in self.valid:
                for x in self.valid:
                    if posicion == x:
                        self.valid.remove(x)
                break
        return posicion

    def win(self):
        if (self.board['1.1'] == self.board['2.2'] == self.board['3.3']):
            return True
        if (self.board['1.1'] == self.board['1.2'] == self.board['1.3']):
            return True
        if (self.board['2.1'] == self.board['2.2'] == self.board['2.3']):
            return True
        if (self.board['3.1'] == self.board['3.2'] == self.board['3.3']):
            return True
        if (self.board['1.1'] == self.board['2.1'] == self.board['3.1']):
            return True
        if (self.board['1.2'] == self.board['2.2'] == self.board['3.2']):
            return True
        if (self.board['1.3'] == self.board['2.3'] == self.board['3.3']):
            return True
        if (self.board['3.1'] == self.board['2.2'] == self.board['1.3']):
            return True
        return False


if __name__ == '__main__':
    game = TaTeTi()

    print('Ganó ' + game.game())
