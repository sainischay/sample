red = ['Miyapur', 'JNTU', 'KPHP colony', 'Kukatpally', 'Balanagar', 'Moosapet', 'Bharat Nagar', 'Erragadda',
       'ESI hospital', 'SR nagar', 'Ameerpet', 'Punjagutta', 'Irrum Manzil', 'Kairatabad', 'Lakdi-ka-pul', 'Assembly',
       'Nampally', 'Gandhi bhavan', 'Osmania college', 'MG station', 'Malakpet', 'New Market', 'Musarambah',
       'Dilsukhnagar', 'Chaitanyapuri', 'Victoria memorial', 'LB nagar']
blue = ['Raidurg', 'Hitec city', 'Durgam cheruvu', 'Madhapur', 'Peddamma gudi', 'Jubilee hills', 'Yusufguda',
        'Madhura nagar', 'Ameerpet', 'Begumpet', 'Prakash nagar', 'Rasoolpura', 'Paradise', 'Parade ground',
        'Secunderabad east', 'Mettuguda', 'Tarnaka', 'Habsiguda', 'NGRI', 'Stadium', 'Uppal', 'Nagole']
green = ['Parade ground', 'Secunderabad west', 'Gandhi hospital', 'Musheerabad', 'RTC X roads', 'Chikkadpally',
         'Narayanaguda', 'Sultan bazaar', 'MG station']
white = [red, blue, green]

