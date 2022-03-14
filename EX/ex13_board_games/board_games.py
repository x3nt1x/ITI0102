"""API."""


class Player:
    """Player class."""

    def __init__(self, name: str):
        """Player constructor."""
        self.__name = name
        self.__games = dict()

    def __repr__(self):
        """Representation of the player."""
        return self.get_name()

    def get_name(self) -> str:
        """Return player's name."""
        return self.__name

    def get_games(self) -> dict:
        """Return player's games."""
        return self.__games

    def get_games_list(self) -> list:
        """Return player's games in list as strings."""
        return [game.get_name() for game in self.get_games().keys()]

    def get_wins(self) -> int:
        """Return player's wins."""
        return sum(result == 1 for result in self.get_games().values())

    def get_losses(self) -> int:
        """Return player's losses."""
        return sum(result == len(game.get_players()) for game, result in self.get_games().items())

    def get_times_played(self, search: str) -> int:
        """Get how many times player has played the searched game."""
        return self.get_games_list().count(search)

    def get_win_percent(self, search: str) -> float:
        """Get player's win percent of the searched game."""
        wins_in_game = sum(result == 1 for game, result in self.get_games().items() if game.get_name() == search)
        return wins_in_game / self.get_times_played(search)

    def get_loss_percent(self, search: str) -> float:
        """Get player's loss percent of the searched game."""
        losses_in_games = sum(result == len(game.get_players()) for game, result in self.get_games().items() if game.get_name() == search)
        return losses_in_games / self.get_times_played(search)

    def add_game(self, game, result: int):
        """
        Add game with player's result.

        Also add + 1 to the result so that it starts counting from 1.
        """
        self.__games[game] = result + 1

    def get(self, path: str):
        """Get player related info."""
        if path == "amount":
            return len(self.get_games().keys())
        if path == "favourite":
            return max(self.get_games_list(), key=self.get_games_list().count)
        if path == "won":
            return self.get_wins()


class Game:
    """Game class."""

    def __init__(self, name: str, type: str):
        """Game constructor."""
        self.__name = name
        self.__type = type
        self.__players: list[Player] = list()
        self.__winner_points = int()

    def __repr__(self):
        """Representation of the game."""
        return self.get_name()

    def get_name(self) -> str:
        """Return game's name."""
        return self.__name

    def get_type(self) -> str:
        """Return game's type."""
        return self.__type

    def get_players(self) -> list[Player]:
        """Return game's players."""
        return self.__players

    def get_winner_points(self) -> int:
        """Return winner points."""
        return self.__winner_points

    def get_winner(self) -> Player:
        """Get game's winner."""
        return self.get_players()[0]

    def get_loser(self) -> Player:
        """Get game's loser."""
        return self.get_players()[-1]

    def add_player(self, player: Player):
        """Aad player to game."""
        self.__players.append(player)

    def set_winner_points(self, points: int):
        """Set winner points."""
        self.__winner_points = points


class Statistics:
    """Statistics class."""

    def __init__(self, filename: str):
        """Statistic constructor."""
        self.__games: list[Game] = list()
        self.__players: list[Player] = list()
        self.read_data_from_file(filename)

    def get_games(self) -> list[Game]:
        """Return games."""
        return self.__games

    def get_players(self) -> list[Player]:
        """Return players."""
        return self.__players

    def get_games_list(self) -> list:
        """Return games in list as strings."""
        return [game.get_name() for game in self.get_games()]

    def get_total(self, type: str = None) -> int:
        """Return total games or total games by type."""
        if type:
            return len([game for game in self.get_games() if game.get_type() == type])

        return len(self.get_games())

    def get_player_by_name(self, name: str):
        """Return player by name."""
        for player in self.get_players():
            if player.get_name() == name:
                return player

        return None

    def read_data_from_file(self, filename: str):
        """Read data from file."""
        with open(filename) as file:
            for row in file.readlines():
                info = row.strip().split(";")

                game_name = info[0]
                game_type = info[2]
                players = info[1].split(",")
                results = info[3].split(",")
                data = list()

                game = Game(game_name, game_type)

                if game_type == "points":
                    for player, result in zip(players, results):
                        data.append([player, int(result)])

                        game.set_winner_points(int(result) if int(result) > game.get_winner_points() else game.get_winner_points())

                    data.sort(key=lambda x: -x[1])

                elif game_type == "places":
                    for player in players:
                        data.append([player, results.index(player)])

                    data.sort(key=lambda x: x[1])

                elif game_type == "winner":
                    for player in players:
                        data.append([player, 1 if player == results[0] else 0])

                    data.sort(key=lambda x: -x[1])

                for i, (name, result) in enumerate(data):
                    player = self.get_player_by_name(name)

                    if not player:
                        player = Player(name)
                        self.__players.append(player)

                    player.add_game(game, i)
                    game.add_player(player)

                self.__games.append(game)

    def get_game_info(self, path: str, game_name: str):
        """Get game related info."""
        if path == "amount":
            return self.get_games_list().count(game_name)

        if path == "player-amount":
            games_list = [game.get_players() for game in self.get_games() if game_name == game.get_name()]
            return len(max(games_list, key=games_list.count))

        if path == "most-wins":
            winners_list = [game.get_winner() for game in self.get_games() if game_name == game.get_name()]
            return max(winners_list, key=winners_list.count).get_name()

        if path == "most-frequent-winner":
            players_list = [player for player in self.get_players() if game_name in player.get_games_list()]
            return max(players_list, key=lambda x: x.get_win_percent(game_name)).get_name()

        if path == "most-losses":
            losers_list = [game.get_loser() for game in self.get_games() if game_name == game.get_name()]
            return max(losers_list, key=losers_list.count).get_name()

        if path == "most-frequent-loser":
            players_list = [player for player in self.get_players() if game_name in player.get_games_list()]
            return max(players_list, key=lambda x: x.get_loss_percent(game_name)).get_name()

        if path == "record-holder":
            records_list = [[game.get_winner(), game.get_winner_points()] for game in self.get_games() if game_name == game.get_name()]
            return max(records_list, key=lambda x: x[1])[0].get_name()

    def get(self, path: str):
        """Get data."""
        if path == "/games":
            games = list()

            for game in self.get_games():
                if game.get_name() not in games:
                    games.append(game.get_name())

            return games

        if path == "/players":
            return [player.get_name() for player in self.get_players()]

        if path.startswith("/total"):
            info = path.split("total/")
            return self.get_total(info[1] if len(info) > 1 else None)

        if path.startswith("/player/"):
            info = path.split("/")
            return self.get_player_by_name(info[2]).get(info[3])

        if path.startswith("/game/"):
            info = path.split("/")
            return self.get_game_info(info[3], info[2])


if __name__ == '__main__':
    api = Statistics("data.txt")

    print(api.get("/players"))
    print(api.get("/games"))
    print(api.get("/total"))
    print(api.get("/total/winner"))
    print()

    print(api.get("/player/joosep/amount"))
    print(api.get("/player/joosep/favourite"))
    print(api.get("/player/joosep/won"))
    print()

    print(api.get("/game/chess/amount"))
    print(api.get("/game/terraforming mars/player-amount"))
    print(api.get("/game/game of thrones/most-wins"))
    print(api.get("/game/chess/most-frequent-winner"))
    print(api.get("/game/chess/most-losses"))
    print(api.get("/game/chess/most-frequent-loser"))
    print(api.get("/game/terraforming mars/record-holder"))
