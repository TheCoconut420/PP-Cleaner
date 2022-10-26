from DukeDrawer import DukeBallDrawer


if __name__ == '__main__':
    duke_ball_drawer = DukeBallDrawer()
    duke_ball_drawer.load('szut.bmp')
    print(duke_ball_drawer)
    duke_ball_drawer.save('test.bmp')
    duke_ball_drawer.load('test.bmp')
    print(duke_ball_drawer)