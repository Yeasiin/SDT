from ride import Ride,RideMatching,RideRequest,RideSharing
from user import Rider, Driver
from vehicle import Car, Bike


uraw = RideSharing("Uraw")

riderYeasin = Rider("Yeasin","yeasin@mail.com",12344,"chittagong",1200)
driverArfat = Driver("Arfat","arfat@mail.com",23432,"Dhaka")

uraw.add_rider(riderYeasin)
uraw.add_driver(driverArfat)

riderYeasin.request_ride(uraw,'Chittagong','car')

driverArfat.reach_destination(riderYeasin.current_ride)
riderYeasin.show_current_ride()

print(uraw)






