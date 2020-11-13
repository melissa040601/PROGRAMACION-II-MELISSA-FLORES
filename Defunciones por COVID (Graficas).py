import matplotlib.pyplot as PLT


Est = ['Coahuila', 'Tabasco', 'Puebla', 'Tamaulipas', 'Sonora','Sumatoria']
Defunciones = (1452, 2620, 3620, 1850,2678,12220 )
colores = ('pink', 'red', 'green', 'yellow', 'purple', 'gray')

PLT.barh(range(6),Defunciones,color=colores)
PLT.yticks(range(6), Est, rotation = 60)
PLT.title ("Defunciones por Covid-19")
PLT.xlim(min(Defunciones)-10,max(Defunciones)+1000)
PLT.show()
