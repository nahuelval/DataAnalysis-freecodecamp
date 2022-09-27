import numpy as np

def calculate(arg):
    a = np.array(arg)
    b = np.reshape(a, (3,3))

    value1 = list(np.mean(b, axis=0))
    value2 = list(np.mean(b, axis=1))
    value3 = np.mean(a, axis=0)

    dicc = {}

    dicc.update({'mean': [value1,value2,value3]})

    value1 = list(np.var(b, axis=0))
    value2 = list(np.var(b, axis=1))
    value3 = np.var(a, axis=0)

    dicc.update({'variance': [value1,value2,value3]})

    value1 = list(np.std(b, axis=0))
    value2 = list(np.std(b, axis=1))
    value3 = np.std(a, axis=0)

    dicc.update({'standard deviation': [value1,value2,value3]})

    value1 = list(np.amax(b, axis=0))
    value2 = list(np.amax(b, axis=1))
    value3 = np.amax(a, axis=0)

    dicc.update({'max': [value1,value2,value3]})

    value1 = list(np.amin(b, axis=0))
    value2 = list(np.amin(b, axis=1))
    value3 = np.amin(a, axis=0)

    dicc.update({'min': [value1,value2,value3]})

    value1 = list(np.sum(b, axis=0))
    value2 = list(np.sum(b, axis=1))
    value3 = np.sum(a, axis=0)

    dicc.update({'sum': [value1,value2,value3]})

    for key, value in dicc.items():
        print(key, ' : ', value)