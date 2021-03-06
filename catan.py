import numpy as np
import random
import player
import catan_tile
import catan_road
import coordinate
import cards
import dev_cards

# List of resources available to be distributed on the board
RESOURCE_NAMES = ["desert", "brick", "ore", "hay", "wood", "sheep"]
RESOURCE_NAMES2 = ["brick", "ore", "hay", "wood", "sheep"]
# Create a dictionary of each resource and a corresponding number id
res_dict = dict(zip(RESOURCE_NAMES, np.arange(0, len(RESOURCE_NAMES))))
# List of available ports that can be distributed around the board
PORTS_NAMES = ["3:1", "2brick:1", "2ore:1", "2hay:1", "2wood:1", "2sheep:1"]
# Create a dictionary of each port and a corresponding number id
port_dict = dict(zip(PORTS_NAMES, np.arange(0, len(PORTS_NAMES))))
# Create a dictionary of each dev card and a corresponding number id
DEVELOPMENT_CARD_NAMES = ["knight", "victory point",
                          "road building", "year of plenty", "monopoly"]
dev_dict = dict(zip(DEVELOPMENT_CARD_NAMES,
                    np.arange(0, len(DEVELOPMENT_CARD_NAMES))))


class CatanBoard:
    # Initialize the Catan Board with all the options for resources, numbers to be rolled,
    # settlements/roads, port options
    def __init__(self):
        """initiates CatanBoard()/self according to catan rules:

        ################################ Insert/Modify Comments HERE ##################################

        Do not forget to ensure 6 and 8 are not next to each other: no 6-6 no 6-8 no 8-8
        """
        ################################ Insert/Modify CODE HERE ##################################
        # Array of each resource id number repeated the amount of times that the resource is available on the board
        # This will be used to distribute the resources into slots on the board
        self.board_resources = np.array(
            [res_dict["desert"]] + [res_dict["brick"]] * 3 + [res_dict["ore"]] * 3 + [res_dict["hay"]] * 4 + [
                res_dict["wood"]] * 4 + [res_dict["sheep"]] * 4)
        # Shuffle the resource array for randomized distribution
        np.random.shuffle(self.board_resources)
        # number associated with the desert and 0 can not actually be rolled
        print(self.board_resources)
        self.roll_numbers = np.array(
            [0, 2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12])
        # shuffle number options
        np.random.shuffle(self.roll_numbers)
        # Array of the port ids, amount of times each port is available -
        self.ports = np.array(
            [port_dict["3:1"]] * 4 + [port_dict["2brick:1"]] + [port_dict["2ore:1"]] + [port_dict["2hay:1"]] +
            [port_dict["2wood:1"]] + [port_dict["2sheep:1"]])
        # shuffle the ports for randomized distribution
        np.random.shuffle(self.ports)
        # Number_of_tiles represents the slots on the board available to receive a resource and number
        # This number is the same length as the available resources
        self.number_of_tiles = len(self.board_resources)
        # Settlements and roads need to be tracked.
        self.settlements = np.array([-1] * (30 + 18 + 6))
        self.cities = np.array([-1] * (30 + 18 + 6))
        self.roads = np.array([0] * (12 * 5 + 6 + 6))

        # Zero_tile_nr will represent where the 0 number exists
        # zero_tile_nr = np.where(self.roll_numbers == 0)
        # Desert_tile_nr will represent where the desert resource exists
        # desert_tile_nr = np.where(self.board_resources == res_dict["desert"])
        # Robber will keep track of where the robber is and it starts in the desert
        # self.robber = desert_tile_nr
        # as the desert tile and replace whatever was already in the desert tile into the empty zero tile
        # self.roll_numbers[zero_tile_nr], self.roll_numbers[desert_tile_nr] = (self.roll_numbers[desert_tile_nr],self.roll_numbers[zero_tile_nr])

        # positioning the 6's & 8's to be apart
        a = self.roll_numbers
        for i in range(19):
            if a[i] == 6 and i != 0:
                if a[0] != 6:
                    a[0], a[i] = a[i], a[0]
                else:
                    a[6], a[i] = a[i], a[6]
        for i in range(19):
            if a[i] == 8 and i != 7:
                if a[7] != 8:
                    a[7], a[i] = a[i], a[7]
                else:
                    a[15], a[i] = a[i], a[15]
        zero_tile_nr = np.where(self.roll_numbers == 0)
        desert_tile_nr = np.where(self.board_resources == res_dict["desert"])
        self.robber = desert_tile_nr
        self.board_resources[zero_tile_nr], self.board_resources[desert_tile_nr] = self.board_resources[desert_tile_nr], \
            self.board_resources[zero_tile_nr]

        # bank resources  "brick", "ore", "hay", "wood", "sheep"
        self.bank = cards.Res_cards()  # np.array([19, 19, 19, 19])
        # player_points player0, player1, player2, player3
        self.dev_bank = dev_cards.DevCards()
        self.player_points = [0, 0, 0, 0]
        # longest road player_number initialisation with -1
        self.longest_road = -1
        # longest largest_army player_number initialisation with -1
        self.largest_army = -1
        # devcards according to dev_dict dictionary
        self.bank_devcards = np.array([14 * [dev_dict["knight"]] + 5 * [dev_dict["victory point"]] + 2 * [
            dev_dict["road building"]] + 2 * [dev_dict["year of plenty"]] + 2 * [dev_dict["monopoly"]]])
        np.random.shuffle(self.bank_devcards)
        # played open knight cards for each player
        self.open_knights = [0, 0, 0, 0]
        # hidden unplayed dev cards for each player
        # as 2d materix  dev_dict x  player_number
        self.hidden_dev_cards = np.array([[0] * 5] * 4)
        # how many dev cards were just bought this turn and can not be played
        # as 2d matrix dev_dict x  player_number
        self.new_hidden_dev_card = np.array([[0] * 5] * 4)

        # road_list is an array for all road object positions
        self.road_list = []
        # array of coordinates for each of the 19 game tiles.
        # each tile has six corners for settlement/city placement.
        self.coordinates = [
            [0, 1, 2, 3, 4, 5],
            [2, 6, 7, 8, 9, 3],
            [7, 10, 11, 12, 13, 8],

            [14, 5, 4, 15, 16, 17],
            [4, 3, 9, 18, 19, 15],
            [9, 8, 13, 20, 21, 18],
            [13, 12, 22, 23, 24, 20],

            [25, 17, 16, 26, 27, 28],
            [16, 15, 19, 29, 30, 26],
            [19, 18, 21, 31, 32, 29],
            [21, 20, 24, 33, 34, 31],
            [24, 23, 35, 36, 37, 33],

            [27, 26, 30, 38, 39, 40],
            [30, 29, 32, 41, 42, 38],
            [32, 31, 34, 43, 44, 41],
            [34, 33, 37, 45, 46, 43],

            [39, 38, 42, 47, 48, 49],
            [42, 41, 44, 50, 51, 47],
            [44, 43, 46, 52, 53, 50],
        ]

        # adds all 19 tiles along with the properties
        # resource, roll number, coordinates
        # creates coordinates array
        self.coordinate_list = []
        for index in range(len(self.settlements)):
            self.coordinate_list.append(coordinate.Intersection(
                index,
                "Open"
            ))

        # Generates full list of road coordiantes for all 19 board tiles
        # creates a full list of road combination possibilities
        # sorts the combos always starting from smaller to larger
        self.roads_by_tiles = []
        full_combo_list = []
        self.coordinate_combos = []
        for i in range(len(self.coordinates)):
            tile_list = []
            for j in range(len(self.coordinates[i])):
                current_coordinates = []
                if j == 5:
                    current_coordinates = [
                        self.coordinates[i][j], self.coordinates[i][0]]
                else:
                    current_coordinates = [
                        self.coordinates[i][j], self.coordinates[i][j + 1]]

                current_coordinates.sort()
                full_combo_list.append(current_coordinates)
                tile_list.append(current_coordinates)
            self.roads_by_tiles.append(tile_list)

        # adding only unique values to coordinate_combo list
        for i in full_combo_list:
            if i not in self.coordinate_combos:
                self.coordinate_combos.append(i)
        # generating and appending road objects to the road_list
        # using only sorted unique combo pairs.
        for index in range(len(self.roads)):
            self.road_list.append(catan_road.Road(
                index,
                self.coordinate_combos[index][0],
                self.coordinate_combos[index][1]
            ))

        print(len(self.roads_by_tiles))
        # adds all board tiles with coordinates.
        self.board_layout = []
        for index in range(len(self.board_resources)):
            # creates coordinate objects for each of the tiles 6 coordinates.
            self.board_layout.append(catan_tile.CatanTile(
                index,
                self.board_resources[index],
                self.roll_numbers[index],
                self.coordinates[index],
                self.roads_by_tiles[index]
            ))
            print(self.board_layout[index])

    # String output for printing the board

    def __str__(self):
        """
        ################################ Insert/Modify Comments HERE ##################################

        output -- str
        """
        ################################ Insert/Modify CODE HERE ##################################
        """ Return the output string with all the resources, numbers, and ports to be printed when needed.
        The robber should be added to this output to keep track of where it is.
        Also, I think the output could use better formatting to differentiate between ports and resources and to
        be easier to look at. """

        # updated print function to something readable.

        printed_board = ''
        tiles = self.board_resources
        values = self.roll_numbers
        printed_board += '{:>20}{:>48}\n\n'.format(
            PORTS_NAMES[self.ports[0]],
            PORTS_NAMES[self.ports[1]]
        )
        printed_board += '{:>30}{:>15}{:>15}\n'.format(
            RESOURCE_NAMES[tiles[0]],
            RESOURCE_NAMES[tiles[1]],
            RESOURCE_NAMES[tiles[2]]
        )
        printed_board += '{:>28}{:>15}{:>15}{:>20}\n\n'.format(
            str(values[0]),
            str(values[1]),
            str(values[2]),
            PORTS_NAMES[self.ports[2]]
        )
        printed_board += '{:>10}{:>12}{:>18}{:>18}{:>18}\n'.format(
            PORTS_NAMES[self.ports[3]],
            RESOURCE_NAMES[tiles[3]],
            RESOURCE_NAMES[tiles[4]],
            RESOURCE_NAMES[tiles[5]],
            RESOURCE_NAMES[tiles[6]]
        )
        printed_board += '{:>20}{:>18}{:>18}{:>18}\n\n'.format(
            str(values[3]),
            str(values[4]),
            str(values[5]),
            str(values[6])
        )
        printed_board += '{:>17}{:>12}{:>18}{:>18}{:>18}\n'.format(
            RESOURCE_NAMES[tiles[7]],
            RESOURCE_NAMES[tiles[8]],
            RESOURCE_NAMES[tiles[9]],
            RESOURCE_NAMES[tiles[10]],
            RESOURCE_NAMES[tiles[11]]
        )
        printed_board += '{:>15}{:>12}{:>18}{:>18}{:>18}{:>15}\n\n'.format(
            str(values[7]),
            str(values[8]),
            str(values[9]),
            str(values[10]),
            str(values[11]),
            PORTS_NAMES[self.ports[4]]
        )
        printed_board += '{:>10}{:>12}{:>18}{:>18}{:>18}\n'.format(
            PORTS_NAMES[self.ports[5]],
            RESOURCE_NAMES[tiles[12]],
            RESOURCE_NAMES[tiles[13]],
            RESOURCE_NAMES[tiles[14]],
            RESOURCE_NAMES[tiles[15]]
        )
        printed_board += '{:>20}{:>18}{:>18}{:>18}\n\n'.format(
            str(values[12]),
            str(values[13]),
            str(values[14]),
            str(values[15])
        )
        printed_board += '{:>30}{:>15}{:>15}\n'.format(
            RESOURCE_NAMES[tiles[16]],
            RESOURCE_NAMES[tiles[17]],
            RESOURCE_NAMES[tiles[18]]
        )
        printed_board += '{:>28}{:>15}{:>15}{:>20}\n\n'.format(
            str(values[16]),
            str(values[17]),
            str(values[18]),
            PORTS_NAMES[self.ports[6]]
        )
        printed_board += '{:>20}{:>48}\n'.format(
            PORTS_NAMES[self.ports[7]],
            PORTS_NAMES[self.ports[8]]
        )

        return printed_board

    def disable_adjacent_coordinates(self, current_coordinate):
        for tile in self.board_layout:
            for index in range(len(tile.coordinates)):
                if tile.coordinates[index] == current_coordinate:
                    if index > 0 and index < 5:
                        self.coordinate_list[tile.coordinates[index - 1]
                                             ].status = "Unavailable"
                        self.coordinate_list[tile.coordinates[index + 1]
                                             ].status = "Unavailable"
                    elif index == 5:
                        self.coordinate_list[tile.coordinates[index - 1]
                                             ].status = "Unavailable"
                        self.coordinate_list[tile.coordinates[0]
                                             ].status = "Unavailable"
                    else:
                        self.coordinate_list[tile.coordinates[5]
                                             ].status = "Unavailable"
                        self.coordinate_list[tile.coordinates[index + 1]
                                             ].status = "Unavailable"

    def get_available_settlements(self):
        """ returns array of all availabel settlement coordinates"""
        available = []
        for index in range(len(self.coordinate_list)):
            if self.coordinate_list[index].status == "Open":
                available.append(index)

        return available

    def start_settlement_first(self, player_number, settle_position, road_position):
        """changes CatanBoard()/self if possible according to the rules of
        building the first starting settelment with an road

        ################################ Insert/Modify Comments HERE ##################################
        buy_settlement arguments:
        self -- CatanBoard()
        player_number -- integer 0-3
        settle_position -- integer 0-54
        road_position -- integer 0-71
        """
        ################################ Insert/Modify CODE HERE ##################################

        self.settlements[settle_position] = player_number
        self.disable_adjacent_coordinates(settle_position)

        # marks the coordinate as taken.
        ###############  insert code to mark off the 2 coordinates before and after the selected ################

        self.coordinate_list[settle_position].status = "Unavailable"
        self.roads[road_position] = player_number
        self.road_list[road_position].status = "Unavailable"

    def start_settlement_second(self, current_player, player_number, settle_position, road_position):
        """changes CatanBoard()/self if possible according to the rules of
         building the first starting settelment with an road
        ################################ Insert/Modify Comments HERE ##################################
        buy_settlement arguments:
        self -- CatanBoard()
        player_number -- integer 0-3
        settle_position -- integer 0-54
        road_position -- integer 0-71
        """
        ################################ Insert/Modify CODE HERE ##################################

        self.settlements[settle_position] = player_number
        self.disable_adjacent_coordinates(settle_position)
        self.coordinate_list[settle_position].status = "Unavailable"
        self.roads[road_position] = player_number
        self.road_list[road_position].status = "Unavailable"

        starting_resources = []
        for tile in self.board_layout:
            if settle_position in tile.coordinates:
                # check if tile is desert
                if tile.resource > 0:
                    current_player.add_to_hand(RESOURCE_NAMES[tile.resource])

    def check_points(self):
        """checks if somebody won the game (reached 10 points) and returns the winner or one of the point leaders

        ################################ Insert/Modify Comments HERE ##################################
        output --

        game_end (logical)
        winner (integer 0-3)
        """
        ################################ Insert/Modify CODE HERE #################################
        game_end, winner = False, 0
        for index, player_points in enumerate(self.player_points):
            if player_points >= 10:
                game_end, winner = True, index
        return game_end, winner

    def check_hand(self, players, player_num, resources):
        """ takes a list of players and the cost of purchase
        checks if this player has the resources to make this purchase
        if yes, then the purchase is completed"""
        valid = True
        for resource in RESOURCE_NAMES2:
            if resources[resource] > 0:
                if players[player_num].hand[resource] >= resources[resource]:
                    print('Has enough', resource)
                else:
                    print('Not enough ', resource)
                    valid = False

        if valid:
            for resource in RESOURCE_NAMES2:
                for index in range(resources[resource]):
                    players[player_num].remove_from_hand(resource)
                    self.bank.add_to_bank(resource)

        return valid

    def buy_settlement(self, players, player_number, position):
        """changes CatanBoard()/self if possible according to the rules of building a settelment:

        ################################ Insert/Modify Comments HERE ##################################

        buy_settlement arguments:
        self -- CatanBoard()
        player_number -- integer 0-3
        position -- integer 0-53

        """
        ################################ Insert/Modify CODE HERE ##################################
        cost = {
            "hay": 1,
            "wood": 1,
            "brick": 1,
            "sheep": 1,
            "ore": 0
        }
        valid = self.check_hand(players, player_number, cost)
        if valid:
            self.settlements[position] = player_number
            self.disable_adjacent_coordinates(position)
            self.coordinate_list[position].status = "Unavailable"

    def buy_city(self, players, player_number, position):
        """changes CatanBoard()/self if possible according to the rules of building a city:

        ################################ Insert/Modify Comments HERE ##################################

        buy_city arguments:
        self -- CatanBoard()
        player_number -- integer 0-3
        position -- integer 0-53
        """

        ################################ Insert/Modify CODE HERE ##################################
        cost = {
            "hay": 2,
            "wood": 0,
            "brick": 0,
            "sheep": 0,
            "ore": 3
        }
        valid = self.check_hand(players, player_number, cost)
        if valid:
            self.settlements[position] = -1
            self.cities[position] = player_number

    def buy_road(self, players, player_number, position):
        """changes CatanBoard()/self if possible according to the rules of building a road:

        ################################ Insert/Modify Comments HERE ##################################

        buy_road arguments:
        self -- CatanBoard()
        player_number -- integer 0-3
        position -- integer 0-71

        """
        ################################ Insert/Modify CODE HERE ##################################

        cost = {
            "hay": 0,
            "wood": 1,
            "brick": 1,
            "sheep": 0,
            "ore": 0
        }
        valid = self.check_hand(players, player_number, cost)
        if valid:
            self.roads[position] = player_number
            self.road_list[position].status = "Unavailable"

    def buy_dev_card(self, players, player_number):
        """changes CatanBoard()/self if possible according to the rules of buying a development card card:

        ################################ Insert/Modify Comments HERE ##################################

        buy_dev_card input arguments:
        self -- CatanBoard()
        player_number -- integer 0-3

        """
        ################################ Insert/Modify CODE HERE ##################################

        ######## I would suggest using code such as the next 10 lines instead.  ###########
        # cost = {
        #     "hay": 1,
        #     "wood": 0,
        #     "brick": 0,
        #     "sheep": 1,
        #     "ore": 1
        # }
        # valid = self.check_hand(players, player_number, cost)
        # if valid:
        #     players[player_number].add_dev(self.bank_devcards.pop())

        player.show_dev()
        choice = int(input('choose the dev_card: '))
        choice = player.dev_convert(choice)
        if self.dev_bank[choice] != 0:
            player.add_dev(choice)
            self.dev_bank.remove_from_bank(choice)
            player.remove_from_hand('wool')
            player.remove_from_hand('ore')
            player.remove_from_hand('hay')
            self.bank.add_to_bank('wool')
            self.bank.add_to_bank('ore')
            self.bank.add_to_bank('hay')
        else:
            print('Card is not in bank.')

    def add_tile_resources(self, tile, player_list):
        """ add code to hand out all resources on the tile spun"""
        for index in range(len(self.settlements)):
            if index in tile.coordinates:
                if self.settlements[index] > -1:
                    player_list[self.settlements[index]].add_to_hand(
                        RESOURCE_NAMES[tile.resource]
                    )

    def roll_dice(self, player_number, player_list):
        """changes CatanBoard()/self if possible according to the rules of rolling dice in catan:

        ################################ Insert/Modify Comments HERE ##################################

        # two die rolls to ensure the spins will be with the correct probability   

        """
        # output roll_numer of dice
        ################################ Insert/Modify CODE HERE ##################################
        roll_die_one = random.randint(1, 6)
        roll_die_two = random.randint(1, 6)
        spin_num = roll_die_one + roll_die_two
        for tile in self.board_layout:
            if tile.resource > 0:
                if spin_num == tile.value:
                    self.add_tile_resources(tile, player_list)

        return spin_num

    def discard_half(self, player):  # , resources):
        """changes CatanBoard()/self if possible according to the rules of discarding cards if 7 rolled

        ################################ Insert/Modify Comments HERE ##################################
        discard_half input arguments:
        self -- CatanBoard()
        player_number -- integer 0-3
        resourses -- np.array([brick, ore, hay, wood, sheep])
                brick -- integer 0-19
                ore -- integer 0-19
                hay -- integer 0-19
                wood --integer 0-19
                sheep --integer 0-19

        """
        ################################ Insert/Modify CODE HERE ##################################

        player_hand = player.hand
        cards_to_discard = 0  # checking for min of 8 cards
        for resource in RESOURCE_NAMES2:
            cards_to_discard += player_hand[resource]
        if cards_to_discard >= 8:
            print('You have to return ', cards_to_discard // 2, ' cards.')
            print('You have the following cards:')
            for resource in RESOURCE_NAMES2:
                print(player_hand[resource], ' ', resource)
            print()
            player.show_options()
            for resource in range(cards_to_discard // 2):
                choice = int(input("enter the card you want to return: "))
                choice = player.convert(choice)
                while not choice in RESOURCE_NAMES2:
                    choice = input("enter a correct resource: ")
                while player_hand[choice] == 0:
                    print("you don't have that card.")
                    choice = input("enter a card you have: ")
                player.remove_from_hand(choice)
                self.bank.add_to_bank(choice)
            print('You now have the following cards:')
            for resource in RESOURCE_NAMES2:
                print(player_hand[resource], ' ', resource)

    def steal_card(self, player_number, position, target_player_number):
        """changes CatanBoard()/self if possible according to the rules of discarding cards if 7 rolled

        ################################ Insert/Modify Comments HERE ##################################
        steal_card input arguments:
        self -- CatanBoard()
        player_number -- integer 0-3
        position -- integer 0 - self.number_of_tiles-1
        target_player_number -- integer 0-3
        """
        ################################ Insert/Modify CODE HERE ##################################

    def play_knight(self, player_number, position, target_player_number):
        """changes CatanBoard()/self if possible according to the rules knight playing in catan:

        ################################ Insert/Modify Comments HERE ##################################
        self -- CatanBoard()
        player_number -- integer 0-3
        position -- integer 0 - self.number_of_tiles-1
        target_player_number -- integer 0-3

        """
        ################################ Insert/Modify CODE HERE ##################################

    def play_roads(self, player_number, position1, position2):
        """changes CatanBoard()/self if possible according to the rules of playing the roadsbuilding dev card :

        ################################ Insert/Modify Comments HERE ##################################
        self -- CatanBoard()
        player_number -- integer 0-3
        position1 -- integer 0-71
        position2 -- integer 0-71
        """
        ################################ Insert/Modify CODE HERE ##################################

        self.roads[position1] = player_number
        self.roads[position2] = player_number

    def play_plenty(self, player, resource1, resource2):
        """changes CatanBoard()/self if possible according to the rules of playing the years of plenty dev card :

        ################################ Insert/Modify Comments HERE ##################################
        self -- CatanBoard()
        player_number -- integer 0-3
        resource1 -- integer 1-5
        resource1 -- integer 1-5
        """
        ################################ Insert/Modify CODE HERE ##################################
        self.bank.remove_from_bank(RESOURCE_NAMES2[resource1])
        self.bank.remove_from_bank(RESOURCE_NAMES2[resource2])
        player.add_to_bank(RESOURCE_NAMES2[resource1])
        player.add_to_bank(RESOURCE_NAMES2[resource2])

    def play_mono(self, player_number, resource):
        """changes CatanBoard()/self if possible according to the rules of playing monopoly dev card :

        ################################ Insert/Modify Comments HERE ##################################
        self -- CatanBoard()
        player_number -- integer 0-3
        resource -- integer 1-5

        """
        ################################ Insert/Modify CODE HERE ##################################

    def trade_bank(self, player_number, resource_own, resource_bank):
        """changes CatanBoard()/self if possible according to the rules bank trading including ports:

        ################################ Insert/Modify Comments HERE ##################################
        self -- CatanBoard()
        player_number -- integer 0-3
        resource_own -- integer 1-5
        resource_bank -- integer 1-5
        """
        ################################ Insert/Modify CODE HERE ##################################

        for i in range(4):
            player.remove_from_hand(RESOURCE_NAMES2[resource_own])
            # player giving the bank 4 cards
            self.bank.add_to_bank(RESOURCE_NAMES2[resource_own])
        # player taking one card from the bank
        player.add_to_hand(RESOURCE_NAMES2[resource_bank])
        self.bank.remove_from_bank(RESOURCE_NAMES2[resource_bank])

    def trade_offer(self, player_number, resources_own, amount, resources_target, amount2):
        """changes CatanBoard()/self if possible according to the rules bank trading including ports:

        ################################ Insert/Modify Comments HERE ##################################
        self -- CatanBoard()
        player_number -- integer 0-3
        resources_own -- np.array([brick, ore, hay, wood, sheep])
        target_player_number -- integer 0-3
        resources_target -- np.array([brick, ore, hay, wood, sheep])
                brick -- integer 0-19
                ore -- integer 0-19
                hay -- integer 0-19
                wood --integer 0-19
                sheep --integer 0-19
        answer_target -- TRUE for yes or FALSE for no
        """
        ################################ Insert/Modify CODE HERE ##################################
        print('The current player is offering to exchange ',
              amount, ' ', resources_own)
        print('in exchange for ', amount2, ' ', resources_target, '.')
        accept = int(input(
            'enter number of player who accepts the offer, enter ', player_number, ' if no-one: '))
        if accept != player_number:
            for i in range(amount):
                player.add_to_hand(RESOURCE_NAMES2[resources_target])
                player.CatanPlayer(accept).remove_from_hand(
                    RESOURCE_NAMES2[resources_target])
            for i in range(amount2):
                player.CatanPlayer(accept).add_to_hand(
                    RESOURCE_NAMES2[resources_own])
                player.remove_from_hand(RESOURCE_NAMES2[resources_own])


if __name__ == '__main__':
    """
     ################################ Insert/Modify Comments HERE ##################################
     """

    ################################ Insert/Modify CODE HERE ##################################
    catan_board = CatanBoard()
    print(catan_board)
    print('Debug complete')
