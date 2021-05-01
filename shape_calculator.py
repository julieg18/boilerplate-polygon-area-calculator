class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return self.width * 2 + self.height * 2

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if (self.height > 50 or self.width > 50):
            return 'Too big for picture.'
        rect_row = '*' * self.width
        return f'{rect_row}\n' * self.height

    def get_amount_inside(self, rect):
        if (self.width < rect.width or self.height < rect.height):
            return 0
        current_area = self.get_area()
        rect_area = rect.get_area()
        amount = 0
        while (current_area >= rect_area):
            current_area -= rect_area
            amount += 1
        return amount


class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)

    def set_height(self, height):
        super().set_height(height)
        super().set_width(height)

    def set_width(self, width):
        super().set_width(width)
        super().set_height(width)

    def __str__(self):
        return f'Square(side={self.height})'

    def set_side(self, side):
        self.width = side
        self.height = side
