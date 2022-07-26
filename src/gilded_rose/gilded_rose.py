class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for i in range(0, len(self.items)):
            if "Normal" == self.items[i].name:
                self.items[i].update_quality()
                return

            if "Aged Brie" == self.items[i].name:
                self.items[i].update_quality()
                return

            if "Backstage passes to a TAFKAL80ETC concert" == self.items[i].name:
                self.backstage_passes_update_quality(self.items[0])
                return

            if "Sulfuras, Hand of Ragnaros" == self.items[0].name:
                self.sulfuras_update_quality(self.items[0])
                return
        return self.items

    @staticmethod
    def backstage_passes_update_quality(item):
        item.sell_in -= 1
        item.quality += 1
        if item.sell_in <= 0:
            item.quality = 0
            return
        if item.sell_in <= 10:
            item.quality += 1
        if item.sell_in <= 5:
            item.quality += 1
        if item.quality > 50:
            item.quality = 50

    @staticmethod
    def sulfuras_update_quality(item):
        return
