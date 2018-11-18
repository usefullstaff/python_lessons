import psycopg2
import json



"""
create user locator with password 'password';
create database obj_data owner locator;

grant all privileges on database obj_data to locator;

ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO locator;
GRANT USAGE ON SCHEMA public to locator;
GRANT SELECT ON ALL SEQUENCES IN SCHEMA public TO locator;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO locator;
ALTER ROLE locator WITH Superuser;

CREATE TABLE obj_locations( obj_name VARCHAR, obj_type VARCHAR, obj_lon numeric, obj_lat numeric, obj_osm_id bigint);
"""


DB ={'base_name': 'obj_data', 'user_name':'locator' , 'password':'password'}


select_obj_in_squad = """ 
SELECT * FROM obj_locations
WHERE obj_lat BETWEEN {:f} AND {:f}
AND obj_lon BETWEEN {:f} AND {:f};
"""


def fill_locations_table():
    psql_conn = psycopg2.connect(database = DB['base_name'], user = DB['user_name'], password = DB['password'], port = "5432")
    cur = psql_conn.cursor()

    data = json.load(open('json_coords.json', encoding="utf8"))
    coords_list = data['features']

    for geo_dict in coords_list:
        obj_name = geo_dict['properties']['name']
        obj_type = geo_dict['properties']['podclass_r']
        obj_lon = geo_dict['geometry']['coordinates'][1]
        obj_lat = geo_dict['geometry']['coordinates'][0]
        obj_osm_id = geo_dict['properties']['osm_id']

        insert_location = "INSERT INTO obj_locations VALUES ({},{},{},{},{})".format ("'"+obj_name.replace("'", "")+"'", "'"+obj_type+"'", obj_lat, obj_lon, obj_osm_id )
        cur.execute(insert_location)         

    psql_conn.commit()
    psql_conn.close()


fill_locations_table()    


