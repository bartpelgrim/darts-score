from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics


class MatrixDriver:
    def __init__(self):
        options = RGBMatrixOptions()
        options.rows = 32
        options.chain_length = 1
        options.parallel = 1
        options.hardware_mapping = 'adafruit-hat'
        options.brightness = 50

        self.matrix = RGBMatrix(options=options)

        self.font = graphics.Font()
        self.font.LoadFont('/home/pi/rpi-rgb-led-matrix/fonts/6x12.bdf')

    def draw_text(self, player: int, text: str, color=graphics.Color(255, 0, 0)):
        if player == 0:
            x, y = 0, 9
        elif player == 1:
            x, y = 0, 18
        else:
            raise ValueError(f'Unknown player, {player}')
        graphics.DrawText(self.matrix, self.font, x, y, color, text)

    def draw_active_player(self, player: int):
        if player == 0:
            x, y = 29, 9
        elif player == 1:
            x, y = 29, 18
        else:
            raise ValueError(f'Unknown player, {player}')
        graphics.DrawText(self.matrix, self.font, x, y, graphics.Color(255, 0, 0), '<')

    def draw_games_won(self, won1, won2):
        graphics.DrawText(self.matrix, self.font, 0, 27, graphics.Color(255, 0, 0), f'G:{won1}-{won2}')
