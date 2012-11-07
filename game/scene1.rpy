#Images
image bg MalaysiaScene="MalaysiaScene.png"
image bg ShipScene="ShipScene.png"
image capitan = Image("Capitan.png", yalign=0.15, xalign=0.0)
image hamzah = Image("Hamzah.png", yalign=0.25,xalign=0.0)
image manufactura = Image("Manufactura.png", yalign=0.25,xalign=0.0)
image proveeduria = Image("Proveeduria.png",yalign=0.25,xalign=0.6)
#Characters
define cap = Character('Capitan', color="#AB1A25")
define lh = Character('Lat Hamzah', color="#CC573F")
define sm = Character('Supervisor Manufactura' , color="#D97925")
define sp = Character('Supervisor Proveeduria', color="#EFE7BE")
# The scene starts here.
label scene1Start:
    #Variables
    $ dock_bad = False
    $ dock_good = False
    $ call_hamzah = False
    $ force_shipment = False
    show bg myoffice
    with fade
    "*Entro a mi oficina*"
    #TODO Sonido de Puerta
    "*Entra a mi oficina el supervisor de proveeduria*"
    show proveeduria
    with dissolve
    "*Detras de el entra el supervisor de manufactura*"
    show manufactura
    with dissolve
    sm "Buenos dias, perdona que no te demos tiempo para acomodarte, pero tenemos un serio problema..."
    sm "Veras..."
    "*El supervisor de proveeduria no lo deja terminar su oracion*"
    sp "*Casi histerico* Los componentes que debian llegar hoy aun estan en el muelle!!!"
    sp "Es un *@!&$ desastre!"
    sp "No sabemos que hacer!"
    sm "*Algo frustrado* Y como comprenderas eso atrasa las pruebas de produccion que debian empezar hoy"
    me "Ok, ya veo. Ya llamaron al muelle para saber que paso?"
    sm "Si, ya llamamos, nuestro encargado en el muelle nos dijo que el barco llego antiayer, con bastante tiempo y que simplemente el dia del desembarco no hicieron nada."
    sm "Cuando nuestro encargado le pregunto al capitan porque no movian el cargamento..."
    sp "DIJO QUE HOY NO LO IBAN A HACER! Puedes creer la cascara de esa gente?!?"
    sm "...basicamente... O al menos eso entendio el encargado, el capitan no habla ingles"
    me "Ya veo y ya llamaron a Lat Hamzah en Malasia? El es nuestro contacto con la empresa que provee esos componentes."
    sm "Preferimos hablar contigo primero, ver que te parecia mejor."
    sp "Igual, nada te puede decir el que ya no sepamos."
    sp "Las buenas noticias es que uno de nuestros equipos de estibadores acaban de terminar su turno de trabajo."
    sp "Y estan dispuestos a quedarse horas extra para desembarcar el cargamento."
    sp "Asi que problema resuelto, si esos vagos no lo van a hacer, nuestra propia gente lo hara."
    sm "Puede ser que haya un malentendido. Igual la decision es tuya, simplemente no tardes mucho, porque ya vamos muy atrasados con las pruebas."
    hide proveeduria
    hide manufactura
    with dissolve
menu:
    "Sera mejor que revisemos la situacion en el muelle en persona.":
        jump scene1Dock
    "Voy a llamar a Lat Hamzah, ustedes dos dirijanse al muelle y esperen instrucciones.":
        jump scene1Hamzah
    "No hay tiempo! Desembarquemos inmediatamente.":
        jump scene1Inmediate
        
label scene1Dock:
    #Sonido muelle
    show bg ShipScene
    with fade
    show proveeduria
    show manufactura
    with dissolve
    me "Por favor vayan y busquen al supervisor del muelle. Yo voy a hablar con la tripulacion."
    sm "Claro."
    sp "Pero... Pero... Mejor te acompano, no?"
    me "No, yo conozco al capitan del barco, buen hombre, me extrana mucho la situacion de hecho."
    hide proveeduria
    hide manufactura
    with dissolve
    "*Cuando te acercas al barco, ves que enfrente de donde esta anclado hay varias mesas donde la tripulacion esta comiendo y dos marineros tocan instrumentos de musica*"
    "*El capitan te reconoce y se acerca para saludarte, se le nota alegre y tranquilo*"
    show capitan
    with dissolve
    cap "*Hace senas para explicar que esta contento de verte y pregunta en que puede ayudarte*"
    me "*Por gestos le explico que necesito saber porque el cargamente no ha sido desembarcado*"
    cap "*Hace una serie de maromas que no alcanzas a entender, mientras constantemente levanta 3 dedos de la mano*"
    hide capitan
    with dissolve
