import random

#Initialize routes variable and open new routes.txt file.  You will want to make sure you have any previous routes.txt file deleted for this operation unless you want to add to the end of it.
routeCount = 0
routes = open("routes.txt", "w+")

"""
By default this is built for IOS XR.
If you want to utilize for standard IOS uncomment the 3rd routes.write line and comment out the 2nd.
To change the number of loopbacks/routes generated just change the count the while loop ends at.
I've created up to 10,000 routes with no issues experienced configuring on XRv.

Using a while loop rather than a for range to keep sequential numbering while continuing on duplicate network ranges.
oct1 range set to remove networks starting with 0 and anything in class D/E, as well as continuing on non-configurable 127s.
oct4 range set to avoid network and broadcast addresses.
"""
while routeCount <= 1000:
    oct1 = random.randrange(1, 224)
    if oct1 == 127:
        continue
    oct2 = random.randrange(0, 256)
    oct3 = random.randrange(0, 256)
    oct4 = random.randrange(1, 255)
    candidateIP = str(oct1) + "." + str(oct2) + "." + str(oct3) + "." + str(oct4)
    candidateNetwork = str(oct1) + "." + str(oct2) + "." + str(oct3)
    if candidateNetwork in routes.read():
        continue
    else:
        routes.write("\ninterface loopback " + str(routeCount + 1000))
        routes.write("\nipv4 address " + candidateIP + "/24")
        #routes.write("\nip address " + candidateIP + " 255.255.255.0")
        routeCount += 1

routes.close