"""Santa's Workshop."""
import re
import base64
import string
import requests
from typing import Optional


class Gift:
    """Gift class."""

    def __init__(self, name: str, weight: int):
        """Gift constructor."""
        self.__name = name
        self.__weight = weight

    def __repr__(self):
        """Representation of the gift."""
        return f"{self.get_name()} {self.get_weight()}g"

    def get_name(self) -> str:
        """Return gift's name."""
        return self.__name

    def get_weight(self) -> int:
        """Return gift's weight in grams."""
        return self.__weight

    def get_weight_kg(self) -> float:
        """Return gift's weight in kilograms."""
        return self.__weight / 1000


class Child:
    """Child class."""

    def __init__(self, name: str, country: str, wish: str):
        """Child constructor."""
        self.__name = name
        self.__country = country
        self.__wish = wish

    def __repr__(self):
        """Representation of the child."""
        return f"{self.get_name()} @{self.get_country()} wishes {self.get_wish()}"

    def get_name(self) -> str:
        """Return child's name."""
        return self.__name

    def get_country(self) -> str:
        """Return child's country."""
        return self.__country

    def get_wish(self) -> str:
        """Return child's wish."""
        return self.__wish


class Children:
    """Children class."""

    def __init__(self):
        """Children constructor."""
        self.__children: list[Child] = list()

    def has(self, name: str) -> bool:
        """Check if child exists."""
        if self.get_child_by_name(name):
            return True

        return False

    def get(self) -> list[Child]:
        """Return children list."""
        return self.__children

    def add(self, child: Child):
        """Add child to list."""
        self.__children.append(child)

    def get_child_by_name(self, name: str) -> Optional[Child]:
        """Return child by name."""
        for child in self.get():
            if child.get_name() == name:
                return child

        return None

    def from_country(self, country: str) -> list[Child]:
        """Get children from country."""
        return [child for child in self.get() if child.get_country() == country]


class Warehouse:
    """Warehouse class."""

    def __init__(self):
        """Warehouse constructor."""
        self.__gifts: dict[str, list[Gift]] = dict()

    def has(self, name: str) -> bool:
        """Check if warehouse has gift."""
        return name in self.get_gifts()

    def get(self, name: str) -> Gift:
        """
        Get gift from warehouse.

        If it was last gift, remove gift key from dictionary
        """
        gift = self.get_gifts().get(name).pop(-1)

        if not self.get_gifts().get(name):
            self.get_gifts().pop(name)

        return gift

    def get_gifts(self) -> dict[str, list[Gift]]:
        """Return all gifts in warehouse."""
        return self.__gifts

    def get_gift_by_name(self, name: str) -> Optional[Gift]:
        """Return gift by name. Don't remove from warehouse."""
        return self.get_gifts().get(name)[0] if self.has(name) else None

    def add(self, gift: Gift):
        """Add gift to warehouse."""
        name = gift.get_name()

        if not self.has(name):
            self.__gifts[name] = list()

        self.__gifts[name].append(gift)


