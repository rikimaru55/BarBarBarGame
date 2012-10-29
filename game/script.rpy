# You can place the script of your game in this file.
# base color EB6621
# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define me = Character('Yo', color="#EB6621")
define al = Character('Alaric Chan', color="#D47113")

# The game starts here.
label start:
    
    "Welcome/Bienvenido/Wielkomen a BarBarBar, un juego sobre como las diferencias culturales pueden afectar nuestro trabajo"
    "Más especificamente un proyecto...{p=1.0}.{p=1.0}.{p=1.0}.o más bien SU proyecto"
    "¡Felicitaciones, ha sido ascendido!"
    #Insertar musica feliz aqui(Standing Ovation/Oscars)
    "Usted es un nuevo director de proyecto que fue asignado a un equipo multicultural hace poco"
    "Ya lleva unos meses trabajando con su equipo, superando retos y tomando acciones"
    "Hoy es un día como cualquier otro{p=2.0}...¿verdad?"
    
    #Cambiamos al frente de la oficina
    me "Bueno... Otro día otra tarea!"

    jump scene3Start
    

label final:
    if alaric_fired:
        "Despedirlo fue un error"
    else:
        "No despedirlo fue un acierto"
    return