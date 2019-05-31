places={'salem':0,'chennai':300,'coimbatore':200,'madurai':400}
source=input("Enter Source:")
des=input("Enter destination:")
km=places[des]-places[source]
print("Total Distance:",km)
print("Modes of Transport Avaible")
print("Car")
print("bus")
print("Auto")
m=input("Enter mode of Transport:")
if(m=='car' or m=='Car' or m=='CAR'):
    baseamo=50
    perkm=5
    print("Base Amount:",baseamo)
    print("Per Km=",perkm)
    rate=(km*perkm)+baseamo
    print("Total Amount:",rate)
if(m=='bus' or m=='Bus' or m=='BUS'):
    baseamo=100
    perkm=10
    print("Base Amount",baseamo)
    print("Per Km=",perkm)
    rate=(km*perkm)+baseamo
    print("Total Amount:",rate)
if(m=='Auto' or m=='auto' or m=='AUTO'):
    baseamo=25
    perkm=3
    print("Base Amount",baseamo)
    print("Per Km=",perkm)
    rate=(km*perkm)+baseamo
    print("Total Amount:",rate)
    

