import sys

sys.path.append("..")
from app.functions import whatsapp_send_message


def test_whatsapp_send_message():
    assert whatsapp_send_message.send_message("Niaje", 254714308029) == True
