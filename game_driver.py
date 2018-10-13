import io_handler as ui

def run_game() :
	ui.ui_intro()
	name = ui.ui_prompt_player_name()
	player = Player(name)
	alive = True
	level = 1
	while(alive) :
		player.give_rand_adj()
		firstRoom = Room(player, level++)
		alive = firstRoom.explore_room()


def main() :
	run_game();

if __name__ == '__main__':
	main()
