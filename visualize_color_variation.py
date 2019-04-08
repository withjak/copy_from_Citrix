import numpy as np
from PIL import Image, ImageDraw
import ccmap


def main(test_string):
    # set reference points location
    reference_point = [(10, 10), (20, 20)]

    # forming white sheet
    data = np.zeros((400, 800, 3), dtype=np.uint8) + 255
    im = Image.fromarray(data)

    # creating an object to help to draw on image
    draw = ImageDraw.Draw(im)

    # plot reference point
    draw.rectangle(reference_point, fill=(0, 0, 0), outline=None)

    # plot rectangle for each character
    coordinate = ccmap.coordinates()
    mapping = ccmap.mapping()
    for char in test_string:
        draw.rectangle(next(coordinate), fill=mapping[char], outline=None)

    im.save('color_test.png')
    im.show()
    print('length of test_string: ', len(test_string))


if __name__ == '__main__':
    # test_string = r"""today is the greatest day in human history because it is :) and kal ho na ho"""
    test_string = r"""hese implementations are for demonstration purposes
     hey are less efficient than the implementations in the Python standard library.Sorting AlgorithmsBubble Sort""".lower()
    main(test_string)
