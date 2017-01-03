import argparse
import io
import shutil

from urllib.request import urlopen

from PIL import Image


def calc_resize(orig_width, orig_height, width, height):
    # 2 pixel for one line
    height = (height - 1) * 2
    ratio_w = orig_width / width
    ratio_h = orig_height / height
    ratio = max(ratio_w, ratio_h)

    return (
        int(orig_width / ratio),
        int(orig_height / ratio))


def show_image(url):
    with urlopen(url) as req:
        file = io.BytesIO(req.read())
        image = Image.open(file).convert('RGB')
    term_size = shutil.get_terminal_size()
    image.thumbnail(calc_resize(*image.size, *term_size), Image.ANTIALIAS)

    buffer = ''

    for y in range(0, image.size[1], 2):
        for x in range(image.size[0]):
            try:
                upper = image.getpixel((x, y))
                color_upper = '38;2;{};{};{}'.format(*upper)
            except:
                color_upper = 1
            try:
                lower = image.getpixel((x, y+1))
                color_lower = '48;2;{};{};{}'.format(*lower)
            except IndexError:
                color_lower = 1

            # print('{} {}'.format(color_upper, color_lower))

            buffer += (
                '\x1b[{color_upper};{color_lower}m'
                '\u2580'.format(
                    color_upper=color_upper,
                    color_lower=color_lower)
            )
        buffer += '\n'
    buffer += '\x1b[0m'
    print(buffer, end='')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('image_url', nargs='?')
    parser.add_argument('--cat', action='store_true',
                        help='Get random cat image.')
    args = parser.parse_args()

    if args.cat:
        show_image('http://thecatapi.com/api/images/get')
    else:
        if not args.image_url:
            parser.print_help()
            exit(1)
        show_image(args.image_url)
