"""Santa's Workshop Tests."""
import santas_workshop


# Gift class tests
gift = santas_workshop.Gift("computer", 5000)


def test__gift__get_name():
    """Test gift class get_name."""
    assert gift.get_name() == "computer"


def test__gift__get_weight():
    """Test gift class get_weight."""
    assert gift.get_weight() == 5000


def test__gift__get_weight_kg():
    """Test gift class get_weight_kg."""
    assert gift.get_weight_kg() == 5


# Child class tests
child = santas_workshop.Child("Alex", "Estonia", "computer")


def test__child__get_name():
    """Test child class get_name."""
    assert child.get_name() == "Alex"


def test__child__get_country():
    """Test child class get_country."""
    assert child.get_country() == "Estonia"


def test__child__get_wish():
    """Test child class get_wish."""
    assert child.get_wish() == "computer"


# Children class tests
children = santas_workshop.Children()


def test__children__get():
    """Test children class get."""
    assert len(children.get()) == 0


def test__children__add():
    """Test children class add."""
    children.add(child)
    children.add(santas_workshop.Child("Oliver", "Estonia", "playstation 5"))
    children.add(santas_workshop.Child("Rein", "Estonia", "phone"))
    children.add(santas_workshop.Child("Siim", "Estonia", "car"))

    assert len(children.get()) == 4


def test__children__has():
    """Test children class has."""
    assert children.has("Alex") is True
    assert children.has("Mati") is False


def test__children__get_child_by_name():
    """Test children class get_child_by_name."""
    assert children.get_child_by_name("Alex") is child


def test__children__from_country():
    """Test children class from_country."""
    children.add(santas_workshop.Child("John", "Sweden", "computer"))
    children.add(santas_workshop.Child("Keith", "Sweden", "xbox"))

    assert len(children.from_country("Sweden")) == 2
    assert len(children.from_country("Estonia")) == 4


# Warehouse class tests
warehouse = santas_workshop.Warehouse()


def test__warehouse__get_gifts():
    """Test warehouse class get_gifts."""
    assert len(warehouse.get_gifts()) == 0


def test__warehouse__add():
    """Test warehouse class add."""
    for _ in range(3):
        warehouse.add(gift)

    warehouse.add(santas_workshop.Gift("playstation 5", 2500))
    warehouse.add(santas_workshop.Gift("phone", 800))
    warehouse.add(santas_workshop.Gift("xbox", 3000))
    warehouse.add(santas_workshop.Gift("car", 46000))

    assert len(warehouse.get_gifts()) == 5
    assert len(warehouse.get_gifts().get("computer")) == 3
    assert len(warehouse.get_gifts().get("playstation 5")) == 1


def test__warehouse__has():
    """Test warehouse class has."""
    assert warehouse.has("playstation 5") is True
    assert warehouse.has("nintendo") is False


def test__warehouse__get():
    """Test warehouse class get."""
    assert len(warehouse.get_gifts().get("computer")) == 3
    warehouse.get("computer")
    assert len(warehouse.get_gifts().get("computer")) == 2

    assert warehouse.has("xbox") is True
    warehouse.get("xbox")
    assert warehouse.has("xbox") is False


def test__warehouse__get_gift_by_name():
    """Test warehouse class get_gift_by_name."""
    assert warehouse.get_gift_by_name("computer") is gift


# Sleigh class tests
sleigh = santas_workshop.Sleigh("Estonia", child, gift)


def test__sleigh__get_country():
    """Test sleigh class get_country."""
    assert sleigh.get_country() == "Estonia"


def test__sleigh__get_gifts():
    """Test sleigh class get_gifts."""
    assert len(sleigh.get_gifts()) == 1


def test__sleigh__get_weight_kg():
    """Test sleigh class get_weight_kg."""
    assert sleigh.get_weight_kg() == 5


def test__sleigh__get_weight():
    """Test sleigh class get_weight."""
    assert sleigh.get_weight() == 5000


def test__sleigh__add():
    """Test sleigh class add."""
    assert sleigh.add(children.get_child_by_name("Siim"), warehouse.get("car")) is False
    assert len(sleigh.get_gifts()) == 1
    assert sleigh.get_weight() == 5000

    assert sleigh.add(children.get_child_by_name("Rein"), warehouse.get("phone")) is True
    assert len(sleigh.get_gifts()) == 2
    assert sleigh.get_weight() == 5800

    assert sleigh.add(children.get_child_by_name("Oliver"), warehouse.get("playstation 5")) is True
    assert len(sleigh.get_gifts()) == 3
    assert sleigh.get_weight() == 8300


def test__sleigh__create_receipt():
    """Test sleigh class create_receipt."""
    assert sleigh.create_receipt() == r"""                        DELIVERY ORDER
                                                          _v
                                                     __* (__)
             ff     ff     ff     ff                {\/ (_(__).-.
      ff    <_\__, <_\__, <_\__, <_\__,      __,~~.(`>|-(___)/ ,_)
    o<_\__,  (_ ff ~(_ ff ~(_ ff ~(_ ff~~~~~@ )\/_;-"``     |
      (___)~~//<_\__, <_\__, <_\__, <_\__,    | \__________/|
      // >>     (___)~~(___)~~(___)~~(___)~~~~\\_/_______\_//
                // >>  // >>  // >>  // >>     `'---------'`

FROM: NORTH POLE CHRISTMAS CHEER INCORPORATED
TO: Estonia

//========[]===============[]==================\\
||  Name  ||     Gifts     || Total Weight(kg) ||
|]========[]===============[]==================[|
|| Alex   || computer      ||              5.0 ||
|| Rein   || phone         ||              0.8 ||
|| Oliver || playstation 5 ||              2.5 ||
\\========[]===============[]==================//"""


