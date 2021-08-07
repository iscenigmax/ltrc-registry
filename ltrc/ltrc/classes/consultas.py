#!/usr/bin/python
# -*- encoding: utf-8 -*-
import csv
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
__author__ = 'csanchez'
__date__ = '2019/01/20 22:28'


def enviar_notificacion():
	with open('C:\\Users\\SLAMNET\\Dropbox\\runner\\THE END IV\\sinentregar.csv', 'r', encoding='utf8') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			msg = MIMEMultipart('alternative')
			msg['Subject'] = "THEN END IV - playera (recuperar)"
			msg['From'] = "info@icons.com"
			msg['To'] = row['correo']

			text = """Buen día {} esperemos que estés muy bien y entrenando inteligentemente para tus proyectos
			venideros; vemos que NO recogiste tu KIT de THE END IV y lamentamos saberlo, pero antes de destruir tu
			playera tienes una oportunidad de recuperarla en caso de quererla.\n\nSi es así recuerda el costo es de $150
			MXN y solo estará disponible hasta el 24 de febrero del 2019, solo confírmanos por este medio o bien en la
			página de LA TRIBU RUNNING CLUB.\n\nGracias y que tengas un excelente 2019…""".format(row['nombre'])

			html = """
			<html>
			  <head></head>
			  <body>
			    <p>Buen día {} esperemos que estés muy bien y entrenando inteligentemente para tus proyectos venideros;
			    vemos que NO recogiste tu KIT de THE END IV y lamentamos saberlo, pero antes de destruir tu playera
			    tienes una oportunidad de recuperarla en caso de quererla.</p>
				<p>Si es así recuerda el costo es de $150 MXN y solo estará disponible hasta el 24 de febrero del 2019,
				solo confírmanos por este medio o bien en la página de LA TRIBU RUNNING CLUB.</p>
				<p>Gracias y que tengas un excelente 2019...</p>
			  </body>
			</html>
			""".format(row['nombre'])

			try:
				# msg.attach(MIMEText(text, 'plain'))
				# msg.attach(MIMEText(html, 'html'))
				# mail = smtplib.SMTP('smtp.gmail.com', 587)
				# mail.ehlo()
				# mail.starttls()
				# mail.login('ing.casr@gmail.com', 'iscenigmax1982.')
				# mail.sendmail(msg['From'], msg['To'], msg.as_string())
				# mail.quit()
				print('		OK-SEND: {} - {}'.format(row['nombre'], row['correo']))
			except Exception as e:
				print('			ERROR-SEND: {}'.format(str(e)))
				pass


if __name__ == "__main__":
	tiempo_inicial = datetime.now()
	print ('inicia envio...')
	print()
	try:
		enviar_notificacion()
	except Exception as e:
		print('ERROR: {}'.format(str(e)))
	finally:
		tiempo_final = datetime.now()
		tiempo_ejecucion = (tiempo_final - tiempo_inicial)
		print()
		print('finaliza envio {}...'.format(tiempo_ejecucion))
