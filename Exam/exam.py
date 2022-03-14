"""Exam 5 (2022-01-17)."""
from typing import Optional


def double_letters(text: str) -> str:
    """
    Double every letter in text.

    Latin letters (a-z and A-Z) have to be doubled for the output.
    All other symbols should remain the same.

    double_letters("abc") => "aabbcc"
    double_letters("hello world") => "hheelllloo wwoorrlldd"
    double_letters("Hi!?") => "HHii!?"
    """
    result = ""

    for c in text:
        if c.isalpha():
            result += c * 2
        else:
            result += c

    return result


def odds_sum(nums: list) -> int:
    """
    Find the sum of all odd numbers in given list.

    odds_sum([]) -> 0
    odds_sum([1, 2, 3]) -> 4
    odds_sum([2, 8, 10, 22]) -> 0
    """
    result = 0

    for num in nums:
        if num % 2 != 0:
            result += num

    return result


def reverse_subword(s: str, subword: str) -> str:
    """
    If subword exists in s, reverse the first occurrence of s and return the modified string.

    Otherwise return original s.

    reverse_subword("abcde", "bc") => "acbde"
    reverse_subword("abcabc", "bc") => "acbabc"
    reverse_subword("abcabc", "ac") => "abcabc"

    :param s: original string
    :param subword: len(subword) > 0
    :return:
    """
    result = str()

    if subword in s:
        index = s.index(subword)
        reverse = subword[::-1]
        size = len(reverse)
        found = False
        test = 0

        for i, c in enumerate(s):
            if test < size and found:
                test += 1
                continue

            if i == index:
                found = True
                result += reverse
                test += 1
            else:
                result += c
    else:
        return s

    return result


def sum_of_multipliers(first_num: int, second_num: int, limit: int) -> int:
    """
    Sum all unique multipliers for two numbers.

    The task is to find all the multipliers of two given numbers within the limit.
    Then, find the sum of those multipliers where duplicates are removed.

    All the numbers are positive integers.

    sum_of_multipliers(3, 5, 20) => 98
    We get: [3, 6, 9, 12, 15, 18] (21 is over the limit)
    and [5, 10, 15, 20]
    15 is in both lists, we only use it once, sum is 98

    sum_of_multipliers(3, 3, 20) => 63
    sum_of_multipliers(3, 1, 20) => 210

    :param first_num: first number
    :param second_num: second number
    :param limit: limit
    :return: sum of multiplies
    """
    first_list = [0]
    second_list = [0]

    i = 0
    while first_list[-1] < limit:
        i += 1
        fnum = first_num * i

        if fnum <= limit:
            first_list.append(fnum)
        else:
            break

    i = 0
    while second_list[-1] < limit:
        i += 1
        snum = second_num * i

        if snum <= limit:
            second_list.append(snum)
        else:
            break

    for num in first_list:
        for i, num2 in enumerate(second_list):
            if num == num2:
                second_list.pop(i)

    return sum(first_list) + sum(second_list)


def recursive_max(numbers: list, best: int = 0, start: bool = False) -> int:
    """
    Find max value from the list using recursion.

    No loops allowed.
    You have to find the maximum value of integers in the list.

    recursive_max([]) => 0
    recursive_max([8]) => 8
    recursive_max([8, 9, 10]) => 10
    """
    if not numbers:
        return best

    if not start:
        best = numbers[0]

    if numbers[0] > best:
        best = numbers[0]

    return recursive_max(numbers[1:], best, True)


def make_cupboard(total_width: int, total_height: int, levels: int, sections_on_levels: list) -> str:
    """
    Given measurements of a cupboard, make a cupboard's string representation.

    Variable total_width determines the width of the cupboard,
    total_height determines the height and levels determines how many levels the cupboard has.
    Variable sections_on_levels shows how many sections there are on each level (bottom up).

     The final result should be cupboard's string representation, where sections and levels are separated by '#' and
     also the walls, roof and bottom should be made of '#'.
     The levels should all be of equal height, but the total height should be met.
     The sections on each level should also be of equal width, the total width should again be met.

     If such cupboard can't be made, return a message saying "Can't make cupboard."

     There is not new line in the end of the string.

    Example:
    make_cupboard(42, 10, 2, [3, 2]) =>
    Can't make cupboard.

    Example:
    make_cupboard(43, 11, 2, [3, 2]) =>
    ###########################################
    #                    #                    #
    #                    #                    #
    #                    #                    #
    #                    #                    #
    ###########################################
    #             #             #             #
    #             #             #             #
    #             #             #             #
    #             #             #             #
    ###########################################
    """
    return "Can't make cupboard."


