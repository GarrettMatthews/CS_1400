def wind_chill(t,v):
    """Finds the wind chill using temperature t with wind speed v"""
    temp = 35.74 + (0.6215 * t) - (35.75 * (v ** 0.16)) + ((0.4275 * t) * (v ** 0.16))
    return temp


print('\t','\t','\t','\t',"Temperature")
print("MPH|",'\t',"-20",'\t',"-10",'\t',"0",'\t',"10",'\t',"20",'\t',"30",'\t',"40",'\t',"50",'\t',"60")
print("---+--------------------------------------------------------")
for v in range(0,52,5):
    t = -20
    print(v,"|",'\t',"{0:.0f}".format(wind_chill(t,v)),'\t',"{0:.0f}".format(wind_chill(t+10,v)),
          '\t',"{0:.0f}".format(wind_chill(t+20,v)),'\t',"{0:.0f}".format(wind_chill(t+30,v)),'\t',
          "{0:.0f}".format(wind_chill(t+40,v)),'\t',"{0:.0f}".format(wind_chill(t+50,v)),'\t',
          "{0:.0f}".format(wind_chill(t+60,v)),'\t',"{0:.0f}".format(wind_chill(t+80,v)),'\t',
          "{0:.0f}".format(wind_chill(t+90,v)))

