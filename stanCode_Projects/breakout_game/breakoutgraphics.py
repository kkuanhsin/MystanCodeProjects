"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE：
This is a class which build the window, ball, bricks, paddle
of the breakout point.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random


BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a game over sign
        self.over = GLabel(f'GAME OVER :(')
        self.over.font = '-60'
        self.over.color = 'red'

        # Create a win sign
        self.win = GLabel(f'YOU WIN!!!!!')
        self.win.font = '-60'
        self.win.color = 'blue'

        # Create a score sign
        self.score = GLabel(f'Score: {0}')
        self.score.font = '-30'
        self.window.add(self.score, 0, self.window.height)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, (window_width - paddle_width) / 2, window_height-paddle_height - paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.window.add(self.ball, window_width/2 - ball_radius, window_height/2 - ball_radius)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        self.click = False
        onmouseclicked(self.start)
        onmousemoved(self.paddle_move)

        # Draw bricks
        self.brick_rows = BRICK_ROWS
        self.brick_cols = BRICK_COLS
        for i in range(BRICK_ROWS):
            for j in range(BRICK_COLS):
                self.brick = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                self.brick.filled = True

                # change color
                if i < 2:
                    self.brick.fill_color = 'red'
                elif i < 4:
                    self.brick.fill_color = 'orange'
                elif i < 6:
                    self.brick.fill_color = 'yellow'
                elif i < 8:
                    self.brick.fill_color = 'green'
                elif i < 10:
                    self.brick.fill_color = 'blue'

                self.window.add(self.brick, (BRICK_WIDTH+BRICK_SPACING)*j, BRICK_OFFSET+(BRICK_SPACING+BRICK_HEIGHT)*i)

    # paddle will move with the mouse in x
    def paddle_move(self, mouse):
        if mouse.x - PADDLE_WIDTH/2 > 0 and mouse.x + PADDLE_WIDTH/2 < self.window.width:
            self.paddle.x = mouse.x - PADDLE_WIDTH/2

    # when mouse click ball start to move
    def start(self, mouse):
        if not self.click:
            # close the gate if mouseclick
            self.click = True

            self.__dx = random.randrange(1, MAX_X_SPEED)

            # ball will move left or right random
            if random.random() > 0.5:
                self.__dx = - self.__dx

            self.__dy = INITIAL_Y_SPEED

    # getter dx
    def get_dx(self):
        return self.__dx

    # getter dy
    def get_dy(self):
        return self.__dy

    # return True when the ball hits object
    def is_impact_brick(self):
        self.brick = self.window.get_object_at(self.ball.x, self.ball.y) or \
                     self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y) or \
                     self.window.get_object_at(self.ball.x, self.ball.height + self.ball.y) or \
                     self.window.get_object_at(self.ball.x + self.ball.width, self.ball.height + self.ball.y)

        if self.brick is not None:
            return True

    # make a new ball for next round
    def reset_ball(self):
        self.ball = GOval(BALL_RADIUS * 2, BALL_RADIUS * 2)
        self.ball.filled = True
        self.window.add(self.ball, self.window.width / 2 - BALL_RADIUS, self.window.height / 2 - BALL_RADIUS)
        self.__dx = 0
        self.__dy = 0
        self.click = False

    # tell player game is over
    def game_over(self):
        self.window.add(self.over, (self.window.width-self.over.width)/2, self.window.height/2)

    # tell player win the game
    def win_win(self):
        self.window.add(self.win, (self.window.width-self.win.width)/2, self.window.height/2)
