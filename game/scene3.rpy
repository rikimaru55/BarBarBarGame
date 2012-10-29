define al = Character('Alaric Chan', color="#D47113")
# The scene starts here.
label scene3Start:

    "*En mi oficina*"
    #Sonido de puerta 
    "*Entra Alaric, tu consultor coreano*"
    al "--En un ingles algo quebrado, Alaric hace su informe de progreso para el dia--"
    me "Gracias Alaric, me parece bien el progreso."
    "Alaric hace una pequena reverencia y sale de la habitacion."
    me "Wow, aunque cada dia entiendo un poco mas, de verdad me es dificil entender ese ingles que usa."
    me "Bueno, al menos en la empresa manejar un nivel basico de ingles es un requisito."
    me "Aunque pensandolo bien, he notado que a varios companeros del equipo les cuesta entender lo que Alaric dice,espero que no este afectando su desempeno."
    me "Hmmm, voy a revisar eso"
    "Revisando tus reportes te das cuenta que aunque el desempeno de Alaric es muy bueno, el desempeno de otros companeros(especificamente los que mas cerca trabajan con Alaric) ha descendido."
    me "Parece que esto es serio, deberia tomar una decision, aunque talvez investigar un poco mas no vendria mal"
    
menu:
    "Debo ser decisivo .Voy a tomar una decision inmediatamente!":
        jump scene3Decision
    "Hmmm, no debo saltar a conclusiones, voy a investigar un poco mas":
        jump scene3Choice

label scene3Decision:
    me "Ok, hora de tomar la decision final. Cual sera la correcta?"

menu:
    "La barrera del lenguaje es demasiado grande, debere pedir su transferencia":
        $ alaric_fired = True
        jump final
    "Alaric es un recurso demasiado valioso y estoy seguro que puedo encontrar una mejor solucion":
        $ alaric_fired = False
        jump final

label scene3Choice:
    me "Me pregunto a quien puedo visitar para entender mejor la situacion"
menu:
    "Coordinadora Tecnica":
        jump scene3Coord
    "Jefa de Recursos Humanos":
        jump scene3RRHH
    "Companero de equipo":
        jump scene3Comp
    "Tengo toda la informacion que necesito":
        jump scene3Decision

label scene3Coord:
    "Entro a la oficina de la Coordinadora Tecnica"
    jump scene3Choice
label scene3RRHH:
    "Entro a la oficina de Recursos Humanos"
    jump scene3Choice
    
label scene3Comp:
    "Entro a la oficina de Companero de equipo"
    jump scene3Choice
    return