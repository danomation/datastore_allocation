def allocate(p, c, u, r, un):
    if un.lower() == "gb":
        r = r * 1024
    elif un.lower() != "tb":
        print("Error!")
    if type(p) == str or p < 0:
        print("Error!")
    elif p != 0:
        ## Define increase by percentage
        #To find the remaining percentage after subtracting the requested overhead percentage (100 - p)
        #(100 - p)/100 gives you the fraction of remaining percentage in ratio to 100
        #we then find the reciprocal, 1/((100-p)/100) which is the increase-by-percent
        #(usage+request) * increase-by-percent gives you the new capacity
        ##
        ip = 1/((100-p)/100)
        print("increase by percent is " + str(p))
        #define new capacity size
        nc = (u+r)*ip
        if (nc-c) <= 0:
            print("No expansion required")
            ##define available storage
            #identity ip = c/(u+r+x), solve for x
            #ip*(u+r+x) = c
            #u+r+x = c/ip
            #x = c/ip -u -r
            #what this mean is the increase percentage, e.g. 1.25 for 20 percent is equivalent to \
            #the capacity divided by the sum of usage + request + (available storage)
            ##
            avs = (c/ip)-u-r

            print("Available Storage still remaining: " + str(round(avs, 5)) + " TiB")
            input("press enter to exit...")
        else:
            #define request storage
            rs = nc - c
            print("Request storage: " + str(round(rs, 5)) + " TiB or " + str(round(rs*1024, 5)) + " GiB")
            print("After request, new Total Datastore Capacity is " + str(round(nc, 5)) + " TiB\n")
            print("The new Datastore Used/Datastore Capacity incl. the request will be " + str(round(u+r, 5)) + "/" + str(nc) + " TiB")
            print("This is " + str(round(((u+r)/nc)*100, 5)) + " Percent used, which allows for " + str(round(p, 5)) + " percent Overhead")
            input("press enter to exit...")


if __name__ == '__main__':
    percent = float(input('Type in the percent of overhead e.g. "20" is 20%.\n'))
    capacity = float(input('What is the Current Datastore Capacity? e.g "20.5" means 20.5 TB\n'))
    used = float(input('How much Datastore is Used currently? e.g. "10.1" means 10.1 TB\n'))
    request = float(input('How much storage will the new server(s) take up? e.g. "20" (no unit)\n'))
    unit = input('Which storage unit, GB or TB? "gb" or "tb"\n')
    allocate(percent, capacity, used, request, unit)
