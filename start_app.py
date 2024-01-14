#!/usr/bin/env python3
import subprocess
import time

# Comando 1: RabbitMQ
subprocess.Popen(['sudo', 'docker', 'run', '-it', '--rm', '--name', 'rabbitmq', '-p', '5672:5672', '-p', '15672:15672', 'rabbitmq:management-alpine'])

# Esperar unos segundos para asegurarse de que RabbitMQ está en funcionamiento antes de ejecutar el siguiente comando
time.sleep(5)

# Comando 2: Celery
subprocess.Popen(['celery', '-A', 'PracticaDjango', 'worker', '-l', 'info'])

# Comando 3: Stripe CLI
subprocess.Popen(['sudo', 'docker', 'run', '--network=host', '-it', '--rm', '-v', 'stripe_config:/root', 'stripe/stripe-cli', 'listen', '--forward-to', 'localhost:8000/payment/webhook/'])

# Comando 4: Django Server
subprocess.Popen(['python', 'manage.py', 'runserver'])


# Este script abrirá un nuevo terminal para cada uno de los comandos, 
# lo que permitirá que se ejecuten en paralelo. Ten en cuenta que el comando gnome-terminal 
# es específico de entornos GNOME. Si estás utilizando un entorno diferente, 
# puedes ajustar el comando según sea necesario, si se quiere todo en un terminal
# solo, puedes ejecutar los comandos uno a uno quitando 'gnome-terminal' '--'
