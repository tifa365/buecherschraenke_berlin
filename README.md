# Berlin Öffentliche Bücherschränke

Scraper for public bookshelves (öffentliche Bücherschränke) in Berlin.

## Data Source

- **URL**: https://www.berlin.de/special/sharing/oeffentliche-buecherschraenke/
- **API**: https://www.berlin.de/special/sharing/oeffentliche-buecherschraenke/rubric.geojson
- **Format**: GeoJSON
- **Count**: ~57 public bookshelves across Berlin
- **Last downloaded**: 08. November 2025

## Usage

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the scraper:
```bash
python3 scraper.py
```

This will fetch the latest data and save it to `buecherschraenke_berlin.json`.

## API Documentation

See `openapi.yaml` for the complete API specification.

## Data Structure

Each bookshelf feature includes:
- **Location**: Coordinates (longitude, latitude)
- **Title**: Name of the bookshelf
- **Address**: Street address
- **Description**: Information about the bookshelf
- **URL**: Link to detailed page on berlin.de
- **Modified**: Last update timestamp

## Example

```json
{
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": [13.4533, 52.5926]
  },
  "properties": {
    "title": "Blankenburger Bücherbox",
    "address": "Alt-Blankenburg 16, Berlin, 13129",
    "description": "Gut besucht und gut gepflegt...",
    "url": "https://www.berlin.de/..."
  }
}
```
