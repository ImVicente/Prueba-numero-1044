#Procedimiento para elegir la opcion con la que se jugara
def elegir_opcion():
  accion_usuario = input("Ingresa una opción: (piedra, papel, tijera):")
  accion_computadora=eleccion_computadora()
  comparacion_resultados(accion_usuario,accion_computadora)


import random

#Funcion (ya que esta si retorna algo) para saber la opcion del computador
def eleccion_computadora():
  accion_computadora = random.choice(acciones_posibles)
  return accion_computadora
#Procedimiento para saber el ganador
def ganador(accion_usuario,accion_computadora):
  
  if accion_usuario=="piedra":
    if accion_computadora=="piedra":
      print("Es un empate")
      contador(accion_usuario,accion_computadora)
    if accion_computadora =="papel":
      print("La computadora ha ganado")
      contador(accion_usuario,accion_computadora)
    if accion_computadora=="tijera":
      print("Usted ha ganado")
      contador(accion_usuario,accion_computadora)

  if accion_usuario=="papel":
    if accion_computadora=="papel":
      print("Es un empate")
      contador(accion_usuario,accion_computadora)
    if accion_computadora =="tijera":
      print("La computadora ha ganado")
      contador(accion_usuario,accion_computadora)
    if accion_computadora=="piedra":
      print("Usted ha ganado")
      contador(accion_usuario,accion_computadora)

  if accion_usuario=="tijera":
    if accion_computadora=="tijera":
      print("Es un empate")
      contador(accion_usuario,accion_computadora)
    if accion_computadora =="piedra":
      print("La computadora ha ganado")
      contador(accion_usuario,accion_computadora)
    if accion_computadora=="papel":
      print("Usted ha ganado")
      contador(accion_usuario,accion_computadora)
#Procedimiento que inicia el juego
def iniciar_juego():
  elegir_opcion()
