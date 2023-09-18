
class DoubleQuotedList(list):
    def __str__(self):
        formatted_elements = [f'"{item}"' if isinstance(item, str) else item for item in self]
        return "[" + ", ".join(formatted_elements) + "]"

# Create a DoubleQuotedList
my_list = DoubleQuotedList(['https://www.herogame.vn/danh-muc/game-nintendo-switch', 'https://www.herogame.vn/danh-muc/game-nintendo-switch?keyword=&page_size=50&sorted=priority_desc&page=2&minRange=&maxRange=', 'https://www.herogame.vn/danh-muc/game-nintendo-switch?keyword=&page_size=50&sorted=priority_desc&page=3&minRange=&maxRange=', 'https://www.herogame.vn/danh-muc/game-nintendo-switch?keyword=&page_size=50&sorted=priority_desc&page=4&minRange=&maxRange=', 'https://www.herogame.vn/danh-muc/game-nintendo-switch?keyword=&page_size=50&sorted=priority_desc&page=5&minRange=&maxRange=', 'https://www.herogame.vn/danh-muc/game-nintendo-switch?keyword=&page_size=50&sorted=priority_desc&page=6&minRange=&maxRange=', 'https://www.herogame.vn/danh-muc/game-nintendo-switch?keyword=&page_size=50&sorted=priority_desc&page=7&minRange=&maxRange=', 'https://www.herogame.vn/danh-muc/game-nintendo-switch?keyword=&page_size=50&sorted=priority_desc&page=8&minRange=&maxRange=', 'https://www.herogame.vn/danh-muc/game-nintendo-switch?keyword=&page_size=50&sorted=priority_desc&page=9&minRange=&maxRange=', 'https://www.herogame.vn/danh-muc/game-nintendo-switch?keyword=&page_size=50&sorted=priority_desc&page=10&minRange=&maxRange=', 'https://www.herogame.vn/danh-muc/game-nintendo-switch?keyword=&page_size=50&sorted=priority_desc&page=11&minRange=&maxRange='])

# Print the DoubleQuotedList
print(my_list)  # Thi