class Book:
    """Represent book model."""

    def __init__(self, title: str, author: str, price: float, rating: float):
        """
        Class constructor.

        Each book has title, author and price.
        :param title: book's title
        :param author: book's author
        :param price: book's price
        """
        self.title = title
        self.author = author
        self.price = price
        self.rating = rating

    def __repr__(self):
        """Return the name of the book."""
        return f"{self.title}, {self.price}, {self.rating}"


class Store:
    """Represent book store model."""

    def __init__(self, name: str, rating: float):
        """
        Class constructor.

        Each book store has name.
        There also should be an overview of all books present in store

        :param name: book store name
        """
        self.name = name
        self.rating = rating
        self.books: list[Book] = list()

    def can_add_book(self, book: Book) -> bool:
        """
        Check if book can be added.

        It is possible to add book to book store if:
        1. The book with the same author and title is not yet present in this book store
        2. book's own rating is >= than store's rating
        :return: bool
        """
        if book.rating < self.rating:
            return False

        for store_book in self.books:
            if store_book.title == book.title and store_book.author == book.author:
                return False

        return True

    def add_book(self, book: Book):
        """
        Add new book to book store if possible.

        :param book: Book
        Function does not return anything
        """
        if self.can_add_book(book):
            self.books.append(book)

    def can_remove_book(self, book: Book) -> bool:
        """
        Check if book can be removed from store.

        Book can be successfully removed if it is actually present in store

        :return: bool
        """
        if book in self.books:
            return True

        return False

    def remove_book(self, book: Book):
        """
        Remove book from store if possible.

        Function does not return anything
        """
        if self.can_remove_book(book):
            self.books.pop(self.books.index(book))

    def get_all_books(self) -> list:
        """
        Return a list of all books in current store.

        :return: list of Book objects
        """
        return self.books

    def get_books_by_price(self) -> list:
        """
        Return a list of books ordered by price (from cheapest).

        :return: list of Book objects
        """
        return sorted(self.books, key=lambda x: x.price)

    def get_most_popular_book(self) -> list:
        """
        Return a list of book (books) with the highest rating.

        :return: list of Book objects
        """
        best_rating = 0
        result = list()

        for store_book in self.books:
            if store_book.rating > best_rating:
                best_rating = store_book.rating

        for store_book in self.books:
            if store_book.rating == best_rating:
                result.append(store_book)

        return result


class ComputerPart:
    """A computer part."""

    def __init__(self, name: str, cost: float):
        """
        ComputerPart constructor.

        Each computer part has a name and a cost.
        """
        self.name = name
        self.cost = cost

    def get_cost(self) -> float:
        """Return the cost of the computer part."""
        return self.cost

    def __repr__(self) -> str:
        """Return the name of the computer part."""
        return self.name


class Computer:
    """A computer at an internet cafe."""

    def __init__(self, name: str, total_parts_needed: int):
        """
        Computer constructor.

        Each computer has name and the amount of parts required for it to function.

        A computer should also keep track of all the parts that are in it.
        :param name: computer name
        :param total_parts_needed: the amount of parts needed for the computer to function
        """
        self.name = name
        self.total_parts_needed = total_parts_needed
        self.cost = 0.00
        self.parts: list[ComputerPart] = list()

    def add_part(self, part: ComputerPart):
        """
        Add a part to the computer.

        The parts cost is also added to the computers cost.

        The part is not added if the computer is already working.
        """
        if not self.is_working():
            self.parts.append(part)
            self.cost += part.cost

    def get_parts_needed(self) -> int:
        """
        Return the amount of parts that is needed to fully build this computer.

        If the computer needs a total of 3 parts and currently has 1 part, this should return 2.
        """
        return self.total_parts_needed - len(self.parts)

    def is_working(self) -> bool:
        """Return if the computer has the correct amount of parts."""
        return len(self.parts) == self.total_parts_needed

    def get_parts(self) -> list[ComputerPart]:
        """
        Return a list of all parts that are in the computer.

        Parts should be in the same order as they were added.
        """
        return self.parts

    def get_cost(self) -> float:
        """Return the cost of the computer."""
        return self.cost

    def __repr__(self) -> str:
        """
        String representation of Computer.

        Returns string in form "A {name} for {cost}€ with {parts}"

        All the parts should be seperated with ", ".
        Parts should be in the same order as they were added.
        If there are no parts in the computer, there should be "nothing".
        Cost is always shown with 2 decimal places.

        Examples:
        "A hardcore gaming computer for 540.30€ with gtx1070, r5 2600, CX650F, EV860"
        "A pc for 0.00€ with nothing"
        """
        parts = ", ".join(part.name for part in self.parts) if self.parts else "nothing"
        return f"A {self.name} for {self.cost:.2f}€ with {parts}"


