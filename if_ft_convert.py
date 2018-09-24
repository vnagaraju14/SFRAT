def if_to_ft(interfailure):
    ft = []
    ft.append( interfailure[0] )
    n = 1
    while n < len(interfailure):
        ft.append( interfailure[n] + ft[n - 1] )
        n += 1
    return ft

def ft_to_if(ft):
    interfailure = []
    interfailure.append( ft[0] )
    n = 1
    while n < len(ft):
        interfailure.append( ft[n] - ft[n-1] )
        n += 1
    return interfailure

class ConvertFailType(object):
    # failures is a list
    def __init__(self, failures):
        self.values = failures
        #self.if_or_ft = lower(if_or_ft)

    def if_to_ft(self):
        ft = []
        ft.append( self.values[0] )
        n = 1
        for n in range(len(self.values)):
            ft.append( self.values[n] + ft[n - 1] )
        self.values = ft
        return self.values

    def ft_to_if(self):
        interfailure = []
        interfailure.append( self.values[0] )
        n = 1
        for n in range(len(self.values)):
            interfailure.append( self.values[n] - self.values[n-1] )
        self.values = interfailure
        return self.values

    def __str__(self):
        return str(self.values)


iflist = [3, 5, 4, 7, 2]
failure_times = if_to_ft(iflist)
print(failure_times)

print( ft_to_if(failure_times) )

fails = ConvertFailType(iflist)
print(fails)
print( fails.if_to_ft() )
