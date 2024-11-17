# Text Class
class Text:
    def __init__(self, x, y, text, font, color, align="topleft"):
        self.x = x
        self.y = y
        self.text = text
        self.font = font
        self.color = color
        self.align = align
        self.update()

    def update(self, text=None):
        if text is not None:
            self.text = text
        self.rendered_text = self.font.render(self.text, True, self.color)
        self.text_rect = self.rendered_text.get_rect()
        setattr(self.text_rect, self.align, (self.x, self.y))

    def draw(self, surface):
        surface.blit(self.rendered_text, self.text_rect)