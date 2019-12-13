class UnicodeCollector(object):
    def __init__(self):
        # do some admin on the unicodes of master glyphs
        # aeach glyph can have multiple unicodes
        # so rake in all unicodes of all masters
        self.unicodes = {}
        self.masterCount = 0

    def add(self, glyph):
        # assume these are mathglyphs
        self.masterCount +=1
        if not glyph.unicodes:
            if not None in self.unicodes:
                self.unicodes[None] = 0
            self.unicodes[None]+=1
            return
        for u in glyph.unicodes:
            if not u in self.unicodes:
                self.unicodes[u] = 0
            self.unicodes[u]+=1

    def evaluate(self):
        # so what do we think of what we've seen
        incomplete = []
        for u, count in self.unicodes.items():
            if count != self.masterCount:
                incomplete.append(u)
        return incomplete
        

unicodes = UnicodeCollector()

for font in AllFonts():
    for g in font:
        print(g)
        unicodes .add(g)
        
unicodeResults = unicodes.evaluate()

print(unicodeResults)