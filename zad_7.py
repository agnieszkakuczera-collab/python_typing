import requests
from typing import Optional
class Brewery:
    def __init__(
        self,
        id: str,
        name: str,
        brewery_type: str,
        street: Optional[str],
        city: Optional[str],
        state: Optional[str],
        postal_code: Optional[str],
        country: Optional[str],
        longitude: Optional[str],
        latitude: Optional[str],
        phone: Optional[str],
        website_url: Optional[str]
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
            f"Brewery {self.name} (ID: {self.id})\n"
            f"Type: {self.brewery_type}\n"
            f"Address: {self.street}, {self.city}, {self.state}, {self.postal_code}, {self.country}\n"
            f"Coordinates: ({self.latitude}, {self.longitude})\n"
            f"Phone: {self.phone}\n"
            f"Website: {self.website_url}\n"
        )
def main():
    response = requests.get(
        "https://api.openbrewerydb.org/v1/breweries",
        params={"per_page": 20}
    )
    response.raise_for_status()
    breweries_data = response.json()
    breweries_lists = [
        Brewery(
            id=brewery.get("id"),
            name=brewery.get("name"),
            brewery_type=brewery.get("brewery_type"),
            street=brewery.get("street"),
            city=brewery.get("city"),
            state=brewery.get("state"),
            postal_code=brewery.get("postal_code"),
            country=brewery.get("country"),
            longitude=brewery.get("longitude"),
            latitude=brewery.get("latitude"),
            phone=brewery.get("phone"),
            website_url=brewery.get("website_url"),
        )
        for brewery in breweries_data
    ]
    for brewery in breweries_lists:
        print(brewery)
if __name__ == "__main__":
    main()
