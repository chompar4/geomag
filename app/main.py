import datetime
from json import dumps

from flask import Flask, request
from flask_cors import CORS
from flask_restful import Api, Resource, abort
from webargs import fields, validate
from webargs.flaskparser import parser, use_kwargs

from geomag import field as calculate_field

app = Flask(__name__)
CORS(app)
api = Api(app)

class GeomagField(Resource):

    schema_args = {
        "lat": fields.Float(required=True, validate=lambda dLat: -90 <= dLat <= 180), # accepts normalised [-90, 90] or unormalised [0, 180]
        "lng": fields.Float(required=True, validate=lambda dLng: -180 <= dLng <= 360), # accepts normalised [-180, 180] or unormalised [0, 360]
        "altitude_km": fields.Float(required=True, validate=lambda km: -1 < km <= 850),
        "yr": fields.Integer(required=True, validate=lambda y: 2020 <= y < 2025),
        "mth": fields.Integer(required=True, validate=lambda m: 1 <= m <= 12),
        "day": fields.Integer(required=True, validate=lambda d: 1 <= d < 31)
    }

    @use_kwargs(schema_args)
    def get(self, lat, lng, altitude_km, yr, mth, day):
        result = calculate_field(lat, lng, altitude_km, datetime.date(yr, mth, day))
        return result
        
api.add_resource(GeomagField, '/')

@parser.error_handler
def handle_request_parsing_error(err, req, schema, *, error_status_code, error_headers):
    abort(error_status_code, errors=err.messages)

if __name__ == '__main__':
     app.run(port='5002', debug=True)