def test__sleigh__print_receipt():
    """Test sleigh class print_receipt."""
    sleigh.print_receipt()

    with open("receipts/Estonia_0.txt"):
        assert True


# PostOffice class tests
postoffice = santas_workshop.PostOffice(5)


def test__postoffice__decrypt_base64():
    """Test PostOffice class decrypt_base64."""
    assert postoffice.decrypt_base64("dGVzdCBiYXNlNjQgZGVjb2Rl==") == "test base64 decode"


def test__postoffice__decrypt_cipher():
    """Test PostOffice class decrypt_cipher."""
    assert postoffice.decrypt_cipher("xiwx gmtliv higshi") == "test cipher decode"


def test__postoffice__read():
    """
    Test PostOffice class read.

    Constructor already calls read, check if wishes and letters combined give us the letters to read :count:.
    """
    assert len(postoffice.get_wishes()) + len(postoffice.get_letters()) == 5


def test__postoffice__reply():
    """
    Test PostOffice class reply.

    Constructor already calls reply, just check if personal reply file was created.
    """
    if not postoffice.get_letters():
        return

    with open(f"letters/{postoffice.get_letters()[0]}.txt") as file:
        assert file.read() == fr"""Dear {postoffice.get_letters()[0]}!

Thank You for Your letter.
Merry Christmas and Happy New Year!

Santa, North Pole"""


# Workshop class tests
workshop = santas_workshop.Workshop("nice_test.csv", "naughty_test.csv", "wish_test.csv", 0)
_children = workshop.get_children()
_warehouse = workshop.get_warehouse()
_postoffice = workshop.get_postoffice()


def test__workshop__get_children():
    """
    Test Workshop class get_children.

    Constructor calls read_data_from_files, check if we got all children from nice_test.txt list.
    """
    assert len(_children.get()) == 5
    assert _children.get()[0].get_name() == "Libby"
    assert _children.get()[2].get_name() == "Amelia"
    assert _children.get()[4].get_name() == "Ben"


def test__workshop__get_warehouse():
    """
    Test Workshop class get_warehouse.

    Constructor calls read_data_from_files, check if children wishes were created and added to warehouse.
    """
    assert len(_warehouse.get_gifts()) == 4
    assert len(_warehouse.get_gifts().get("zebra jumpy")) == 1
    assert len(_warehouse.get_gifts().get("wall-mount diamond pickaxe")) == 2
    _warehouse.add(santas_workshop.Gift("dumbbell", 49500))  # Something heavy for testing purpose


def test__workshop__get_postoffice():
    """
    Test Workshop class get_postoffice.

    Read no letters from API, because it makes testing difficult. Instead add few ourselves.
    """
    _postoffice.get_letters().append("Tony")
    _postoffice.get_letters().append("Tanya")
    _postoffice.get_letters().append("Keira")
    _postoffice.get_wishes().update({"Ben": ["United Kingdom", "polar bear plushie"]})
    _postoffice.get_wishes().update({"Jamie": ["Sweden", "raspberry pi 4"]})
    _postoffice.get_wishes().update({"Igor": ["Germany", "dumbbell"]})

    assert len(_postoffice.get_letters()) == 3
    assert len(_postoffice.get_wishes()) == 3


def test__workshop__get_countries():
    """Test Workshop class get_countries."""
    assert workshop.get_countries() == ["United Kingdom", "Germany", "Sweden"]


def test__workshop__create_gift__new():
    """Test Workshop class create_gift new."""
    assert _warehouse.has("lego death star") is False
    workshop.create_gift("lego death star")
    assert _warehouse.has("lego death star") is True


def test__workshop__create_gift__existing():
    """Test Workshop class create_gift existing."""
    assert len(_warehouse.get_gifts().get("zebra jumpy")) == 1
    workshop.create_gift("zebra jumpy")
    assert len(_warehouse.get_gifts().get("zebra jumpy")) == 2


def test__workshop__handle_letters():
    """Test Workshop class handle_letters."""
    assert len(_children.get()) == 5
    assert len(_warehouse.get_gifts().get("dumbbell")) == 1

    workshop.handle_letters("naughty_test.csv")

    assert len(_warehouse.get_gifts().get("dumbbell")) == 2
    assert len(_children.get()) == 6
    assert _children.get()[5].get_name() == "Igor"
    assert _children.has("Jamie") is False


def test__workshop__get_sleighs():
    """Test Workshop class get_sleighs."""
    assert len(workshop.get_sleighs()) == 0


def test__workshop__prepare_sleighs():
    """Test Workshop class prepare_sleighs."""
    workshop.prepare_sleighs()
    assert len(workshop.get_sleighs()) == 3


def test__workshop__get_sleighs_by_country():
    """Test Workshop class get_sleighs_by_country."""
    assert len(workshop.get_sleighs_by_country("Sweden")) == 1
    assert len(workshop.get_sleighs_by_country("Germany")) == 2
    assert len(workshop.get_sleighs_by_country("United Kingdom")) == 1


def test__workshop__print_sleighs_receipts():
    """Test Workshop class print_sleighs_receipts."""
    workshop.print_sleighs_receipts()

    with open("receipts/Germany_0.txt"):
        assert True

    with open("receipts/Germany_1.txt"):
        assert True

    with open("receipts/Sweden_0.txt"):
        assert True

    with open("receipts/United Kingdom_0.txt"):
        assert True
