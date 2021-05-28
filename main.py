# This is a catan Python script.
import catan
import player
import copy
"""
################################ You ar free to modify and add any comments ##################################

you can and should change and add print statements
it would be also usefull to write log of the game in a file
"""
# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# the game is played for maximum 30 rounds (30*4 = 120 turns) to prevent infinite loops
MAXIMUM_ROUNDS = 30


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # build catan board
    board = catan.CatanBoard()

    # insert players
    players = list()

    # Create players
    for player_number in range(4):
        players.append(player.CatanPlayer(player_number))

    # game set up of the two settelment
    # first settelment with road
    for player_number in range(4):
        current_player = players[player_number]
        board_safety_copy = copy.deepcopy(board)

        # Player chooses first settlement and road
        settle_position, road_position = current_player.start_settelment_first(
            board_safety_copy)

        # Place chosen settlement and road on board
        board.start_settlement_first(
            player_number, settle_position, road_position)

    # second settelment with road
    for player_number in range(3, -1, -1):
        current_player = players[player_number]
        board_safety_copy = copy.deepcopy(board)
        settle_position, road_position = current_player.start_settelment_second(
            board_safety_copy)
        board.start_settlement_second(current_player,
                                      player_number, settle_position, road_position)

    for coord in board.coordinate_list:
        print(coord)
    # game will be played for maximum MAXIMUM_ROUNDS
    for game_round in range(MAXIMUM_ROUNDS):
        # print statements for debugging
        print(game_round)
        # in each round each player has his turn
        for player_number in range(4):
            current_player = players[player_number]
            # print statements for debugging
            print('It is turn of player number:{0}'.format(
                current_player.player_number))
            choice = 42  # random positive number for initialisation
            rolled = False
            choice = 42  # random positive number for initialisation
            while choice > 0:
                # making safety working copy of board (can be changed in later
                # implementation to only visible data)
                board_safety_copy = copy.deepcopy(board)
                # player makes the choice what to do the choices are integers 0 or negative integer is turn finished
                choice = current_player.turn_choice(board_safety_copy)
                # print statements for debugging
                # choices below are moves available to a player
                if choice == 1:
                    position, target_player_number = current_player.steal_card(
                        board_safety_copy)
                    board.play_knight(player_number, position,
                                      target_player_number)
                if choice == 2:
                    # roll dice
                    if not rolled:
                        rolled = True
                        dice_number = board.roll_dice(player_number, players)
                        print(dice_number)
                        if dice_number == 7:
                            for p_nr in range(4):
                                p = players[p_nr]
                                # resources = p.discard_half(board_safety_copy)
                                board.discard_half(p)
                            # steal resource after everybody discarded cards
                            position, target_player_number = current_player.steal_card(
                                board_safety_copy)
                            board.steal_card(
                                player_number, position, target_player_number)
                    else:
                        print("Already rolled this turn! No cheating!")
                        # choice 3 is to buy a settlement
                if rolled:
                    if choice == 3:
                        position = current_player.set_settlement(
                            board_safety_copy)
                        board.buy_settlement(players, player_number, position)
                    # choice 4 is to buy a city
                    if choice == 4:
                        position = current_player.set_city(board_safety_copy)
                        board.buy_city(player_number, position)
                    # choice 5 is to buy a road
                    if choice == 5:
                        position = current_player.set_road(board_safety_copy)
                        board.buy_road(player_number, position)
                    if choice == 6:
                        board.buy_dev_card(player_number)
                    if choice == 7:
                        position1, position2 = current_player.play_roads(
                            board_safety_copy)
                        board.play_roads(player_number, position1, position2)
                    if choice == 8:
                        resource1, resource2 = current_player.play_plenty(
                            board_safety_copy)
                        board.play_plenty(player_number, resource1, resource2)
                    if choice == 9:
                        resource = current_player.play_mono(board_safety_copy)
                        board.play_mono(player_number, resource)
                    if choice == 10:
                        resource_own, resource_bank = current_player.trade_bank(
                            board_safety_copy)
                        board.trade_bank(
                            player_number, resource_own, resource_bank)
                    if choice == 11:
                        resources_own, amount, resources_target, amount2 = current_player.trade_offer(
                            board_safety_copy)
                        # answer_target = players[target_player_number].trade_answer(board_safety_copy, resources_own,
                        # resources_target)
                        board.trade_offer(player_number, resources_own, amount, resources_target,
                                          amount2)
                    if choice == 12:
                        current_player.print_hand()

                else:
                    print('You must roll the dice first. Did you read the rule book??')

            game_end, winner = board.check_points()
            if game_end:
                print("player {0} won".format(players[winner]))
                break
    print('game ended')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
