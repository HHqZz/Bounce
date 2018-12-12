
import arcade
import Constants
from Bounce import MyGame

def main():
    window = MyGame(Constants.SCREEN_X, Constants.SCREEN_Y, " Bounce")
    window.setup()
    arcade.finish_render()
    arcade.run()

if __name__ == "__main__":
    main()
