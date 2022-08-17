from unicodedata import name
from django.db import models
from django.db import models

# Create your models here.
class Test(models.Model):
  name =  models.CharField(max_length=250, null=True)

class Genres(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return str(self.name)

class Production_companies(models.Model):
    logo_path = models.CharField(max_length=250, null=True, blank=True)
    name = models.CharField(max_length=250)
    origin_country = models.CharField(max_length=4, null=True, blank= True)

    def __str__(self):
        return str(self.name)

class Production_countries(models.Model):
    iso_3166_1 = models.CharField(null=False, max_length=4, blank=True)
    name = models.CharField(max_length=250)

    def __str__(self):
        return str(self.name)

class Spoken_languages(models.Model):
    iso_639_1 = models.CharField(null=False, max_length=4, blank=True)
    name = models.CharField(max_length=250)

    def __str__(self):
        return str(self.name)

class Movie(models.Model):
    """
      class Movie models field
    """  
    movie_name = models.CharField(null=False, max_length=250)
    description = models.TextField(null=True, max_length=200, blank=True)
    date_c = models.DateTimeField(null=True),
    adult = models.BooleanField (null=True, default=False)
    is_active = models.BooleanField (null=True, default=False)
    backdrop_path = models.CharField(null=True, max_length=250, blank=True)
    genres = models.ForeignKey(Genres, on_delete=models.CASCADE, null=True, blank=True)
    homepage = models.CharField(null=False, max_length=250, blank=True)
    imdb_id = models.CharField(null=False, max_length=250, blank=True)
    original_language = models.CharField(null=False, max_length=4, blank=True)
    original_title = models.CharField(null=False, max_length=250, blank=True)
    overview = models.TextField(null=True, blank=True)
    popularity = models.FloatField(null=True, default=None)
    poster_path = models.CharField(null=True, default=None, max_length=250)
    production_companies = models.ForeignKey(Production_companies,on_delete=models.CASCADE, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    revenue = models.CharField(null=True, default=None, max_length=250)
    runtime = models.CharField(null=True, default=None, max_length=250)
    spoken_languages = models.ForeignKey(Spoken_languages, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(null=True, default=None, max_length=50)
    tagline = models.TextField(null=True, blank=True)
    title = models.CharField(null=True, default=None, max_length=250)
    video = models.BooleanField (null=True, default=False)
    vote_average = models.FloatField(null=True, default=None)
    vote_count = models.IntegerField(null=True)


    def __str__(self):
        return str(self.movie_name)





"""
 
{
  "adult": false,
  "backdrop_path": "/fCayJrkfRaCRCTh8GqN30f8oyQF.jpg",
  "belongs_to_collection": null,
  "budget": 63000000,
  "genres": [
    {
      "id": 18,
      "name": "Drama"
    }
  ],
  "homepage": "",
  "id": 550,
  "imdb_id": "tt0137523",
  "original_language": "en",
  "original_title": "Fight Club",
  "overview": "A ticking-time-bomb insomniac and a slippery soap salesman channel primal male aggression into a shocking new form of therapy. Their concept catches on, with underground \"fight clubs\" forming in every town, until an eccentric gets in the way and ignites an out-of-control spiral toward oblivion.",
  "popularity": 0.5,
  "poster_path": null,
  "production_companies": [
    {
      "id": 508,
      "logo_path": "/7PzJdsLGlR7oW4J0J5Xcd0pHGRg.png",
      "name": "Regency Enterprises",
      "origin_country": "US"
    },
    {
      "id": 711,
      "logo_path": null,
      "name": "Fox 2000 Pictures",
      "origin_country": ""
    },
    {
      "id": 20555,
      "logo_path": null,
      "name": "Taurus Film",
      "origin_country": ""
    },
    {
      "id": 54050,
      "logo_path": null,
      "name": "Linson Films",
      "origin_country": ""
    },
    {
      "id": 54051,
      "logo_path": null,
      "name": "Atman Entertainment",
      "origin_country": ""
    },
    {
      "id": 54052,
      "logo_path": null,
      "name": "Knickerbocker Films",
      "origin_country": ""
    },
    {
      "id": 25,
      "logo_path": "/qZCc1lty5FzX30aOCVRBLzaVmcp.png",
      "name": "20th Century Fox",
      "origin_country": "US"
    }
  ],
  "production_countries": [
    {
      "iso_3166_1": "US",
      "name": "United States of America"
    }
  ],
  "release_date": "1999-10-12",
  "revenue": 100853753,
  "runtime": 139,
  "spoken_languages": [
    {
      "iso_639_1": "en",
      "name": "English"
    }
  ],
  "status": "Released",
  "tagline": "How much can you know about yourself if you've never been in a fight?",
  "title": "Fight Club",
  "video": false,
  "vote_average": 7.8,
  "vote_count": 3439
}

"""