import serial
from datetime import date

from time import sleep

NUM_SENSORS = 4
SEPARATOR_CHARACTER = "|"


def leer_arduino():
    arduino = serial.Serial('/dev/ttyACM0', 9600)
    arduino.setDTR(False)
    sleep(1)
    arduino.flushInput()
    arduino.setDTR(True)
    try:
        while True:
            lineBytes = arduino.readline()
            linea = lineBytes.decode('utf-8').strip()
            linea = line_to_str(linea)
            to_csv_line(linea)
    except keyboardInterrupt:
        arduino.close()
        exit()


def line_to_str(line):
    line = line.replace(" ", "")
    line = line.strip('\n')
    str_line = ""
    sensors_info = line.split(SEPARATOR_CHARACTER, NUM_SENSORS)
    if len(sensors_info) == NUM_SENSORS:
        sensors_info.append(str(date.today()))
        y_field = input('A que elemento pertenece? ')
        sensors_info.append(y_field)
        str_line = ';'.join(map(str, sensors_info))
    return str_line


def to_csv_line(data):
    with open('data/salida.csv', "a") as f:
        f.write('\n')
        f.write(data)


def leer_dato():
    dato = []
    with open("./data/entrada.txt","r") as f:
        for linea in f:
            linea = line_to_str(linea)
            to_csv_line(linea)
        return dato


if __name__ == "__main__":
    # para leer datos del archivo uso la funcion leer_dato()
    # para leer datos del arduino usar la funcion leer_arduino()
    leer_dato()
