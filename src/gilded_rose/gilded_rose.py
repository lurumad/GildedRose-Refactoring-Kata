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
                self.items[i].update_quality()
                return

            if "Sulfuras, Hand of Ragnaros" == self.items[0].name:
                self.items[i].update_quality()
                return
        return self.items