class Sleigh:
    """Santa's sleigh class. Max weight 50kg."""

    def __init__(self, country: str, child: Child, gift: Gift):
        """Gift constructor."""
        self.__weight = 0
        self.__country = country
        self.__gifts: dict[Child, Gift] = dict()
        self.add(child, gift)

    def __repr__(self):
        """Representation of the sleigh."""
        return f"sleigh ({self.get_weight_kg()}kg)"

    def get_weight(self) -> int:
        """Return sleigh's weight in grams."""
        return self.__weight

    def get_weight_kg(self) -> float:
        """Return sleigh's weight in kilograms."""
        return self.__weight / 1000

    def get_country(self) -> str:
        """Return sleigh's destination country."""
        return self.__country

    def get_gifts(self) -> dict[Child, Gift]:
        """Return gifts in sleigh."""
        return self.__gifts

    def add(self, child: Child, gift: Gift) -> bool:
        """Add gift to sleigh and increase weight."""
        if (self.get_weight() + gift.get_weight()) > 50000:
            return False

        self.__gifts[child] = gift
        self.__weight += gift.get_weight()

        return True

    def print_receipt(self, count: int = 0):
        """
        Print receipt.

        :param count: in case we send multiple sleighs to same country
        """
        with open(f"receipts/{self.get_country()}_{count}.txt", "w") as file:
            file.write(self.create_receipt())

    def create_receipt(self) -> str:
        """Create receipt."""
        text = r"""                        DELIVERY ORDER
                                                          _v
                                                     __* (__)
             ff     ff     ff     ff                {\/ (_(__).-.
      ff    <_\__, <_\__, <_\__, <_\__,      __,~~.(`>|-(___)/ ,_)
    o<_\__,  (_ ff ~(_ ff ~(_ ff ~(_ ff~~~~~@ )\/_;-"``     |
      (___)~~//<_\__, <_\__, <_\__, <_\__,    | \__________/|
      // >>     (___)~~(___)~~(___)~~(___)~~~~\\_/_______\_//
                // >>  // >>  // >>  // >>     `'---------'`"""

        name_width = 4  # "Name" length is 4 so minimum width is always 4
        gift_width = 5  # "Gifts" length is 5 so minimum width is always 5
        weight_width = 18  # "Total Weight(kg)" length is 16, + 2 for the space around word

        for child, gift in self.get_gifts().items():
            name_size = len(child.get_name())
            gift_size = len(gift.get_name())

            name_width = name_size if name_width < name_size else name_width
            gift_width = gift_size if gift_width < gift_size else gift_width

        name_width += 2  # + 2 for the space around name
        gift_width += 2  # + 2 for the space around gift

        text += "\n\nFROM: NORTH POLE CHRISTMAS CHEER INCORPORATED\n"
        text += f"TO: {self.get_country()}\n\n"

        text += "//" + "=" * name_width + "[]" + "=" * gift_width + "[]" + "=" * weight_width + r"\\" + "\n"
        text += "||{:^{}s}||{:^{}s}||{:^{}s}||\n".format("Name", name_width, "Gifts", gift_width, "Total Weight(kg)", weight_width)
        text += "|]" + "=" * name_width + "[]" + "=" * gift_width + "[]" + "=" * weight_width + "[|" + "\n"

        for child, gift in self.get_gifts().items():
            text += "|| {:<{}} || {:<{}s} || {:>{}} ||\n".format(child.get_name(), name_width - 2, gift.get_name(),
                                                                 gift_width - 2, gift.get_weight_kg(), weight_width - 2)

        text += r"\\" + "=" * name_width + "[]" + "=" * gift_width + "[]" + "=" * weight_width + "//"

        return text


class PostOffice:
    """PostOffice class."""

    def __init__(self, count: int = 10):
        """PostOffice constructor."""
        self.__letters = list()
        self.__wishes = dict()
        self.read(count)
        self.reply()

    def get_letters(self) -> list:
        """Return letters."""
        return self.__letters

    def get_wishes(self) -> dict:
        """Return wishes."""
        return self.__wishes

    def decrypt_base64(self, letter: str) -> str:
        """Decrypt base64 letter."""
        return base64.b64decode(letter).decode()

    def decrypt_cipher(self, letter: str) -> str:
        """Decrypt cipher letter."""
        message = str()
        alphabet = string.ascii_lowercase

        for char in letter:
            if char in alphabet:
                message += alphabet[(alphabet.index(char) - 4) % len(alphabet)]
            else:
                message += char

        return message

    def read(self, count: int = 10):
        """
        Read letters from API. Decrypt when needed. Determine if it's just letter or contains wish.

        :param count: how many letters to read (default 10)
        """
        for _ in range(count):
            letter = requests.get('http://api.game-scheduler.com:8089/letter').json()["letter"]

            if letter.islower():  # If entire letter is in lowercase, it's probably cipher
                letter = self.decrypt_cipher(letter)
            elif " " not in letter:  # If entire letter is one long string, it's probably base64
                letter = self.decrypt_base64(letter)

            wish = str()

            for match in re.finditer(r"(I wish for |I want |wishlist: )(.+?)(?=[,.])|(?<=,\n)(\w+), (.+)", letter):
                if match.group(2):  # If group 2 matches, it's probably wish
                    wish = match.group(2).lower()
                    continue

                name = match.group(3).capitalize()
                country = match.group(4)

                if wish:
                    self.__wishes[name] = [country, wish]
                else:
                    self.__letters.append(name)

    def reply(self):
        """Reply to letters that didn't have any wishes."""
        for name in self.get_letters():
            with open(f"letters/{name}.txt", "w") as file:
                file.write(f"""Dear {name}!\n\nThank You for Your letter.\nMerry Christmas and Happy New Year!\n\nSanta, North Pole""")


