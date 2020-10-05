from flask import current_app
from pprint import pprint


def load_data(airport_db_obj):
    """ Load user's data

    Parameters:
    - Airport db object
    """
    from app.models.schemas import AirportSchema

    airport_schema = AirportSchema()

    data = airport_schema.dump(airport_db_obj)

    return data

def serialize_file_data(filename):
    """ Converts all file data to a serialized structure """
    import csv

    output = []

    with open(filename, newline='', encoding='utf-8') as csv_file: 
        reader = list(csv.reader(csv_file))
        columns = reader[0]

        for row in reader[1:]:
            output.append({
                field.lower(): (value if value != '' else None) 
                                for (field, value) in zip(columns, row) 
            })

    csv_file.close()

    return output
