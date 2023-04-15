# 集合（set）を使って色を記憶
all_colors = set()

with open('README.md') as favorite_colors_file:
    for line in favorite_colors_file:
        all_colors.add(line.strip())

print('琥珀' in all_colors)
