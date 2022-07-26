from gilded_rose.gilded_rose import GildedRose
from gilded_rose.normal import Normal


class TestsNormalItem:
    def test_quality_of_an_item_is_never_negative(self):
        items = [Normal(name="Normal", sell_in=0, quality=1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 0

    def test_normal_items_quality_degrades_by_one_when_the_sell_by_date_has_not_passed(self):
        items = [Normal(name="Normal", sell_in=6, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 9
        assert items[0].sell_in == 5

    def test_normal_items_quality_degrades_twice_as_fast_when_the_sell_by_date_has_passed(self):
        items = [Normal(name="Normal", sell_in=0, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 8
        assert items[0].sell_in == -1

    def test_the_quality_of_an_item_is_never_more_than_50(self):
        items = [Normal(name="Normal", sell_in=0, quality=100)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 50
        assert items[0].sell_in == -1
