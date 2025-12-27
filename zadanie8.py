import requests
import argparse
from typing import Optional
class Brewery:
    def __init__(
        self,
        id:str,
        name:str,
        brewery_type:str, 
        street:Optional[str],
        city:Optional[str],
        state:Optional[str],
        postal_code:Optional[str],
        country:Optional[str], 
        longitude:Optional[str],
        latitude:Optional[str],
        phone:Optional[str],
        website_url:Optional[str],
    ):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.city = city
        self.state = state 
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url
    def __str__(self):
        return (
            f"Brewery{self.name} (ID:{self.id})\n"
            f"Type: {self.brewery_type}\n"
            f"Address: {self.street}, {self.city}, {self.state}, {self.postal_code}\n"
            f"Coordinates: ({self.latitude}, {self.longitude})\n"
            f"Phone: {self.phone}\n"
            f"Website: {self.website_url}\n"
        )
def main():
    parser = argparse.ArgumentParser(description="Fetch breweries from Open Brewery"
    )
    parser.add_argument(
        "--city",
        type=str,
        help="Filter breweries by city name (e.g., Berlin)",
    )
    args = parser.parse_args()
    url = "https://api.openbrewerydb.org/breweries"
    params = {"per_page":20}
    if args.city:
        params["by_city"] = args.city
    response = requests.get(url, params=params)
    breweries_data = response.json()
    breweries = [
        Brewery(
            id=b.get("id"),
            name=b.get("name"),
            brewery_type=b.get("brewery_type"),
            street=b.get("street"),
            city=b.get("city"),
            state=b.get("state"),
            postal_code=b.get("postal_code"),
            country=b.get("country"),
            longitude=b.get("longitude"),
            latitude=b.get("latitude"),
            phone=b.get("phone"),
            website_url=b.get("website_url")
        )
        for b in breweries_data
    ]
    for brewery in breweries:
        print (brewery)
if __name__=="__main__":
    main()



