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

f=formula1()
f.last_result()

        

    


    




