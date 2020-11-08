import json
import requests as req

class Matchflix():
    def __init__(self, movieId):
        self.movieId = movieId
        
    def GetDetails(self):
        url = "https://unogsng.p.rapidapi.com/title"
        querystring = {"netflixid":self.movieId}
        headers = {
        'x-rapidapi-host': "unogsng.p.rapidapi.com",
        'x-rapidapi-key': "44f2c854c9msh70052d5b0318de0p115f87jsna34187fcf3fb"
        }
        response = req.request("GET", url, headers=headers, params=querystring)
        self.Details = json.loads(response.content)

    def GetCountries(self):
        url = "https://unogsng.p.rapidapi.com/titlecountries"
        querystring = {"netflixid":self.movieId}
        headers = {
        'x-rapidapi-host': "unogsng.p.rapidapi.com",
        'x-rapidapi-key': "44f2c854c9msh70052d5b0318de0p115f87jsna34187fcf3fb"
        }
        response = req.request("GET", url, headers=headers, params=querystring)
        obj = json.loads(response.content)
        countries = []
        i = 0
        for i in range(len(obj['results'])):
            country = obj['results'][i]['country']
            countries.append(country)
            i += 1
        self.Countries = countries
        
    def isInSweden(self):
        if 'Sweden' in str(self.Countries):
            return True
        else:
            return False
    def isInUK(self):
        if 'United Kingdom' in str(self.Countries):
            return True
        else:
            return False
    def isInAmerica(self):
        if 'United States' in str(self.Countries):
            return True
        else:
            return False 
    def getTitle(self):
        obj = self.Details
        title = obj['results'][0]['title']
        return title
    def getPlot(self):
        obj = self.Details
        snippet = obj['results'][0]['imdbplot']
        return snippet
    def getImdbruntime(self):
        obj = self.Details
        runtime = obj['results'][0]['imdbruntime']
        return runtime
    def getYear(self):
        obj = self.Details
        year = obj['results'][0]['year']
        return year
    def getGenre(self):
        obj = self.Details
        genre = obj['results'][0]['imdbgenre']
        return genre
    def getMatlabel(self):
        obj = self.Details
        matlabel = obj['results'][0]['matlabel']
        return matlabel
    def getImg(self):
        obj = self.Details
        img = obj['results'][0]['img']
        return img
    def getSynopsis(self):
        obj = self.Details
        synopsis = obj['results'][0]['synopsis']
        return synopsis
    def getRuntime(self):
        obj = self.Details
        runtime = obj['results'][0]['imdbruntime']
        return runtime