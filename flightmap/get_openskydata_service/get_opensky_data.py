from flightmap.http_client.http_client import get
from django.conf import settings


def get_data():
    data = get(settings.OPENSKY_URL)
    geojson_dict = {
        "type": "FeatureCollection",
        "features": [
        ]
    }
    for state in data['states']:
        geojson_dict['features'].append({
            "type": "Feature",
            "id": state[1],
            "properties": {
                "name": state[1],
                "velocity": str(round(state[9] * 3.6, 1)) + ' km/h',
                "altitude": str(round(state[7], 1)) + ' m'
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    state[5],
                    state[6]
                ]
            }
        })

    return geojson_dict
