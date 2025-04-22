import requests
import json


# url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJbbvccbIUzI1nbvmvbmNiJ9.eyJhdWQiOiJkMDExMW23434ZiMDdjYTljbNDYyMGRmZWNjMçTlhMTJlYzJmMSIsInN1YnghiI6IjY2MDUyYTI1ZjkwYjE5MDE0OWE3OGMwOSIsInNjb3BlcyI6Wy52454JhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.HduHEYJaJUfBjhgggXFfT3I30RFCOwQL-2mCnlvjuxrXwl7g"
}


# response = requests.get(url, headers=headers)

# print(response.text)



class TheMovieDb:
    def  __init__(self) -> None:
        self.api_url = "https://api.themoviedb.org/3"
        self.api_key = "d0111fb07ca9c4jjgfgfffhg620d576676fecc19jga12ec2f1"
        self.headers = headers

    def getPopular(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        formatted_response = json.dumps(response.json(), indent=4)
        return formatted_response
    
    def searchMovie(self, keyword):
        response = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyword}&page=1'")
        formatted_response = json.dumps(response.json(), indent=4)
        return formatted_response


    
themoviedb = TheMovieDb()




while True:
    secim = input("1-Popular Movies\n2-Search\n3-Exit\nChoice: ")
    if secim == "3":
        break
    else:
        if secim == "1":
            movies = themoviedb.getPopular()
            movies = json.loads(movies)
            for movie in movies["results"]:
                print(movie["title"])
            # print(movies)

        elif secim == "2":
            keyword = input("Search Keyword: ")
            search = themoviedb.searchMovie(keyword)
            search = json.loads(search)
            for s in search["results"]:
                print(s["name"])

