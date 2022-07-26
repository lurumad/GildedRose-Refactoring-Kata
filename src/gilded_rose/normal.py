from gilded_rose.item import Item


class Normal(Item):
    def update_quality(self):
        self.sell_in -= 1
        self.quality -= 1
        if self.sell_in <= 0:
            self.quality -= 1
        if self.quality < 0:
            self.quality = 0
        if self.quality > 50:
            self.quality = 50