import catan
import numpy as np

RESOURCE_NAMES = ["brick", "ore", "hay", "wood", "sheep"]
DEVELOPMENT_CARD_NAMES = ["knight", "victory point",
                          "road building", "year of plenty", "monopoly"]


class CatanPlayer:
    # Initialize the Catan Board with all the options for resources, numbers to be rolled,
    # settlements/roads, port options
    def __init__(self, player_number):
        self.player_number = player_number

        self.hand = {}
        for i in RESOURCE_NAMES:
            self.hand[i] = 0

        self.dev_card = {}
        for i in DEVELOPMENT_CARD_NAMES:
            self.dev_card[i] = 0

    def add_to_hand(self, card):
        self.hand[card] += 1

    def remove_from_hand(self, card):
        self.hand[card] -= 1

    def add_dev(self, card):
        self.dev_card[card] += 1
        if card == DEVELOPMENT_CARD_NAMES[1]:
            catan.player_points[player_number] += 1

    def show_dev(self):
        print('Here are the options:')
        for i in range(1, 6):
            print(i, ': ', DEVELOPMENT_CARD_NAMES[i-1])

    def dev_convert(self, number):
        '''convert from number to dev_card'''
        dev = DEVELOPMENT_CARD_NAMES[number - 1]
        return dev

    def print_hand(self):
        print('Player Number: {}', format(self.player_number))
        for key, value in self.hand.items():
            print(key, value)

    def show_options(self):
        print('Here are the options:')
        for i in range(1, 6):
            print(i, ': ', RESOURCE_NAMES[i-1])

    def convert(self, number):
        '''convert from number to resource'''
        resource = RESOURCE_NAMES[number - 1]
        return resource

    def set_settlement(self, board):
        """
        ################################ Insert/Modify Comments HERE ##################################

        generate buy_settlement input:
        output -- position -- integer 0-53 """
        ################################ Insert/Modify CODE HERE ##################################
        valid_choice = False
        while not valid_choice:
            print('Select an open settlement')
            print(board.get_available_settlements())
            position = int(input('Place your Settlement'))
            if position >= 0 and position <= 53:
                if board.coordinate_list[position].status == "Open":
                    valid_choice = True
                else:
                    print("Position is unavailable")
            else:
                print("Position is invalid")

        return position

    def set_city(self, board):
        """
        ################################ Insert/Modify Comments HERE ##################################

        output -- genererate buy_city arguments:
        position -- integer 0-53
        """
        ################################ Insert/Modify CODE HERE ##################################

        valid_choice = False
        while not valid_choice:
            position = int(input('Place your City'))
            if position >= 0 and position <= 53:
                if board.settlements[position] == self.player_number:
                    valid_choice = True
                else:
                    print("Position is unavailable")
            else:
                print("Position is invalid")

        return position

    def set_road(self, board):
        """
        ################################ Insert/Modify Comments HERE ##################################

        output -- generate buy_road arguments:
        position -- integer 0-71
        """
        ################################ Insert/Modify CODE HERE ##################################
        valid_road = False
        while not valid_road:
            road_position = int(input('Place your Road'))
            if road_position >= 0 and road_position <= 71:
                if board.road_list[road_position].status == "Open":
                    valid_road = True
                else:
                    print("Position is unavailable")
            else:
                print("Position is invalid")

        return road_position

    def turn_choice(self, board):
        """
        ################################ Insert/Modify Comments HERE ##################################

        output -- integer
        0 -- end turn
        see main for more integer - action correspondance

        """
        ################################ Insert/Modify CODE HERE ##################################

        choice = int(input('Please select from the above options'))
        return choice

    def discard_half(self, board):
        """
        ################################ Insert/Modify Comments HERE ##################################
        discard_half output arguments:

        resourses -- np.array([brick, ore, hay, wood, sheep])
                brick -- integer 0-19
                ore -- integer 0-19
                hay -- integer 0-19
                wood --integer 0-19
                sheep --integer 0-19
        """
        ################################ Insert/Modify CODE HERE ##################################

        return np.array([int(input('insert argument')), int(input('insert argument')), int(input('insert argument')),
                         int(input('insert argument')), int(input('insert argument'))])

    def steal_card(self, board):
        """
        ################################ Insert/Modify Comments HERE ##################################
        output
        position -- integer 0 - self.number_of_tiles-1
        target_player_number -- integer 0-3

        """
        ################################ Insert/Modify CODE HERE ##################################
        position, target_player_number = int(
            input('insert argument')), int(input('insert argument'))
        return position, target_player_number

    def play_roads(self, board):
        """

        ################################ Insert/Modify Comments HERE ##################################
        position1 -- integer 0-71
        position2 -- integer 0-71

        """
        ################################ Insert/Modify CODE HERE ##################################

        valid_road_1 = False
        while not valid_road_1:
            road_position_1 = int(input('Place your Road'))
            if road_position_1 >= 0 and road_position_1 <= 71:
                if board.road_list[road_position_1].status == "Open":
                    valid_road_1 = True
                else:
                    print("Position is unavailable")
            else:
                print("Position is invalid")

        valid_road_2 = False
        while not valid_road_2:
            road_position_2 = int(input('Place your Road'))
            if road_position_2 >= 0 and road_position_2 <= 71:
                if board.road_list[road_position_2].status == "Open":
                    valid_road_2 = True
                else:
                    print("Position is unavailable")
            else:
                print("Position is invalid")

        return road_position_1, road_position_2

    def play_plenty(self, board):
        """
        ################################ Insert/Modify Comments HERE ##################################
        resource1 -- integer 1-5
        resource2 -- integer 1-5

        """
        ################################ Insert/Modify CODE HERE ##################################
        print('0: Brick')
        print('1: Ore')
        print('2: Hay')
        print('3: Wood')
        print('4: Sheep')
        resource1, resource2 = int(input('Select a Resource')), int(
            input('Select another Resource'))
        return resource1, resource2

    def play_mono(self, board):
        """
        ################################ Insert/Modify Comments HERE ##################################
        resource -- integer 1-5
        """
        ################################ Insert/Modify CODE HERE ##################################

        return int(input('insert argument'))

    def trade_bank(self, board):
        """
        ################################ Insert/Modify Comments HERE ##################################

        resource_own -- int-resource name
        resource_bank -- int-resource name

        """
        ################################ Insert/Modify CODE HERE ##################################
        self.show_options()
        resource_own, resource_bank = int(input('Select resource to trade in')), int(
            input('insert resource to receive'))
        resources_own = self.convert(resources_own)
        resources_bank = self.convert(resources_bank)
        # validating that player has 4 such cards & bank has 1
        return resource_own, resource_bank

    def trade_offer(self, board):
        """
        ################################ Insert/Modify Comments HERE ##################################
        resources_own -- np.array([brick, ore, hay, wood, sheep])
        target_player_number -- integer 0-3
        resources_target -- np.array([brick, ore, hay, wood, sheep])
                brick -- integer 0-19
                ore -- integer 0-19
                hay -- integer 0-19
                wood --integer 0-19
                sheep --integer 0-19
        """
        ################################ Insert/Modify CODE HERE ##################################
        self.show_options()
        resources_own, amount, resources_target, amount2 = int(input(
            'enter resource you are offering: ')),
        int(input('enter amount of cards: ')), int(input(
            'enter the resource you are asking for: ')), int(input('enter the amount: '))
        resources_own = self.convert(resources_own)
        resources_target = self.convert(resources_target)

        return resources_own, amount, resources_target, amount2

    def trade_answer(self, board, resources_offered, resources_asked):
        """
        output true or false
        ################################ Insert/Modify Comments HERE ##################################
        resources_offered -- np.array([brick, ore, hay, wood, sheep])
        resources_asked -- np.array([brick, ore, hay, wood, sheep])
                """

        return False

    def start_settelment_second(self, board):
        """
                ################################ Insert/Modify Comments HERE ##################################
        output:
            settle_position -- integer 0-53
            road_position integer 0-71
        """
        ################################ Insert/Modify CODE HERE ##################################

        valid_choice = False
        while not valid_choice:
            print('Select an open settlement')
            print(board.get_available_settlements())
            settle_position = int(input('Place your Settlement'))
            if settle_position >= 0 and settle_position <= 53:
                if board.coordinate_list[settle_position].status == "Open":
                    valid_choice = True
                else:
                    print("Position is unavailable")
            else:
                print("Position is invalid")

        # finding roads adjacent to the settlement
        available_roads = []
        for road in board.road_list:
            for key in road.coordinates:
                if road.coordinates[key] == settle_position:
                    available_roads.append(road.index)

        print('please select from the following road options')
        for road in available_roads:
            print(road)

        valid_road = False
        while not valid_road:
            road_position = int(input('Place your Road'))
            if road_position in available_roads and road_position >= 0 and road_position <= 71:
                if board.road_list[road_position].status == "Open":
                    valid_road = True
                else:
                    print("Position is unavailable")
            else:
                print("Position is invalid")

        return settle_position, road_position

    def start_settelment_first(self, board):
        """
                ################################ Insert/Modify Comments HERE ##################################
        output:
            settle_position -- integer 0-53
            road_position integer 0-71
        """
        ################################ Insert/Modify CODE HERE ##################################
        valid_choice = False
        while not valid_choice:
            print('Select an open settlement')
            print(board.get_available_settlements())
            settle_position = int(input('Place your Settlement'))
            if settle_position >= 0 and settle_position <= 53:
                if board.coordinate_list[settle_position].status == "Open":
                    valid_choice = True
                else:
                    print("Position is unavailable")
            else:
                print("Position is invalid")

        # finding roads adjacent to the settlement
        available_roads = []
        for road in board.road_list:
            for key in road.coordinates:
                if road.coordinates[key] == settle_position:
                    available_roads.append(road.index)

        print('please select from the following road options')
        for road in available_roads:
            print(road)

        valid_road = False
        while not valid_road:
            road_position = int(input('Place your Road'))
            if road_position in available_roads and road_position >= 0 and road_position <= 71:
                if board.road_list[road_position].status == "Open":
                    valid_road = True
                else:
                    print("Position is unavailable")
            else:
                print("Position is invalid")

        return settle_position, road_position


if __name__ == '__main__':
    """
    ################################ Insert/Modify Comments HERE ##################################
    """

    ################################ Insert/Modify CODE HERE ##################################
    player = CatanPlayer(0)
    print(player.player_number)
    print('Debug complete')
