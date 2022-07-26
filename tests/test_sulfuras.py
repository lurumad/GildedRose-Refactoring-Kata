from gilded_rose.gilded_rose import GildedRose
from gilded_rose.sulfuras import Sulfuras


class TestsSulfuras:
    def test_sulfuras_is_a_legendary_item_and_as_such_its_quality_is_80_and_it_never_alters(self):
        items = [Sulfuras(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 80

