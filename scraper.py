#!/usr/bin/env python3
"""
Scraper for Berlin public bookshelves (Öffentliche Bücherschränke)
Source: https://www.berlin.de/special/sharing/oeffentliche-buecherschraenke/
"""

import json
import requests


def fetch_buecherschraenke():
    """Fetch public bookshelf data from Berlin.de"""

    url = 'https://www.berlin.de/special/sharing/oeffentliche-buecherschraenke/rubric.geojson'

    headers = {
        'sec-ch-ua-platform': '"Linux"',
        'Referer': 'https://www.berlin.de/special/sharing/oeffentliche-buecherschraenke/',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
        'DNT': '1',
        'sec-ch-ua-mobile': '?0'
    }

    params = {
        '_rnd': '489609'
    }

    print("Fetching data from Berlin.de...")
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    data = response.json()

    # Save to file
    output_file = 'buecherschraenke_berlin.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✓ Data saved to {output_file}")
    print(f"✓ Found {len(data.get('features', []))} public bookshelves")

    return data


if __name__ == '__main__':
    fetch_buecherschraenke()
