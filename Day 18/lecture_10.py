import colorgram

colors = colorgram.extract('image.jpg', 30)

rgb_list = []
for color in colors:
    rgb_tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
    rgb_list.append(rgb_tuple)

print(rgb_list)

