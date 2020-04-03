class Scene(object):

    def enter(self):
        pass


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        self.scene_map.opening_scene()

    def next(self):
        self.scene_map.next_scene()


class Death(Scene):

    def enter(self):
        pass


class CentralCorridor(Scene):

    def __init__(self):
        self.next_scene = LaserWeaponArmory

    def enter(self):
        print("Scene 1: This is the Central Corridor")


class LaserWeaponArmory(Scene):

    def __init__(self):
        self.next_scene = TheBridge

    def enter(self):
        print("Scene 2: This is the Laser Weapon Armory")


class TheBridge(Scene):

    def __init__(self):
        self.next_scene = EscapePod

    def enter(self):
        print("Scene 3: This is the Bridge")


class EscapePod(Scene):

    def __init__(self):
        self.next_scene = EndOfGame

    def enter(self):
        print("Scene 4: This is the Escape Pod")


class EndOfGame(Scene):
    
    def enter(self):
        print("End of game. Goodbye")
        exit() 



class Map(object):

    def __init__(self, start_scene):
        self.start_scene = start_scene()
        self.current_scene = self.start_scene

    def next_scene(self):
        self.current_scene = self.current_scene.next_scene()
        self.current_scene.enter()

    def opening_scene(self):
        print("Game introduction text <HERE>")
        self.start_scene.enter()


a_map =  Map(CentralCorridor)


a_game = Engine(a_map)
a_game.play()
a_game.next()
a_game.next()
a_game.next()
a_game.next()