class Workshop:
    """Workshop class."""

    def __init__(self, nice_file: str, naughty_file: str, wishes_file: str, letters_to_read: int = 10):
        """Workshop constructor."""
        self.__children = Children()
        self.__warehouse = Warehouse()
        self.__postoffice = PostOffice(letters_to_read)
        self.__countries = list()
        self.__sleighs: dict[str, list[Sleigh]] = dict()
        self.read_data_from_files(nice_file, wishes_file)
        self.handle_letters(naughty_file)

    def get_children(self) -> Children:
        """Return children object."""
        return self.__children

    def get_warehouse(self) -> Warehouse:
        """Return warehouse object."""
        return self.__warehouse

    def get_postoffice(self) -> PostOffice:
        """Return PostOffice object."""
        return self.__postoffice

    def get_countries(self) -> list:
        """Return countries."""
        return self.__countries

    def get_sleighs(self) -> dict[str, list[Sleigh]]:
        """Return sleighs."""
        return self.__sleighs

    def get_sleighs_by_country(self, country: str) -> list[Sleigh]:
        """Return sleighs by country."""
        return self.get_sleighs().get(country)

    def print_sleighs_receipts(self):
        """Print all receipts from all sleighs."""
        for country in self.get_countries():
            for i, sleigh in enumerate(self.get_sleighs_by_country(country)):
                sleigh.print_receipt(i)

    def create_gift(self, name: str) -> Gift:
        """
        Create a gift and add it to warehouse.

        Only turn to API if we've no previous info about gift. Else just use existing gift from warehouse.
        """
        gift = self.get_warehouse().get_gift_by_name(name)

        if not gift:
            request = requests.get('http://api.game-scheduler.com:8089/gift', params={"name": name}).json()
            gift = Gift(name, request["weight_in_grams"])

        self.get_warehouse().add(gift)
        return gift

    def read_data_from_files(self, nice_file: str, wishes_file: str):
        """Read data from files."""
        nice_list = open(nice_file)
        wish_list = open(wishes_file)

        for row in nice_list.readlines():
            info = row.strip().split(", ")

            name = info[0]
            country = info[1]
            wish = wish_list.readline().split(", ")[1].strip().lower()

            self.get_children().add(Child(name, country, wish))
            self.create_gift(wish)

            if country not in self.get_countries():
                self.__countries.append(country)

        nice_list.close()
        wish_list.close()

    def handle_letters(self, naughty_file: str):
        """
        Handle letters.

        Check if child is already getting a gift, avoid delivering them same gift twice.
        Check if child is in naughty list, don't deliver them anything.
        """
        for name, (country, wish) in self.get_postoffice().get_wishes().items():
            if self.get_children().has(name):
                continue

            with open(naughty_file) as file:
                if name in file.read():
                    continue

            self.get_children().add(Child(name, country, wish))
            self.create_gift(wish)

            if country not in self.get_countries():
                self.__countries.append(country)

    def prepare_sleighs(self):
        """Prepare sleighs for transport."""
        for country in self.get_countries():
            self.__sleighs[country] = list()

            for child in self.get_children().from_country(country):
                gift = self.get_warehouse().get(child.get_wish())
                did_fit = False

                for sleigh in self.get_sleighs_by_country(country):
                    if sleigh.add(child, gift):
                        did_fit = True
                        break

                if not did_fit:
                    self.__sleighs[country].append(Sleigh(country, child, gift))


if __name__ == '__main__':
    shop = Workshop("nice_list.csv", "naughty_list.csv", "wish_list.csv")
    shop.prepare_sleighs()
    shop.print_sleighs_receipts()
