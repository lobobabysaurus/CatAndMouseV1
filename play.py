from game import CatAndMouseGame

cmg = CatAndMouseGame()
first_run = True
while True:
    cmg.present_menu(not first_run)
    cmg.reset_game()
    cmg.play_game()
    first_run = False
