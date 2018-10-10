def land_robbery_assessment():
    assess = 0.0
    land_val = float(input('What is the value of your land?:'))
    assess = (land_val * 0.6)
    theft = .72 * (assess / 100)
    print('Your assessment value is $%0.2f'% assess)
    print('While your property tax is $%0.2f'% theft)
    return

land_robbery_assessment()
