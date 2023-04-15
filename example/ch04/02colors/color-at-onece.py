# メモリに全て読み込んでから処理 - 非効率
color_counts = {}
with open('README.md') as favorite_colors_file:
    favorite_colors = favorite_colors_file.read().splitlines()

for color in favorite_colors:
    if color in color_counts:
        color_counts[color] += 1
    else:
        color_counts[color] = 1
