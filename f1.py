import requests



class formula1:
    def __init__(self): 
        self.payload = {}
        self.headers = {}

    def driverdatabase_season(self,year):
        dirver_in_season = "http://ergast.com/api/f1/{}/drivers".format(year)+".json"
        response = requests.request("GET", dirver_in_season, headers=self.headers, data=self.payload)
        database = eval(response.text)
        return database['MRData']['DriverTable']

    def display(self,year):
        db=self.driverdatabase_season(year)
        print("Drivers in Formula 1 season 2021:\n")
        for key in db['Drivers']:
            try:
                if int(key['permanentNumber'])<10:
                    print(" "+key['permanentNumber']+"  "+ key['code'] +":  "+key['givenName'] + " " + key['familyName'])
                else:
                    print(key['permanentNumber']+"  "+ key['code'] +":  "+key['givenName'] + " " + key['familyName'])
            except:
                print("NA"+"  "+ key['code'] +":  "+key['givenName'] + " " + key['familyName'])

    def last_result(self):
        url = "http://ergast.com/api/f1/current/last/results.json"
        response = requests.request("GET", url, headers=self.headers, data=self.payload)
        db = eval(response.text)
        db=db['MRData']['RaceTable']['Races'][0]
        print("\nRound {} Forumla 1 season {} :".format(db['round'],db['season']))
        print(db['raceName'])
        print("At circuit {} ,{} {}".format(db['Circuit']['circuitName'],db['Circuit']['Location']['locality'],db['Circuit']['Location']['country']))
        print("Date: {}  Time: {}".format(db['date'],db['time']))
        print("Pos\tNo\tDriver\t\t\tLaps\tPoints")
        for key in db['Results']:
            try:
            except:
                if key['status']=="Disqualified":
                    status="DQ"
                elif key['status']=='Collision':
                    status="DNF"
                else:
                    status=key['status']
                print("{}\t{}\t{}\t\t{}\t{}".format(key['position'],key['number'],key['Driver']['givenName']+" " +key['Driver']['familyName'],key['laps'],status,key['points'] ))



f=formula1()
f.last_result()

        

    


    




