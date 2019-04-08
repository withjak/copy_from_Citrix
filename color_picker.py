from PIL import Image, ImageDraw
from ccmap import coordinates, rev_map


def find_reference_point(image):
    reference_box = []
    # 30m pixels
    for y in range(30):
        for x in range(30):
            # Tuples always compare its first index and gives output according to your program.
            # it does not compare all the elements.
            if image.getpixel((x, y)) < (10, 10, 10):
                reference_box.append((x, y))
    # print('These coordinates have dark pixels required for reference_box', reference_box)
    x0 = sum(pt[0] for pt in reference_box) / len(reference_box)
    y0 = sum(pt[1] for pt in reference_box) / len(reference_box)
    print('\n\nMiddle point of reference_box: ', x0, y0)
    return int(x0), int(y0)


def main23(src_img):
    text = ''
    reference_pt_orig_loc = (15, 15)
    im = Image.open(src_img)
    rgb_im = im.convert('RGB')

    x0, y0 = find_reference_point(rgb_im)
    shift_x = reference_pt_orig_loc[0] - x0
    shift_y = reference_pt_orig_loc[1] - y0

    rev_mapping = rev_map()

    for upper_l, lower_r in coordinates():
        upper_l = upper_l[0] - shift_x, upper_l[1] - shift_y
        lower_r = lower_r[0] - shift_x, lower_r[1] - shift_y

        draw = ImageDraw.Draw(im)
        draw.rectangle([upper_l, lower_r], outline='black')

        r, g, b = 0, 0, 0
        for x in range(upper_l[0], lower_r[0]):
            for y in range(upper_l[1], lower_r[1]):
                _r, _g, _b = rgb_im.getpixel((x, y))
                r += _r
                g += _g
                b += _b
        r, g, b = int(r/100), int(g/100), int(b/100)

        # when all boxes are over, stop picking background white sheet as characters
        if r > 200 and g > 200 and b > 200:
            print('White box detected. Stopping now...')
            break
        print('color: ', (r, g, b), ' mapped to: ', rev_mapping[(r, g, b)])
        text += rev_mapping[(r, g, b)]
    print(text)

    im.save('tes2_edit.png')
    im.show()


if __name__ == '__main__':
    img = 'color_test.png'
    main23(src_img=img)
