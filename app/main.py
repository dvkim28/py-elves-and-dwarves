from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(team: list[Player]) -> int:
    result = 0
    for member in team:
        result += member.get_rating()
    return result


def elves_concert(list_of_elves: list[Elf]) -> None:
    for elf in list_of_elves:
        elf.play_elf_song()


def feast_of_the_dwarves(list_of_dwarves: list[Dwarf]) -> None:
    for dwarf in list_of_dwarves:
        dwarf.eat_favourite_dish()
