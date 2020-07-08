import uuid
from rentomatic.domain import room as r

def test_room_model_init():
    """Tests if the model inits with the data inserted"""
    code = uuid.uuid4()
    room = r.Room(code, size=200, price=10,
                  longitude=-0.09998975,
                  latitude=51.75436293)
    assert room.code == code
    assert room.size == 200
    assert room.price == 10
    assert room.longitude == -0.09998975
    assert room.latitude == 51.75436293

def test_room_model_from_dict():
    """Tests if the model initialize from a dict"""
    code = uuid.uuid4()
    room = r.Room.from_dict(
        {
            'code': code,
            'size': 200,
            'price': 10,
            'longitude': -0.09998975,
            'latitude': 51.75436293
        }
    )
    assert room.code == code
    assert room.size == 200
    assert room.price == 10
    assert room.longitude == -0.09998975
    assert room.latitude == 51.75436293

def test_room_model_to_dict():
    """
    Tests if the object initialized by a dict store the data corerctly
    and produces the same json
    """
    room_dict = {
        'code': uuid.uuid4(),
        'size': 200,
        'price': 10,
        'longitude': -0.09998975,
        'latitude': 51.75436293
    }

    room = r.Room.from_dict(room_dict)

    assert room.to_dict() == room_dict

def test_room_model_comparison():
    room_dict = {
        'code': uuid.uuid4(),
        'size': 200,
        'price': 10,
        'longitude': -0.09998975,
        'latitude': 51.75436293
    }
    room1 = r.Room.from_dict(room_dict)
    room2 = r.Room.from_dict(room_dict)

    assert room1 == room2
