arrow_base_height = int(input('Enter arrow base height:\n'))

arrow_base_width = int(input('Enter arrow base width:\n'))

arrow_head_width = int(input('Enter arrow head width:\n'))
while arrow_head_width <= arrow_base_width:
    arrow_head_width = int(input('Enter arrow head width:\n'))
print('')
for i in range(1, arrow_base_height +1):
    print('*' * arrow_base_width)

for h in range(arrow_head_width, 0, -1):
    print('*' * h)
