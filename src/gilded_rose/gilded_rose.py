class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for i in range(0, len(self.items)):

            if "Normal" == self.items[i].name:
                self.normal_update_quality(self.items[i])
                return

            if "Aged Brie" == self.items[i].name:
                self.aged_brie_update_quality(self.items[0])
                return

            if "Backstage passes to a TAFKAL80ETC concert" == self.items[i].name:
                self.backstage_passes_update_quality(self.items[0])
                return

            if "Sulfuras, Hand of Ragnaros" == self.items[0].name:
                self.sulfuras_update_quality(self.items[0])
                return

            if "Aged Brie" != self.items[i].name and "Backstage passes to a TAFKAL80ETC concert" != self.items[i].name:
                if self.items[i].quality > 0:
                    if "Sulfuras, Hand of Ragnaros" != self.items[i].name:
                        self.items[i].quality = self.items[i].quality - 1
            else:
                if self.items[i].quality < 50:
                    self.items[i].quality = self.items[i].quality + 1
                    if "Aged Brie" == self.items[i].name:
                        if self.items[i].sell_in < 6:
                            self.items[i].quality = self.items[i].quality + 1
                    if "Aged Brie" == self.items[i].name:
                        if self.items[i].sell_in < 11:
                            self.items[i].quality = self.items[i].quality + 1
                    if "Backstage passes to a TAFKAL80ETC concert" == self.items[i].name:
                        if self.items[i].sell_in < 11:
                            # See revision number 2394 on SVN.
                            if self.items[i].quality < 50:
                                self.items[i].quality = self.items[i].quality + 1
                        if self.items[i].sell_in < 6:
                            if self.items[i].quality < 50:
                                self.items[i].quality = self.items[i].quality + 1
            if "Sulfuras, Hand of Ragnaros" != self.items[i].name:
                self.items[i].sell_in = self.items[i].sell_in - 1
            if self.items[i].sell_in < 0:
                if "Aged Brie" != self.items[i].name:
                    if "Backstage passes to a TAFKAL80ETC concert" != self.items[i].name:
                        if self.items[i].quality > 0:
                            if "Sulfuras, Hand of Ragnaros" != self.items[i].name:
                                self.items[i].quality = self.items[i].quality - 1
                    else:
                        self.items[i].quality = self.items[i].quality - self.items[i].quality
                else:
                    if self.items[i].quality < 50:
                        self.items[i].quality = self.items[i].quality + 1
                    if "Aged Brie" == self.items[i].name and self.items[i].sell_in <= 0:
                        self.items[i].quality = 0
            if "Sulfuras, Hand of Ragnaros" != self.items[i].name:
                if self.items[i].quality > 50:
                    self.items[i].quality = 50
        return self.items

    @staticmethod
    def normal_update_quality(item):
        item.sell_in -= 1
        item.quality -= 1
        if item.sell_in <= 0:
            item.quality -= 1
        if item.quality < 0:
            item.quality = 0
        if item.quality > 50:
            item.quality = 50

    @staticmethod
    def aged_brie_update_quality(item):
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


