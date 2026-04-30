"""Shannon Airport (SNN) destinations — April 2026."""

DESTINATIONS = {
    "SNN": {
        "name": "Shannon",
        "routes": {
            # UK
            "BHX": "Birmingham",
            "EDI": "Edinburgh",
            "LPL": "Liverpool",
            "LTN": "London Luton",
            "MAN": "Manchester",
            # Spain (Mainland)
            "AGP": "Malaga",
            "ALC": "Alicante",
            "MAD": "Madrid",
            # Spain (Barcelona region)
            "GRO": "Barcelona Girona",
            "REU": "Barcelona Reus",
            # Balearic Islands
            "PMI": "Palma de Mallorca",
            # Canary Islands
            "ACE": "Lanzarote",
            "FUE": "Fuerteventura",
            "LPA": "Gran Canaria",
            "TFS": "Tenerife South",
            # Italy
            "FCO": "Rome Fiumicino",
            "NAP": "Naples",
            "TRN": "Turin",
            # France
            "BZR": "Beziers",
            "CDG": "Paris Charles de Gaulle",
            # Portugal
            "FAO": "Faro",
            "FNC": "Funchal (Madeira)",
            "OPO": "Porto",
            # Germany
            "FRA": "Frankfurt",
            # Greece
            "CFU": "Corfu",
            # Poland
            "KRK": "Krakow",
            "POZ": "Poznan",
            "WAW": "Warsaw",
            "WRO": "Wroclaw",
            # Hungary
            "BUD": "Budapest",
            # Lithuania
            "KUN": "Kaunas",
            # Finland
            "RVN": "Rovaniemi (Lapland)",
            # Malta
            "MLA": "Malta",
            # North America
            "BOS": "Boston",
            "JFK": "New York JFK",
            "ORD": "Chicago O'Hare",
        },
    },
}


def get_destinations(airport: str) -> dict:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("routes", {})


def get_airport_name(airport: str) -> str:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("name", airport)
