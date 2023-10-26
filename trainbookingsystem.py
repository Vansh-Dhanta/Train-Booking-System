print("\n\n\nTrain Ticket Booking System")

print("\nPLAN YOUR JOURNEY")
From = str(input("\nEnter Departure City: "))
To = str(input("\nEnter Destination City: "))
Date = str(input("\nEnter date of travel (DD/MM/YYYY): "))
Train = To.upper() + " EXPRESS"

quotalst = ["GENERAL", "LADIES", "TATKAL", "SENIOR CITIZEN", "PWD"]
print("\nQUOTA PREFERENCE: ", quotalst)

Quota = str(input("\nEnter Preferable Quota: "))
Quota = Quota.upper()

Classlst = ["ACFIRSTCLASS", "AC2TIER", "AC3TIER", "SLEEPER"]
name_1 = []
age_1 = []
sex_1 = []

if Quota == quotalst[0]:
    print("\nCLASS PREFERENCE: ", Classlst)
    Class = str(input("\n\nEnter Preferable Class: "))
    Class = Class.upper()

    if Class == Classlst[0]:
        print("\nTicket Fare for AC First Class Rs. 3500")
        noftickets = int(input("\nEnter Number of Persons: "))
        totalfare = noftickets * 3500
        totalfare = int(totalfare)

        for i in range(noftickets):
            name = str(input("\nName : "))
            name_1.append(name)
            age = int(input("\nAge : "))
            age_1.append(age)
            sex = str(input("\nMale or Female : "))
            sex_1.append(sex)

        print("\nTotal fare: Rs. ", totalfare)

    elif Class == Classlst[1]:
        print("\nTicket Fare for AC 2 Tier Rs. 2200")
        noftickets = int(input("\nEnter Number of Persons: "))
        totalfare = noftickets * 2200
        totalfare = int(totalfare)

        for i in range(noftickets):
            name = str(input("\nName : "))
            name_1.append(name)
            age = int(input("\nAge : "))
            age_1.append(age)
            sex = str(input("\nMale or Female : "))
            sex_1.append(sex)

        print("\nTotal fare: Rs. ", totalfare)

    elif Class == Classlst[2]:
        print("\nTicket Fare for AC 3 Tier Rs. 1500")
        noftickets = int(input("\nEnter Number of Persons: "))
        totalfare = noftickets * 1500
        totalfare = int(totalfare)

        for i in range(noftickets):
            name = str(input("\nName : "))
            name_1.append(name)
            age = int(input("\nAge : "))
            age_1.append(age)
            sex = str(input("\nMale or Female : "))
            sex_1.append(sex)

        print("\nTotal fare: Rs. ", totalfare)

    elif Class == Classlst[3]:
        print("\nTicket Fare for Sleeper Class Rs. 800")
        noftickets = int(input("\nEnter Number of Persons: "))
        totalfare = noftickets * 800
        totalfare = int(totalfare)

        for i in range(noftickets):
            name = str(input("\nName : "))
            name_1.append(name)
            age = int(input("\nAge : "))
            age_1.append(age)
            sex = str(input("\nMale or Female : "))
            sex_1.append(sex)

        print("\nTotal fare: Rs. ", totalfare)

elif Quota == quotalst[1]:
    print("\nCLASS PREFERENCE: ", Classlst)
    Class = str(input("\n\nEnter Preferable Class: "))
    Class = Class.upper()
    print("\nWe're providing 20% discount for Ladies")

    if Class == Classlst[0]:
        print("\nTicket Fare for AC First Class Rs. 2800")
        noftickets = int(input("\nEnter Number of Persons: "))
        totalfare = noftickets * 2800
        totalfare = int(totalfare)

        for i in range(noftickets):
            name = str(input("\nName : "))
            name_1.append(name)
            age = int(input("\nAge : "))
            age_1.append(age)
            sex = str(input("\nMale or Female : "))
            sex_1.append(sex)

        print("\nTotal fare: Rs. ", totalfare)

    elif Class == Classlst[1]:
        print("\nTicket Fare for AC 2 Tier Rs. 1760")
        noftickets = int(input("\nEnter Number of Persons: "))
        totalfare = noftickets * 1760
        totalfare = int(totalfare)

        for i in range(noftickets):
            name = str(input("\nName : "))
            name_1.append(name)
            age = int(input("\nAge : "))
            age_1.append(age)
            sex = str(input("\nMale or Female : "))
            sex_1.append(sex)

        print("\nTotal fare: Rs. ", totalfare)

    elif Class == Classlst[2]:
        print("\nTicket Fare for AC 3 Tier Rs. 1200")
        noftickets = int(input("\nEnter Number of Persons: "))
        totalfare = noftickets * 1200
        totalfare = int(totalfare)

        for i in range(noftickets):
            name = str(input("\nName : "))
            name_1.append(name)
            age = int(input("\nAge : "))
            age_1.append(age)
            sex = str(input("\nMale or Female : "))
            sex_1.append(sex)

        print("\nTotal fare: Rs. ", totalfare)

    elif Class == Classlst[3]:
        print("\nTicket Fare for Sleeper Class Rs. 640")
        noftickets = int(input("\nEnter Number of Persons: "))
        totalfare = noftickets * 640
        totalfare = int(totalfare)

        for i in range(noftickets):
            name = str(input("\nName : "))
            name_1.append(name)
            age = int(input("\nAge : "))
            age_1.append(age)
            sex = str(input("\nMale or Female : "))
            sex_1.append(sex)

        print("\nTotal fare: Rs. ", totalfare)
