RESET = '\033[0m'

class colour:
    colour_map = {
        'black': 16, 'red': 196, 'green': 28, 'yellow': 226, 'blue': 21,
        'magenta': 201, 'cyan': 51, 'white': 231, 'gray': 102, 'silver': 145,
        'maroon': 88, 'olive': 100, 'lime': 46, 'teal': 30, 'navy': 18,
        'fuchsia': 201, 'aqua': 51,
        'aqua_marine': 122, 'azure': 231, 'beige': 230, 'bisque': 224,
        'blanched_almond': 230, 'blue_violet': 92, 'brown': 124, 'cadet_blue': 73,
        'coral': 209, 'corn_flower_blue': 69, 'cornsilk': 230, 'crimson': 161,
        'dark_blue': 18, 'dark_cyan': 30, 'dark_golden_rod': 136, 'dark_khaki': 143,
        'dark_magenta': 90, 'dark_olive_green': 58, 'dark_orange': 208,
        'dark_orchid': 98, 'dark_red': 88, 'dark_salmon': 174,
        'dark_sea_green': 108, 'dark_slate_blue': 60, 'dark_slate_gray': 23,
        'dark_turquoise': 44, 'dark_violet': 92, 'deep_pink': 198,
        'deep_sky_blue': 39, 'dodger_blue': 33, 'fire_brick': 124, 'gold': 220,
        'golden_rod': 178, 'honeydew': 231, 'hot_pink': 205, 'indian_red': 167,
        'indigo': 54, 'khaki': 222, 'lavender': 189, 'lavender_blush': 231,
        'lemon_chiffon': 230, 'light_blue': 152, 'light_coral': 210,
        'light_cyan': 195, 'light_golden_rod_yellow': 230, 'light_pink': 217,
        'light_salmon': 216, 'light_sea_green': 37, 'light_sky_blue': 117,
        'medium_aquamarine': 79, 'medium_blue': 20, 'medium_orchid': 134,
        'medium_purple': 98, 'medium_slate_blue': 99, 'medium_turquoise': 80,
        'medium_violet_red': 162, 'midnight_blue': 17, 'mint_cream': 231,
        'moccasin': 223, 'navajo_white': 223, 'olive_drab': 64, 'orange': 214,
        'orange_red': 202, 'orchid': 170, 'pale_golden_rod': 223,
        'pale_turquoise': 159, 'pale_violet_red': 168, 'peach_puff': 223,
        'pink': 218, 'plum': 182, 'powder_blue': 152, 'purple': 90,
        'royal_blue': 62, 'salmon': 209, 'sky_blue': 117, 'slate_blue': 62,
        'steel_blue': 67, 'thistle': 182, 'tomato': 203, 'turquoise': 80,
        'violet': 213, 'wheat': 223, 'yellow_green': 113
    }

    def __getattr__(self, name):
        # handle changing function names
        def colour_function(text):
            code_or_name = self.parse_colour(name)
            if code_or_name is type(int):
                code_or_name = str(code_or_name)
            elif code_or_name is None:
                raise ValueError(f"unknown colour: {name}")
            return f"\033[38;5;{code_or_name}m" + f"{text}" + RESET
        return colour_function

    def parse_colour(self, code_or_name):

        if code_or_name in self.colour_map:
            return self.colour_map[code_or_name]
        elif code_or_name[4:].isdigit() and int(code_or_name[4:]) <= 256:
            if code_or_name[:4] == "ansi":
                return int(code_or_name[4:])
            else:
                raise ValueError(f"unknown colour format: {code_or_name[:4]}")
        return None

    def ansi_remind(self):
        for i in range(0, 256):
            colour = f"\033[38;5;{i:03d}m"
            if i == 17 or i == 231:
                carriage = "\n" + ("=") * 71 + "\n"
            elif (i + 1) % 18 == 0 and (i + 1) < 18 * 13:
                carriage = "\n"
            else:
                carriage = " "
            print(colour + f"{i:03d}" + RESET, end=carriage)

c = colour()
verbose = True
if verbose == True:
    
    def verbose_print(*args):
        for arg in args:
            print(arg, "\n", end="")
else:
    def verbose_print(*args):
        pass
    

if __name__ == "__main__":
    c.ansi_remind()
    print(c.ansi196("red text here"))
    verbose_print(c.ansi111("verbose text here"))