menu:
    "Le dejo muy claro al capitan que si no desembarcan ellos, pedire que otros lo hagan y lo reportare a su supervisor":
        jump scene1DockBad
    "Le explico que me urge que desembarquen el contenido del barco.":
        jump scene1DockGood
        
label scene1DockBad:
    show capitan
    with dissolve
    "*La cara del capitan se convierte en una mueca de ira... Juras que esta a punto de golpearte*"
    cap "*Hace el gesto de entender*"
    "*El capitan da media vuelta y va hacia donde su tripulacion, empieza a gritarles, ellos empiezan a moverse y empiezan el proceso de desembarco.*"
    $ dock_bad = True
    jump scene1Final
label scene1DockGood:
    show capitan
    with dissolve
    cap "*Se encoge de hombros, como si no entiendera porque le estas pidiendo desembarcar*"
    cap "*Hace gestos de entender y se da media vuelta*"
    "En escasos momentos el capitan levanta a su tripulacion y empiezan a desembarcar el contenido del barco."
    $ dock_good = True
    jump scene1Final

label scene1Hamzah:
    "*Los dos supervisores salen de tu oficina y se dirijen al puerto.*"
    hide proveeduria
    hide manufactura
    with dissolve
    me "Ok, ahora a llamar a Lat."
    #Sonido de celular
    show bg MalaysiaScene
    with fade
    show hamzah
    with dissolve
    #Sonido de fiestas
    "*La siguiente conversacion sucede en ingles.*"
    me "Hola Lat, como haz estado? Perdona la llamada tan tarde."
    lh "*Reconoce mi acento inmediatamente*"
    lh "Hey! No hay problema, estaba despierto. Como va todo?"
    me "Pues mira, precisamente por eso te llamo, tengo una situacion en el puerto, tiene que ver con uno de sus cargamentos..."
    lh "Que podria ser?"
    me "Fijate que debia desembarcarse ayer, pero la tripulacion no lo hizo, ni siquiera es que hayan faltado papeles ni nada."
    me "Cuando les preguntaron simplemente dijeron que ese dia no lo iban a hacer."
    me "Y nos estamos atrasando con unas pruebas de equipo, la situacion es mala."
    lh "*Se queda callado un momento*"
    me "Lat? Sigues ahi?"
    lh "Si claro, aqui estoy. Ahhh pues mira, esto es algo incomodo, pensaba que lo sabias. Hoy es Prabhamkar, es el festival de uno de nuestros santos mas importantes"
    lh "El festival dura tres dias y durante esos dias no se trabaja. De hecho solo conteste el telefono porque la llamada era internacional."
    me "No estaba informado... Talvez deberia haber estudiado un poco mas sobre Malasia antes..."
    lh "Cual estudiado?!? Yo envie esa informacion y tengo un acuso de recibo del correo que envie y se me aseguro que se te habia informado de la situacion."
    lh "Iba junto con toda la informacion del envio."
    me "A quien se lo enviaste?"
    lh "A el supervisor de proveeduria de tu empresa."
    me ".{p=0.5}.{p=0.5}.{p=0.5}Ya veo............"
    lh "Mira, parece que ha habido un malentendido. Dejame llamar al capitan del barco y explicarle lo que paso, bajo las circunstancias hara una excepcion."
    me "Gracias Lat, te debo una."
    lh "No hay problema, perdona el enredo mas bien."
    lh "*Cuelga el telefono*"
    hide hamzah
    with dissolve
    show bg myoffice
    with fade
    "*Media hora despues recibo una llamada*"
    #telefono
    sm "Hey! Parece que los tripulantes ya estan desembarcando."
    sm "Le preguntamos al supervisor y dijo que no sabia porque."
    me "Yo si se porque, dejenlos que desembarquen, traigan los componentes y te explico."
    sm "Ok, perfecto."
    $ call_hamzah = True
    jump scene1Final

label scene1Inmediate:
    "*Los dos supervisores salen de tu oficina y se dirijen al puerto.*"
    hide proveeduria
    hide manufactura
    with dissolve
    #suena telefono
    me "Alo"
    sp "Ya estamos aqui, le digo a nuestro equipo de estibadores que prosigan?"
    me "Si"
    sp "Ok, voy a hacer eso."
    "*10 minutos despues*"
    sp "Listo, ya los estibadores empezaron a desembarcar."
    me "Perfecto. Hubo algun problema?"
    sp "Casi tuvimos que llamar a seguridad del puerto, los tripulantes del barco no querian dejar a los estibadores subir."
    sp "Me imagino que seguian esperando que se les pagara o algo."
    me "Hmmm, al menos ya todo va progresando, gracias."
    $ force_shipment = True
    jump scene1Final

label scene1Final:
    me "Bueno, eso ya esta resulto."
    jump scene2Start
    