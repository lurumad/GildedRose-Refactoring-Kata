from gilded_rose.gilded_rose import GildedRose
from gilded_rose.item import Item


class TestsSulfuras:
    def test_sulfuras_is_a_legendary_item_and_as_such_its_quality_is_80_and_it_never_alters(self):
        items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 80