class Customer:
    """A customer at an internet cafe."""

    def __init__(self, name: str, money: float):
        """
        Constructor.

        Each customer must have a name, money and it should also keep track of owned computers.
        """
        self.name = name
        self.money = money
        self.computers: list[Computer] = list()

    def can_buy_computer(self, computer: Computer) -> bool:
        """Return if this customer has enough money to buy a computer."""
        return self.money >= computer.cost

    def buy_computer(self, computer: Computer) -> bool:
        """
        Buy a computer if it can be done.

        This customer loses money equal to the cost of the computer.

        Returns True or False whether the computer was bought.
        """
        if self.can_buy_computer(computer):
            self.money -= computer.cost
            self.computers.append(computer)
            return True

        return False

    def get_computers(self) -> list[Computer]:
        """Return all computers owned by this customer."""
        return self.computers

    def __repr__(self) -> str:
        """
        String representation of a customer.

        Should be in format:
        "{name} with {money}€
        {computer1}
        {computer2}
        {computer3}
        ..."

        The money is always shown with 2 decimal places.

        example1:
        "Laura with 666.00€
        A hardcore gaming computer for 540.30€ with gtx1070, r5 2600, CX650F, EV860
        A pc for 0.00€ with nothing"

        example2:
        "Karl with 0.00€"
        """
        if not self.get_computers():
            return f"{self.name} with {self.money:.2f}€"

        computers = "".join(computer.__repr__() for computer in self.computers)
        return f"{self.name} with {self.money:.2f}€ {computers}"


class ComputerStore:
    """A store where people can buy computers."""

    def __init__(self):
        """Constructor."""
        self.computers: list[Computer] = list()
        self.parts: list[ComputerPart] = list()
        self.working_computers: list[Computer] = list()

    def add_computer(self, computer: Computer):
        """Add a computer to the store."""
        if computer.is_working():
            self.working_computers.append(computer)
        else:
            self.computers.append(computer)

    def add_part(self, part: ComputerPart):
        """Add a computer part to the storage of the store."""
        self.parts.append(part)

    def get_computers(self) -> list[Computer]:
        """Return all computers in the stores as a list."""
        return self.computers + self.working_computers

    def get_parts(self) -> list[ComputerPart]:
        """Return all unused computer parts in the store."""
        return self.parts

    def get_working_computers(self) -> list[Computer]:
        """Return all computers which are working."""
        return self.working_computers

    def build_computer(self) -> Optional[Computer]:
        """
        Make the store build a computer.

        If the store has no non-functioning computers, return None.

        The store looks at the computer which have the least amount of parts missing.
        If two computers have the same amount of parts missing, then the store picks the one that is cheaper.
        (there aren't any cases where computers parts missing and costs are equal)

        example:
        computer1 costs 100 and 3 parts missing
        computer2 costs 300 and 3 parts missing
        computer3 costs 50 and 4 parts missing
        computer4 costs 10 and 0 parts missing (it is already functional)
        The store chooses to build computer1!

        If the store doesnt have enough spare parts to build a computer, return None.

        The store adds the cheapest available parts to the computer until it is built.

        If the computer is built successfully, return the built computer. Else return None.
        """
        if not self.computers:
            return None

        if not self.parts:
            return None

        best_choises = sorted(self.computers, key=lambda x: (x.get_parts_needed(), x.cost))
        best_parts = sorted(self.parts, key=lambda x: x.cost)

        to_fix = best_choises[0]
        if to_fix.get_parts_needed() > len(best_parts):
            return None

        for part in best_parts:
            if not to_fix.is_working():
                to_fix.add_part(part)
            else:
                break

        self.working_computers.append(to_fix)
        self.computers.pop(self.computers.index(to_fix))

        return to_fix

    def sell_customer_computer(self, customer: Customer):
        """
        A customer walks into the store and wants the most expensive working computer that can be bought with their money.

        Note that the sold computer must work.

        If there are no such computers, the store tries to build a new computer.

        If a computer is successfully built and it is cheap enough to buy, then the customer buys that computer.
        """
        best_choises = sorted(self.working_computers, key=lambda x: -x.cost)

        for computer in best_choises:
            if customer.can_buy_computer(computer):
                customer.buy_computer(computer)
                self.working_computers.pop(self.working_computers.index(computer))
                return

        new = self.build_computer()

        if new and customer.can_buy_computer(new):
            customer.buy_computer(new)
            self.working_computers.pop(self.working_computers.index(new))


