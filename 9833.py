import visa
rm = visa.ResourceManager()
li = rm.list_resources()
for index in range(len(li)):
    print(str(index)+" - "+li[index])
choice = input('Which one?: ')
vi=rm.open_resource(li[int(choice)])
#vi.baud=19200
print(vi.query('*idn?'))
