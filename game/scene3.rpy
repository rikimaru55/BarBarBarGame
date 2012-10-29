#Images
image bg DirTecnicaScene="DirTecnicaScene.png"
image bg RRHHScene="RRHHScene.png"
image bg CompaneroScene="CompaneroScene.png"
image alaric = Image("Alaric.png", yalign=0.25, xalign=0.0)
image dirTecnica = Image("DirTecnica.png", yalign=0.30,xalign=0.0)
image RRHH = Image("RRHH.png", yalign=0.40,xalign=0.0)
image companero = Image("Companero.png",yalign=0.30,xalign=0.0)
#Characters
define al = Character('Alaric Chan', color="#D47113")
define dt = Character('Directora Tecnica', color="#856E48")
define rh = Character('Directora Recursos Humanos' , color="#07B84D")
define ce = Character('Miembro del equipo', color="#1EDBD6")
# The scene starts here.
label scene3Start:
    show bg myoffice
    with dissolve
    "*En mi oficina*"
    #Sonido de puerta 
    "*Entra Alaric, tu consultor coreano*"
    show alaric
    with dissolve
    al "--En un ingles algo quebrado, Alaric hace su informe de progreso para el dia--"
    me "Gracias Alaric, me parece bien el progreso."
    "Alaric hace una pequena reverencia y sale de la habitacion."
    hide alaric
    with fade
    me "Wow, aunque cada dia entiendo un poco mas, de verdad me es dificil entender ese ingles que usa."
    me "Bueno, al menos en la empresa manejar un nivel basico de ingles es un requisito."
    me "Aunque pensandolo bien, he notado que a varios companeros del equipo les cuesta entender lo que Alaric dice,espero que no este afectando su desempeno."
    me "Hmmm, deberia investigar eso."
    "Revisando tus reportes te das cuenta que aunque el desempeno de Alaric es muy bueno, el desempeno de otros companeros(especificamente los que mas cerca trabajan con Alaric) ha descendido."
    me "Parece que esto es serio, deberia tomar una decision, aunque talvez investigar un poco mas no vendria mal"
    
menu:
    "Debo ser decisivo .Voy a tomar una decision inmediatamente!":
        jump scene3Decision
    "Hmmm, no debo saltar a conclusiones, voy a investigar un poco mas.":
        jump scene3Choice

label scene3Decision:
    me "Ok, hora de tomar la decision final. Cual sera la correcta?"

menu:
    "La barrera del lenguaje es demasiado grande, debere pedir su transferencia":
        $ alaric_fired = True
        jump final
    "Alaric es un recurso demasiado valioso y estoy seguro que puedo encontrar una mejor solucion.":
        $ alaric_fired = False
        jump final

label scene3Choice:
    me "Me pregunto a quien puedo visitar para entender mejor la situacion."
menu:
    "Coordinadora Tecnica":
        jump scene3Coord
    "Jefa de Recursos Humanos":
        jump scene3RRHH
    "Companero de equipo":
        jump scene3Comp
    "Tengo toda la informacion que necesito":
        jump scene3Decision

########################
# Coordinadora Tecnica #
########################
label scene3Coord:
    show bg DirTecnicaScene
    show dirTecnica
    with dissolve
    me "Hola, todo bien?"
    dt "Todo bien, estoy terminando mi informe"
    me "Oye, queria hacerte una pregunta."
    dt "Que paso?"
    me "Que te ha parecido el trabajo de Alaric? Es bueno? Haz tenido algun problema con el?"
    dt "Pues si, su ingles no es muy bueno y a veces me cuesta entenderle. No me quedan claras sus soluciones cuando me las explica."
    dt "Pero... Cuando ya las implementa si las entiendo y siempre son excelentes. Su nivel tecnico es asombroso, he aprendido mas leyendo sus comentarios que en algunos cursos de la carrera."
    me "Hmmm, entonces estas contenta de trabajar con el?"
    dt "Claro que si, gracias a el, nuestras metas tecnicas han avanzado impresionantemente. Aunque lo del lenguaje es molesto de vez en cuando, se empalidece al compararlo con los logros tecnicos."
    me "Me alegra oir eso, gracias!"
    dt "No hay problema, te dejo que tengo que terminar mi informe."
    hide dirTecnica
    with dissolve
    jump scene3Choice
########################
# Coordinadora RRHH    #
########################
label scene3RRHH:
    show bg RRHHScene
    show RRHH
    with dissolve
    me "Perdona, tienes un momento?"
    rh "Por supuesto, dime"
    me "La gente te tiene mucha confianza y a veces te dicen cosas que no se atreven a decirle a sus supervisores."
    rh "Asi es, a veces la gente se siente mas comoda conversando con un tercero."
    me "Queria saber, si no te incomoda, si has recibido algun comentario sobre mala comunicacion en mi proyecto?"
    rh "Esto es sobre Alaric me imagino?"
    me "Ok, lo admito, eres muy buena. Como supiste?"
    rh "Facil, si he estado recibiendo comentarios sobre comunicacion con respecto a Alaric"
    me "Y? Son positivos?"
    rh "La mayoria al menos, casi todos son sobre como deberiamos dar capacitacion para mejorar el nivel de ingles de la gente."
    rh "Mi impresion es que la gente siente curiosidad por las excelentes habilidades de Alaric y les gustaria poder conversar mas con el."
    me "Dijiste que la mayoria. Hay comentarios negativos?"
    rh "Si, pocos pero bastante vocales, algunos miembros sienten que es responsabilidad de Alaric conocer el idioma del lugar donde viene a trabajar."
    rh "Y que su falta de capacidad para comunicarse afecta fuertemente el desempeno del proyecto."
    me "Esas son observaciones algo severas."
    me "Bueno, te agradezco la informacion."
    rh "Estoy para servir. Bueno, tengo que irme, fallaron las negociaciones de un proyecto en Inglaterra y ahora tenemos varios recursos listos para trabajar, pero sin nada que hacer."
    hide RRHH
    with dissolve
    jump scene3Choice

########################
# Companero Equipo     #
########################
label scene3Comp:
    show bg CompaneroScene
    show companero
    with dissolve
    me "Hola! Crees que podriamos hablar un momento?"
    ce "Ando algo ajetreado, pero si claro, podemos hablar."
    me "Queria pedir tu opinion sobre un tema algo sensible."
    ce "Ok, que podria ser?"
    hide companero
    with dissolve
    jump scene3Choice
    return