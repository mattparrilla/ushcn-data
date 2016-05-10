from flask import Flask, make_response
from flask_restful import Resource, Api
import sqlite3

import json

app = Flask(__name__)
api = Api(app)


@api.representation('application/json')
def output_json(data, code, headers=None):
    resp = make_response(json.dumps(data, code))
    resp.headers.extend(headers or {})
    return resp


# /readingsByStation/:station_id
class ReadingsByStation(Resource):
    def get(self, station_id):
        conn = sqlite3.connect('../ushcn.db')
        c = conn.cursor()
        responseDict = {}
        for row in c.execute('SELECT * FROM reading WHERE station_id = %s' % station_id):
            id, value, metric, m_flag, q_flag, s_flag, date, station_id = row
            reading = {
                'value': value,
                'mFlag': m_flag,
                'qFlag': q_flag,
                'sFlag': s_flag,
                'date': date
            }
            if metric in responseDict:
                responseDict[metric].append(reading)
            else:
                responseDict[metric] = [reading]

        conn.close()
        return responseDict

api.add_resource(ReadingsByStation, '/readings-by-station/<string:station_id>')

if __name__ == '__main__':
    app.run(debug=True)
