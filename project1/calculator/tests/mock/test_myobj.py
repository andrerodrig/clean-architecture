from unittest import mock
from mock import myobj as m

def test_setup():
    external_obj = mock.Mock()
    obj = m.MyObj(external_obj)
    obj.setup()
    external_obj.setup.assert_called_with(cache=True, max_connections=256)
