import requests
import json

def process_json(fname):
    f = open(fname, 'r')
    sens = json.load(f) #Rückgabewert ist hier eine (assoziative) Liste

    pretty = json.dumps(sens, indent=4, sort_keys=True) #Achtung: Rückgabewert ist ein String
    print(pretty)

    first = sens[0] #Hole den ersten Eintrag aus der Liste
    print(first)

    #Auslesen aller Namen
    for s in sens:
        print(s['key'])

    #Auslesen aller Sensortypen
    for s in sens:
        entries = s['sensor']['array']
        for entry in entries:
            if 'type' in entry: #So überprüft man ob es einen Eintrag gibt (allgemein, ob ein key in einem Dictionary vorhanden ist
                print(entry['type'])


    f.close()

    with open('%s.first' % fname, 'w') as outfile:
        json.dump(first, outfile)


if __name__ == '__main__':
    process_json('/home/albert/tmp/sensor.json')