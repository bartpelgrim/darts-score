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

        self.player_1_score = GAME_STARTING_SCORE
        self.player_2_score = GAME_STARTING_SCORE

    def draw_text(self, player: int, text: str, color):
        if player == 0:
            x, y = 1, 1
        elif player == 1:
            x, y = 1, 17
        else:
            raise ValueError(f'Unknown player, {player}')
        graphics.DrawText(self.matrix, self.font, x, y, color, text)
