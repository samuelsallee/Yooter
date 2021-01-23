import header


class things_to_buy:
    def __init__(self):
        self.cost: float = 0


class placeable(things_to_buy):
    def __init__(self, player, mouse):
        self.x: int = mouse[0]
        self.y: int = mouse[1]
        self.overall_x = player.overall_position_x + mouse[0] - player.position_x
        self.overall_y = player.overall_position_y - mouse[1] - player.position_y
