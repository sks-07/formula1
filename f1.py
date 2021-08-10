import requests
from datetime import date
import xmltodict
import json

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
        url2 = "http://ergast.com/api/f1/{}/{}/status.json".format(db['season'],db['round'])
        response2 = requests.request("GET", url2, headers=self.headers, data=self.payload)
        db2 = eval(response2.text)
        db2=db2['MRData']['StatusTable']['Status']
        a=[]
        for key in db2:
            if(key['status'][0]=='+'):pass
            else:
                a.append(key['status'])
        print("\nRound {} Forumla 1 season {} :".format(db['round'],db['season']))
        print(db['raceName'])
        print("At circuit {} ,{} {}".format(db['Circuit']['circuitName'],db['Circuit']['Location']['locality'],db['Circuit']['Location']['country']))
        print("Date: {}  Time: {}".format(db['date'],db['time']))
        print ("{:<8} {:<8} {:<20} {:<10} {:<15} {:<10}".format('Pos','No','Driver','Laps','Time','Points'))
        print ("{:<8} {:<8} {:<20} {:<10} {:<15} {:<10}".format('---','--','------','----','----','------'))
        for key in db['Results']:
            try:
                print("{:<8} {:<8} {:<20} {:<10} {:<15} {:<10}".format(key['position'],key['number'],key['Driver']['givenName']+" " +key['Driver']['familyName'],key['laps'],key['Time']['time'],key['points'] ))
            except:
                flag=0
            
                for k in a:
                    if k==key['status']:
                        flag=1
                        break
                
                if key['status']=="Disqualified":
                    status="DQ"
                elif flag==0:
                    status=key['status']
                elif flag==1:
                    status="DNF"
                print("{:<8} {:<8} {:<20} {:<10} {:<15} {:<10}".format(key['position'],key['number'],key['Driver']['givenName']+" " +key['Driver']['familyName'],key['laps'],status,key['points'] ))

    def race_result(self,year,round):
        url = "http://ergast.com/api/f1/{}/{}/results.json".format(year,round)
        url2 = "http://ergast.com/api/f1/{}/{}/status.json".format(year,round)
        response = requests.request("GET", url, headers=self.headers, data=self.payload)
        response2 = requests.request("GET", url2, headers=self.headers, data=self.payload)
        db = eval(response.text)
        db2 = eval(response2.text)
        db=db['MRData']['RaceTable']['Races'][0]
        db2=db2['MRData']['StatusTable']['Status']
        a=[]
        for key in db2:
            if(key['status'][0]=='+'):pass
            else:
                a.append(key['status'])

        print("\nRound {} Forumla 1 season {} :".format(db['round'],db['season']))
        print(db['raceName'])
        print("At circuit {} ,{} {}".format(db['Circuit']['circuitName'],db['Circuit']['Location']['locality'],db['Circuit']['Location']['country']))
        print("Date: {}  Time: {}".format(db['date'],db['time']))
        print ("{:<8} {:<8} {:<20} {:<10} {:<15} {:<10}".format('Pos','No','Driver','Laps','Time','Points'))
        print ("{:<8} {:<8} {:<20} {:<10} {:<15} {:<10}".format('---','--','------','----','----','------'))
        for key in db['Results']:
            try:
                print("{:<8} {:<8} {:<20} {:<10} {:<15} {:<10}".format(key['position'],key['number'],key['Driver']['givenName']+" " +key['Driver']['familyName'],key['laps'],key['Time']['time'],key['points'] ))
            except:
                flag=0
            
                for k in a:
                    if k==key['status']:
                        flag=1
                        break
                
                if key['status']=="Disqualified":
                    status="DQ"
                elif flag==0:
                    status=key['status']
                elif flag==1:
                    status="DNF"

                print("{:<8} {:<8} {:<20} {:<10} {:<15} {:<10}".format(key['position'],key['number'],key['Driver']['givenName']+" " +key['Driver']['familyName'],key['laps'],status,key['points'] ))



    def diver_standing(self,year):
        url = "http://ergast.com/api/f1/{}/driverStandings.json".format(year)
        response = requests.request("GET", url, headers=self.headers, data=self.payload)
        db=eval(response.text)
        db=db['MRData']['StandingsTable']['StandingsLists'][0]
        print("\n\t\tDrivers Championship Forumla 1 season {}".format(db['season']))
        print("\t\t------------------------------------------ \n")
        print ("{:<8} {:<30} {:<15} {:<20} {:<15}".format('Pos','Driver','Wins','Team','Points'))
        print ("{:<8} {:<30} {:<15} {:<20} {:<15}".format('---','------','----','----','------'))
        for key in db['DriverStandings']:
            print ("{:<8} {:<30} {:<15} {:<20} {:<15}".format(key['position'],key['Driver']['givenName']+" "+key['Driver']['familyName'],key['wins'],key['Constructors'][0]['name'],key['points']))

    def team_standing(self,year):
        url = "http://ergast.com/api/f1/{}/constructorStandings.json".format(year)
        response = requests.request("GET", url, headers=self.headers, data=self.payload)
        db=eval(response.text)
        db=db['MRData']['StandingsTable']['StandingsLists'][0]
        print("\n\tConstructor Championship Forumla 1 season {}".format(db['season']))
        print("\t---------------------------------------------- \n")
        print ("{:<8} {:<25} {:<15} {:<20} ".format('Pos','Team','Wins','Points'))
        print ("{:<8} {:<25} {:<15} {:<20} ".format('---','----','----','------'))
        for key in db['ConstructorStandings']:
             print ("{:<8} {:<25} {:<15} {:<20} ".format(key['position'],key['Constructor']['name'],key['wins'],key['points']))
    

    def all_drivers_champions(self,yearf,yeart):
        limit=date.today().year-1950
        url = "http://ergast.com/api/f1/driverStandings/1?limit={}.json".format(limit)
        response = requests.request("GET", url, headers=self.headers, data=self.payload)
        db=json.dumps(xmltodict.parse(response.text))
        db=eval(db)
        db=db['MRData']['StandingsTable']['StandingsList']
        y1=yearf-1950
        y2=yeart-1950
        print("\n\t\tForumla 1 World Diver Champions")
        print("\t\t-------------------------------\n")
        print ("{:<8} {:<25} {:<15} {:<15} {:<20} ".format('Year','Driver','Wins','Team','Points'))
        print ("{:<8} {:<25} {:<15} {:<15} {:<20} ".format('---','------','----','----','------'))
        for i in range(y1,y2+1):
             print ("{:<8} {:<25} {:<15} {:<15} {:<20} ".format(db[i]['@season'],db[i]['DriverStanding']['Driver']['GivenName']+" "+db[i]['DriverStanding']['Driver']['FamilyName'],db[i]['DriverStanding']['@wins'],db[i]['DriverStanding']['Constructor']['Name'],db[i]['DriverStanding']['@points']))

    def driver_champion_year(self,year):
        self.all_drivers_champions(year,year)

    
    def all_Team_champions(self,yearf,yeart):
        if date.today().month<12 and yeart==date.today().year:
            yeart-=1
        limit=date.today().year-1958
        url = "http://ergast.com/api/f1/constructorStandings/1?limit={}.json".format(limit)
        response = requests.request("GET", url, headers=self.headers, data=self.payload)
        db=json.dumps(xmltodict.parse(response.text))
        db=eval(db)
        db=db['MRData']['StandingsTable']['StandingsList']
        y1=yearf-1958
        y2=yeart-1958
        print("\n\t\tForumla 1 World Diver Champions")
        print("\t\t-------------------------------\n")
        print ("{:<8} {:<25} {:<15} {:<20} ".format('Year','Team','Wins','Points'))
        print ("{:<8} {:<25} {:<15} {:<20} ".format('---','------','----','----','------'))
        for i in range(y1,y2+1):
             print ("{:<8} {:<25} {:<15} {:<20} ".format(db[i]['@season'],db[i]['ConstructorStanding']['Constructor']['Name'],db[i]['ConstructorStanding']['@wins'],db[i]['ConstructorStanding']['@points']))
    
    def team_champion_year(self,year):
        self.all_drivers_champions(year,year)

    def qualifying_time(self,year,roun):
        url = "http://ergast.com/api/f1/{}/{}/qualifying.json".format(year,roun)
        response = requests.request("GET", url, headers=self.headers, data=self.payload)
        db=eval(response.text)
        db=db['MRData']['RaceTable']['Races'][0]
        print("\t\t\t\tRound {} Formula 1 season {}".format(roun,year))
        print("\t\t\t\t-------------------------------")
        print("{} Qualifying Highlights at {}, {} {}".format(db['raceName'],db['Circuit']['circuitName'],db['Circuit']['Location']['locality'],db['Circuit']['Location']['country']))
        #print("Date: {} Time: {}".format(db['date'],db['time']))
        print("----------------------------------------------------------------------------------------------------------")
        print ("{:<8} {:<25} {:<20} {:<20} {:<20} {:<20} ".format('Pos','Driver','Team','Q1','Q2','Q3'))
        print ("{:<8} {:<25} {:<20} {:<20} {:<20} {:<20} ".format('---','------','----','--','--','--'))
        for key in db['QualifyingResults']:
            try:
                print ("{:<8} {:<25} {:<20} {:<20} {:<20} {:<20} ".format(key['position'],key['Driver']['givenName']+ " "+key['Driver']['familyName'],key['Constructor']['name'],key['Q1'],key['Q2'],key['Q3']))
            except:
                try:
                    print ("{:<8} {:<25} {:<20} {:<20} {:<20} {:<20} ".format(key['position'],key['Driver']['givenName']+ " "+key['Driver']['familyName'],key['Constructor']['name'],key['Q1'],key['Q2'],"--------"))
                except:
                    print ("{:<8} {:<25} {:<20} {:<20} {:<20} {:<20} ".format(key['position'],key['Driver']['givenName']+ " "+key['Driver']['familyName'],key['Constructor']['name'],key['Q1'],"--------","--------"))

f=formula1()
f.race_result(2021,11)


        

    


    