s = input('Enter the station:\n')
e = input('Enter the station:\n')
no = int(input('Enter 1 if minimal amount of station changes and 0 for minimum ticket price:\n'))
if s != e and (red.count(s) != 0 or blue.count(s) != 0 or green.count(s) != 0) and (
        red.count(e) != 0 or blue.count(e) != 0 or green.count(e) != 0):
    if red.count(s) == 1 and red.count(e) == 1:
        n = 10 + ((abs(red.index(s) - red.index(e)) - 1) * 5)
        print(f"Start with destination {s} and drop in station {e} using red line and ticket charges are {n} ")


    elif blue.count(s) == 1 and blue.count(e) == 1:
        n = 10 + ((abs(blue.index(s) - blue.index(e)) - 1) * 5)
        print(f"Start with destination {s} and drop in station {e} using blue line and ticket charges are {n} ")


    elif green.count(s) == 1 and green.count(e) == 1:
        n = 10 + ((abs(green.index(s) - green.index(e)) - 1) * 5)
        print(f"Start with destination {s} and drop in station {e} using green line and ticket charges are {n} ")


    elif red.count(s) == 1 and blue.count(e) == 1:
        x = set(red)
        y = set(blue)
        a = set(green)
        b = list(x.intersection(a))[0]
        c = list(y.intersection(a))[0]
        z = list(x.intersection(y))[0]
        m = 10 + (((abs(red.index(s) - red.index(b)) + abs(green.index(b) - green.index(c)) + abs(
            blue.index(c) - blue.index(e))) - 1) * 5)
        n = 10 + (((abs(red.index(s) - red.index(z)) + abs(blue.index(z) - blue.index(e))) - 1) * 5)

        if (n <= m or no == 1):
            print(
                f"Start with destination {s} drop at station {z} to change track and drop finally at {e} ticket price is {n} ")
        else:
            print(
                f"Start with destination {s} drop at station {b} and again drop at station {c} and drop finally at {e} and price is {m} ")


    elif red.count(s) == 1 and green.count(e) == 1:
        x = set(red)
        y = set(green)
        a = set(blue)
        b = list(x.intersection(a))[0]
        c = list(y.intersection(a))[0]
        z = list(x.intersection(y))[0]
        m = 10 + (((abs(red.index(s) - red.index(b)) + abs(blue.index(b) - blue.index(c)) + abs(
            green.index(c) - green.index(e))) - 1) * 5)
        n = 10 + (((abs(red.index(s) - red.index(z)) + abs(green.index(z) - green.index(e))) - 1) * 5)
        if (n <= m or no == 1):
            print(
                f"Start with destination {s} drop at station {z} to change track and drop finally at {e} ticket price is {n} ")
        else:
            print(
                f"Start with destination {s} drop at station {b} and again drop at station {c} and drop finally at {e} and price is {m} ")



    elif blue.count(s) == 1 and green.count(e) == 1:
        x = set(blue)
        y = set(green)
        a = set(red)
        b = list(x.intersection(a))[0]
        c = list(y.intersection(a))[0]
        z = list(x.intersection(y))[0]
        m = 10 + (((abs(blue.index(s) - blue.index(b)) + abs(red.index(b) - red.index(c)) + abs(
            green.index(c) - green.index(e))) - 1) * 5)
        n = 10 + (((abs(blue.index(s) - blue.index(z)) + abs(green.index(z) - green.index(e))) - 1) * 5)
        if (n <= m or no == 1):
            print(
                f"Start with destination {s} drop at station {z} to change track and drop finally at {e} ticket price is {n} ")
        else:
            print(
                f"Start with destination {s} drop at station {b} and again drop at station {c} and drop finally at {e} and price is {m} ")


    elif blue.count(s) == 1 and red.count(e) == 1:
        x = set(blue)
        y = set(red)
        a = set(green)
        b = list(x.intersection(a))[0]
        c = list(y.intersection(a))[0]
        z = list(x.intersection(y))[0]
        n = 10 + (((abs(blue.index(s) - blue.index(z)) + abs(red.index(z) - red.index(e))) - 1) * 5)
        m = 10 + (((abs(blue.index(s) - blue.index(b)) + abs(green.index(b) - green.index(c)) + abs(
            red.index(c) - red.index(e))) - 1) * 5)
        if (n <= m or no == 1):
            print(
                f"Start with destination {s} drop at station {z} to change track and drop finally at {e} ticket price is {n} ")
        else:
            print(
                f"Start with destination {s} drop at station {b} and again drop at station {c} and drop finally at {e} and price is {m} ")


    elif green.count(s) == 1 and blue.count(e) == 1:
        x = set(green)
        y = set(blue)
        a = set(red)
        b = list(x.intersection(a))[0]
        c = list(y.intersection(a))[0]
        z = list(x.intersection(y))[0]
        m = 10 + (((abs(green.index(s) - green.index(b)) + abs(red.index(b) - red.index(c)) + abs(
            blue.index(c) - blue.index(e))) - 1) * 5)
        n = 10 + (((abs(green.index(s) - green.index(z)) + abs(blue.index(z) - blue.index(e))) - 1) * 5)
        if (n <= m or no == 1):
            print(
                f"Start with destination {s} drop at station {z} to change track and drop finally at {e} ticket price is {n} ")
        else:
            print(
                f"Start with destination {s} drop at station {b} and again drop at station {c} and drop finally at {e} and price is {m} ")


    elif green.count(s) == 1 and red.count(e) == 1:
        x = set(green)
        y = set(red)
        a = set(blue)
        b = list(x.intersection(a))[0]
        c = list(y.intersection(a))[0]
        z = list(x.intersection(y))[0]
        m = 10 + (((abs(green.index(s) - green.index(b)) + abs(blue.index(b) - blue.index(c)) + abs(
            red.index(c) - red.index(e))) - 1) * 5)
        n = 10 + (((abs(green.index(s) - green.index(z)) + abs(red.index(z) - red.index(e))) - 1) * 5)
        if (n <= m or no == 1):
            print(
                f"Start with destination {s} drop at station {z} to change track and drop finally at {e} ticket price is {n} ")
        else:
            print(
                f"Start with destination {s} drop at station {b} and again drop at station {c} and drop finally at {e} and price is {m} ")

elif s == e:
    print("Invalid--Both the inputs are same")

else:
    print("Invalid Input or spelling mistake")






