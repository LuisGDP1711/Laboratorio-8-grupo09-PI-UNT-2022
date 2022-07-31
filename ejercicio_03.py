import os
import locale
from datetime import datetime, timedelta
from win10toast import ToastNotifier

locale.setlocale(locale.LC_ALL, 'es-ES')

fecha_actual = datetime.now()
# print(fecha_actual.strftime("%A %d de %B del %Y - %H:%M"))
hora_escogida = int(input("Indique la hora en la que quiere ser alertado: "))
minuto_escogido = int(input("Indique el mminuto en el que quiere ser alertado: "))
fecha_escogida = datetime(fecha_actual.year, fecha_actual.month, fecha_actual.day, hora_escogida, minuto_escogido)
# print(fecha_escogida.strftime("%A %d de %B del %Y - %H:%M"))

t = timedelta(minutes=5)
fecha_notificacion = fecha_escogida - t
# print(fecha_notificacion.strftime("%A %d de %B del %Y - %H:%M"))


def notificacion():
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    toast = ToastNotifier()
    titulo = "¡ALERTA!"
    mensaje = f"Faltan 5 minutos para que sean las {fecha_escogida.hour}:{fecha_escogida.minute}"
    time = 30
    icon = None

    toast.show_toast(titulo, mensaje, icon_path=icon, duration=time, threaded=True)


while f"{fecha_actual.hour}:{fecha_actual.minute}" != f"{fecha_notificacion.hour}:{fecha_notificacion.minute}":
    fecha_actual = datetime.now()
else:
    notificacion()