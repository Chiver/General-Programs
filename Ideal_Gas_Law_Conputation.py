
### __________User Guide__________###
user_guide = '''Put in your goddamn parameters in the following sequence: p, v, n, t; if unknown, put in 0.
If you with to stop, put in "stop" \n'''
print(user_guide)

### __________Void Loop__________###
while True:
    inp = input('P, V, n, T = ')
    if inp == 'stop':
        break
    
    parameters_init = inp.split(',')
    
    if len(parameters_init) != 4:
        print( 'Bad input, check again.')
        break
    
    parameters = {}
    parameters['p'] = float(parameters_init[0])
    parameters['v'] = float(parameters_init[1])
    parameters['n'] = float(parameters_init[2])
    parameters['t'] = float(parameters_init[3])
    #print('\n')


    ### _____Function_____ ###
    def ideal_gas(parameters):
        '''
            p = pressure
            v = volumn
            n = moles
            t = temperature in kelvin
        '''
        r = 0.08206 # ideal gas constant

        if parameters['p'] ==0:
            return 'P = ' + str(parameters['n'] * r * parameters['t'] / parameters['v']) + ' atm\n'
        elif parameters['v'] == 0:
            return 'V = '+ str(parameters['n'] * r * parameters['t'] / parameters['p']) + ' liters\n'
        elif parameters['n'] == 0:
            return 'n = ' + str(parameters['p'] * parameters['v'] / r / parameters['t']) + ' moles\n'
        elif parameters['t'] == 0:
            return 'T = ' + str(parameters['p'] * parameters['v'] / parameters['n'] / r) + ' kelvin\n'

    print(ideal_gas(parameters))



    '''
    '''

