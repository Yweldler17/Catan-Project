import catan
import numpy as np

RESOURCE_NAMES = ["brick", "ore", "hay", "wood", "sheep"]


class CatanPlayer:
    # Initialize the Catan Board with all the options for resources, numbers to be rolled,
    # settlements/roads, port options
    def __init__(self, player_number):
        self.player_number = player_number
        self.hand = {}
        for i in RESOURCE_NAMES:
            self.hand[i] = 0

    def add_to_hand(self, card):
        self.hand[card] += 1

    def set_settlement(self, board):
        """
        ################################ Insert/Modify Comments HERE ##################################

        generate buy_settlement input:
        output -- position -- integer 0-54 """
        ################################ Insert/Modify CODE HERE ##################################
        position = int(input('Insert settlement you wish to buy. 0-54'))
        return position

    def set_city(self, board):
        """
        ################################ Insert/Modify Comments HERE ##################################

        output -- genererate buy_city arguments:
        position -- integer 0-53
        """
        ################################ Insert/Modify CODE HERE ##################################

        position = int(input('insert argument'))
        return position

    def set_road(self, board):
        """
        ################################ Insert/Modify Comments HERE ##################################

        output -- generate buy_road arguments:
        position -- integer 0-71
        """
        ################################ Insert/Modify CODE HERE ##################################
        position = int(input('insert argument'))
        return position

    def turn_choice(self, board):
        """
        ################################ Insert/Modify Comments HERE ##################################

        output -- integer
        0 -- end turn
        see main for more integer - action correspondance

        """
        ################################ Insert/Modify CODE HERE ##################################
        choice = int(input('choose an action'))
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
        position1, position2 = int(input('insert argument')), int(
            input('insert argument'))
        return position1, position2

    def play_plenty(self, board):
        """
        ################################ Insert/Modify Comments HERE ##################################
        resource1 -- integer 1-5
        resource2 -- integer 1-5

        """
        ################################ Insert/Modify CODE HERE ##################################

        resource1, resource2 = int(input('insert argument')), int(
            input('insert argument'))
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

        resource_own -- string-resource name
        resource_bank -- string-resource name

        """
        ################################ Insert/Modify CODE HERE ##################################
        resource_own, resource_bank = int(input('Select resource to trade in')), int(
            input('insert resource to receive'))
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
        resources_own, target_player_number, resources_target = input(
            'insert resources you want'),
        input('insert player you want to trade with'), input(
            'insert resources you want from that player')

        return resources_own, target_player_number, resources_target

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

        settle_position, road_position = int(
            input('Place your Settlement')), int(input('Place your Road'))
        return settle_position, road_position

    def start_settelment_first(self, board):
        """
                ################################ Insert/Modify Comments HERE ##################################
        output:
            settle_position -- integer 0-53
            road_position integer 0-71
        """
        ################################ Insert/Modify CODE HERE ##################################

        settle_position, road_position = int(
            input('Place your Settlement')), int(input('Place your Road'))
        return settle_position, road_position


if __name__ == '__main__':
    """
    ################################ Insert/Modify Comments HERE ##################################
    """

    ################################ Insert/Modify CODE HERE ##################################
    player = CatanPlayer(0)
    print(player.player_number)
    print('Debug complete')
