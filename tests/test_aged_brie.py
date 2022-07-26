from gilded_rose.gilded_rose import GildedRose
from gilded_rose.item import Item


class TestAgedBrie:
    def test_aged_brie_increases_in_quality_by_two_when_there_are_ten_or_less_days_remaining(self):
        items = [Item(name="Aged Brie", sell_in=10, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 22
        assert items[0].sell_in == 9

    def test_aged_brie_increases_in_quality_by_three_when_there_are_five_or_less_days_remaining(self):
        items = [Item(name="Aged Brie", sell_in=5, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 23
        assert items[0].sell_in == 4

    def test_aged_brie_quality_drops_to_zero_when_no_days_remaining(self):
        items = [Item(name="Aged Brie", sell_in=0, quality=40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 0
        assert items[0].sell_in == -1
