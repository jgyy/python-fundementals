def l100kmtompg(litres):
    gpm = (litres / 3.785411784) / (100 / 1.609344)
    return 1 / gpm

def mpgtol100km(miles):
    kmpl = (miles * 1.609344) / 3.785411784
    return 100 / kmpl

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))
