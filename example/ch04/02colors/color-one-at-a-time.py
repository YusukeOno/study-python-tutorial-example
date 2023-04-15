# 1行ずつ読み込み
color_counts = {}
with open('README.md') as favorite_colors_file:
    for color in favorite_colors_file:
        color = color.strip()

        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1
