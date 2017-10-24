import RPi.GPIO as GPIO #tutti i comandi si rifanno alla libreria da noi impostata, in questo caso GPIO#
import time #importiamo una nuova libreria che si riferisce al tempo#
GPIO.setmode(GPIO.BCM) #senti, noi parliamo in BCM, capisc a me#
GPIO.setwarnings(False) #non mi stampare/scrivere gli errori#
GPIO.setup(18,GPIO.OUT) #il pin 18 sarà il nostro OUTPUT#
print "LED on" #ci comunica l'accensione del led#
GPIO.output(18,GPIO.HIGH) #accende il led#
time.sleep(1) #tempo di pausa che si prende il led#
print "LED off" #ci comunica che il led è spento#
GPIO.output(18,GPIO.LOW) #interruzione della corrente al led#
