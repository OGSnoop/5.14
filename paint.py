def paint_wizard(wall_space, paint_price):
    gallons = wall_space / 112
    hours = gallons * 8
    labor = hours * 35
    tot_paint = paint_price * gallons
    tot_cos = labor + tot_paint

    print('You wall will require %f gallons of paint' % gallons)
    print('This job will demand %f hours of labor' % hours)
    print('The cost for all of this paint will be $%0.2f' % tot_paint)
    print('Labor charge will come to $%0.2f' % labor)
    print('Total cost for job comes to $%0.2f' % tot_cos)
    return


wall_space = float(input('How much squared feet would you like painted?\n'))
paint_price = float(input('How much per gallon does the paint cost which you wish for us too use?\n'))
paint_wizard(wall_space, paint_price)
