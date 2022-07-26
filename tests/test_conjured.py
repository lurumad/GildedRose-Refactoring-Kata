from gilded_rose.conjured import Conjured
from gilded_rose.gilded_rose import GildedRose


class TestConjuredItems:
    def test_conjured_items_degrade_in_quality_twice_as_fast_as_normal_items_when_the_sell_by_date_has_not_passed(self):
        items = [Conjured(name="Conjured", sell_in=10, quality=8)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 6
        assert items[0].sell_in == 9

    def test_conjured_items_degrade_in_quality_twice_as_fast_as_normal_items_when_the_sell_by_date_has_passed(self):
        items = [Conjured(name="Conjured", sell_in=0, quality=8)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 4
        assert items[0].sell_in == -1
