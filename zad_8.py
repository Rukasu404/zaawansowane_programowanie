from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Any, Optional

import requests

API_URL = "https://api.openbrewerydb.org/v1/breweries"
BREWERIES_LIMIT = 20


def _to_float(value: Any) -> Optional[float]:
    """Zamienia wartość z API (zwykle string) na float; None jeśli brak/niepoprawna."""
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


@dataclass
class Brewery:
    """Browar - atrybuty odpowiadają polom zwracanym przez Open Brewery DB."""

    id: str
    name: str
    brewery_type: str
    address_1: Optional[str]
    address_2: Optional[str]
    address_3: Optional[str]
    city: str
    state_province: Optional[str]
    postal_code: Optional[str]
    country: str
    longitude: Optional[float]
    latitude: Optional[float]
    phone: Optional[str]
    website_url: Optional[str]
    state: Optional[str]
    street: Optional[str]

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Brewery:
        """Tworzy obiekt Brewery na podstawie słownika zwróconego przez API."""
        return cls(
            id=data["id"],
            name=data["name"],
            brewery_type=data.get("brewery_type", ""),
            address_1=data.get("address_1"),
            address_2=data.get("address_2"),
            address_3=data.get("address_3"),
            city=data.get("city", ""),
            state_province=data.get("state_province"),
            postal_code=data.get("postal_code"),
            country=data.get("country", ""),
            longitude=_to_float(data.get("longitude")),
            latitude=_to_float(data.get("latitude")),
            phone=data.get("phone"),
            website_url=data.get("website_url"),
            state=data.get("state"),
            street=data.get("street"),
        )

    def __str__(self) -> str:
        address_parts = [
            self.address_1,
            self.address_2,
            self.address_3,
            self.city,
            self.state_province,
            self.postal_code,
            self.country,
        ]
        address = ", ".join(part for part in address_parts if part)
        coordinates = (
            f"{self.latitude}, {self.longitude}"
            if self.latitude is not None and self.longitude is not None
            else "brak danych"
        )

        return (
            f"Browar: {self.name} (ID: {self.id})\n"
            f"  Typ:         {self.brewery_type}\n"
            f"  Adres:       {address or 'brak danych'}\n"
            f"  Współrzędne: {coordinates}\n"
            f"  Telefon:     {self.phone or 'brak danych'}\n"
            f"  Strona WWW:  {self.website_url or 'brak danych'}"
        )


def fetch_breweries(
    limit: int = BREWERIES_LIMIT, city: Optional[str] = None
) -> list[Brewery]:
    """Pobiera `limit` pierwszych browarów z API i zwraca listę obiektów Brewery.

    Jeśli podano `city`, wyniki są ograniczone do wskazanego miasta.
    """
    params: dict[str, Any] = {"per_page": limit}
    if city:
        # API oczekuje spacji zastąpionych podkreśleniami, np. "san_diego"
        params["by_city"] = city.strip().replace(" ", "_")

    response = requests.get(API_URL, params=params, timeout=10)
    response.raise_for_status()
    return [Brewery.from_dict(item) for item in response.json()[:limit]]


def parse_args() -> argparse.Namespace:
    """Wczytuje parametry przekazane w wierszu poleceń."""
    parser = argparse.ArgumentParser(
        description="Pobiera browary z Open Brewery DB i wyświetla je w konsoli."
    )
    parser.add_argument(
        "--city",
        type=str,
        default=None,
        help="ogranicza wyniki do wskazanego miasta, np. --city=Berlin "
        '(nazwy ze spacją w cudzysłowie: --city="San Diego")',
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    try:
        breweries = fetch_breweries(city=args.city)
    except requests.RequestException as error:
        print(f"Błąd podczas pobierania danych z API: {error}")
        return

    if not breweries:
        print(f"Nie znaleziono browarów dla miasta: {args.city}")
        return

    for brewery in breweries:
        print(brewery)
        print("-" * 60)


if __name__ == "__main__":
    main()

### python main.py --city=Berlin  przykladowo """