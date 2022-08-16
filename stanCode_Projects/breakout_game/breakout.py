"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE:
This program will let the ball move and bounce when it hit bricks or paddle,
the hit brick will be removed, player have NUM_LIVES to let the ball out of the bottom of the window,
when they died, show GAME OVER, when they hit a brick, score will plus one.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    score = 0

    # count how many bricks
    end_score = graphics.brick_cols * graphics.brick_rows

    # The animation loop !

    while True:
        dx = graphics.get_dx()
        dy = graphics.get_dy()

        # when no lives, game over
        if lives == 0:
            graphics.window.clear()
            graphics.game_over()
            break

        # when no bricks, game over
        if score == end_score:
            graphics.window.clear()
            graphics.win_win()
            break

        while dx != 0 and dy != 0:
            graphics.ball.move(dx, dy)

            # when ball touch the side of the window
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                dx = -dx
            if graphics.ball.y <= 0:
                dy = -dy
            # when ball is out of the bottom of the window
            if graphics.ball.y >= graphics.window.height:
                graphics.window.remove(graphics.ball)
                graphics.reset_ball()
                lives -= 1
                break

            # if ball hits brick
            if graphics.is_impact_brick():
                if graphics.brick is not graphics.paddle:
                    if graphics.brick is not graphics.score:
                        graphics.window.remove(graphics.brick)
                        score += 1
                        graphics.score.text = f'Score: {score}'
                        dy = -dy

                    # no more bricks
                    if score == end_score:
                        print('over')
                        graphics.window.remove(graphics.ball)
                        graphics.reset_ball()
                        break

                # when ball hit paddle only move upward
                else:
                    if dy > 0:
                        dy = -dy

            pause(FRAME_RATE)

        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
