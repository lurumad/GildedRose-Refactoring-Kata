class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for i in range(0, len(self.items)):
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





