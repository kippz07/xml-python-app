import xml.etree.ElementTree as ET
tree = ET.parse('mini-schema.xml')
root = tree.getroot()

from bottle import Bottle, run
app = Bottle()

def get_notes(device):
    for d in root.iter('device'):
        name = d.find('name').text
        if name == device:
            return (d.find('notes').text)

def get_all():
    array = []
    for d in root.iter('device'):
        name = d.find('name').text
        array.append(name)
    return array



@app.route('/')
def home():
    return "<h1>Input a device name in the url</h1>"

@app.route('/all')
def all():
    devices = get_all()
    return (f"<p>{devices}</p>")


@app.route('/<device>')
def get_device_notes(device):
    notes = get_notes(device)
    return (f"<h1>{notes}</h1>")

run(app, host='localhost', port=3000)