if __name__ == '__main__':
    print(double_letters("ab"))  # == "aabb"
    print(double_letters("a! b"))  # == "aa! bb"
    print(double_letters("abc"))  # == "aabbcc"
    print(double_letters("hello world"))  # == "hheelllloo wwoorrlldd"
    print(double_letters("Hi!?"))  # == "HHii!?"
    print()

    print(odds_sum([1, 2, 3]))  # == 4
    print(odds_sum([1]))  # == 1
    print(odds_sum([2, 8, 10, 22]))  # == 0
    print(odds_sum([]))  # == 0
    print()

    print(reverse_subword("tere", "ab"))  # == "tere"
    print(reverse_subword("tere", "te"))  # == "etre"
    print(reverse_subword("teretere", "te"))  # == "etretere"
    print(reverse_subword("abcde", "bc"))  # == "acbde"
    print(reverse_subword("abcabc", "bc"))  # == "acbabc"
    print(reverse_subword("abcabc", "ac"))  # == "abcabc"
    print()

    print(sum_of_multipliers(3, 3, 20))  # == 63
    print(sum_of_multipliers(3, 1, 20))  # == 210
    print()

    print(recursive_max([1, 2, 3]))  # == 3
    print(recursive_max([]))  # == 0
    print(recursive_max([8]))  # == 8
    print(recursive_max([8, 9, 10]))  # == 10
    print(recursive_max([-1, -30, -5]))  # == 10
    print()

    """
    assert make_cupboard(42, 11, 2, [3, 2]) == "Can't make cupboard."
    cupboard = make_cupboard(43, 6, 1, [3])
    print(cupboard)
    assert cupboard[-1] != "\n"
    rows = cupboard.split("\n")
    assert len(rows) == 6
    assert rows[0] == "#" * 43
    assert rows[1] == ("#" + " " * 13) * 3 + "#"
    """

    # Book store
    store = Store("Apollo", 98.9)
    book = Book("War & Peace", "Leo Tolstoy", 10.5, 99)

    print(store.can_add_book(book))  # True

    store.add_book(book)
    print(store.get_all_books())  # [book]

    book2 = Book("War & Peace", "Leo Tolstoy", 10.5, 99)
    print(store.can_add_book(book2))  # False (cannot add book with the same title and author)

    book3 = Book("War", "Leo Tolstoy", 10.5, 80)
    print(store.can_add_book(book3))  # False (cannot add book since its rating is too low)

    book4 = Book("test2", "idk", 12, 222)
    store.add_book(book4)
    book8 = Book("test4", "idk", 12, 222)
    store.add_book(book8)
    book6 = Book("test3", "idk", 6, 99)
    store.add_book(book6)
    book7 = Book("test1", "idk", 33, 105)
    store.add_book(book7)

    print(store.get_all_books())
    print(store.get_books_by_price())
    print(store.get_most_popular_book())
    print()

    # Start of OOP2 ComputerStore
    computer1 = Computer("pc", 3)
    computer1.add_part(ComputerPart("cpu", 200))
    computer1.add_part(ComputerPart("mobo", 60.5))
    computer1.add_part(ComputerPart("case", 70))

    print(computer1.get_cost())  # == 330.5
    print(computer1.is_working())  # True

    computer2 = Computer("laptop", 3)
    computer2.add_part(ComputerPart("display", 160))
    computer2.add_part(ComputerPart("keyboard", 20))

    print(computer2)  # "A laptop for 180.00€ with display, keyboard"
    print(computer2.is_working())  # False

    store = ComputerStore()
    store.add_part(ComputerPart("mousepad", 36))
    store.add_computer(computer1)
    store.add_computer(computer2)

    print(len(store.get_computers()))  # 2
    print(len(store.get_working_computers()))  # 1 computer is working

    store.build_computer()  # add mousepad to laptop

    print(len(store.get_working_computers()))  # 2

    laura = Customer("Laura", 1000)

    store.sell_customer_computer(laura)  # sell pc to laura

    print(len(store.get_computers()))  # 1
    print(laura)
    # "Laura with 669.50€
    # A pc for 330.50€ with cpu, mobo, case"
