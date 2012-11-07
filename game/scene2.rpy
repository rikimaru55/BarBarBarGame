#Images
image bg RestaurantScene="RestaurantScene.png"
image cliente1 = Image("Cliente1.png", yalign=0.35, xalign=0.0)
image cliente2 = Image("Cliente2.png", yalign=0.30,xalign=0.6)
image atci = Image("ATC.png", yalign=0.40,xalign=0.0)
#Characters
define atc = Character('ATC', color="#B2004A")
define c1 = Character('Sr. Takahashi' , color="#5EB262")
define c2 = Character('Sr. Watanabe', color="#00FF0C")
# The scene starts here.
label scene2Start:
    show bg myoffice
    with fade
    me "*Empiezo a prepararme para un almuerzo con clientes orientales*"
    "*Entra mi Asesora Tecnica Cultural(ATC)*"
    #Sonido puerta
    show atci
    with dissolve
    atc "*Me entrega un informe sobre costumbres orientales a tomar en cuenta durante el almuerzo*"
    me  "Entonces aquí esta toda la información para el almuerzo de hoy con los clientes?"
    atc "Si jefe, ahí tienes todas las formas de saludar, protocolos de comida e información general sobre China, Japón y Corea en caso de alguna duda."
    atc "Tambien ahi tienes sobre los tipos de comida que ellos usualmente prefieren, sabes usar los palillos de buena forma?"
    me  "Claro que si! Me encanta la comida asiatica."
    atc "Perfecto! Entonces no deberia haber problema."
    me "Ok, muchas gracias."
    hide atci
    with dissolve
    show bg RestaurantScene
    with fade
    #Sonidos restaurante
    "Llegas al restaurante e inmediatamente reconoces a tus clientes de fotos que habias recibido."
    show cliente1
    show cliente2
    with dissolve
    "*La siguiente conversacion sucede en ingles*"
    me "*Haciendo reverencia según mi ATC me dice* Bienvenidos a la presentación del proyecto, nuestra empresa preparo un almuerzo tradicional para que se sientan mas a gusto!"
    c1 "Muy agradecido, tenemos varias semanas de gira y nos hacia falta sentirnos como en casa."
    me "Me alegra, proseguimos?"
    c2 "Si, claro."
    "Durante la comida mientras explicas los puntos del proyecto, casi botas tus palillos en varias ocasiones."
    "Para evitar esto decides poner tus platillos verticalmente en el tazon de arroz."
    "*Inmediatamente la expresion de tus clientes cambia, se vuelve mas seria y algo sombria.*"
    c1 "Le agradecemos el almuerzo, estaremos en contacto."
    me "Perfecto, tienen mi informacion de contacto?"
    c2 "Si, gracias"
    "*Nos despedimos formalmente y salen casi corriendo del restaurante*"
    hide cliente1
    hide cliente2
    with dissolve
    show bg myoffice
    with fade
    "Apenas entras recibes una llamada de tu contacto en Japon y el te menciona haber recibido una queja por una falta de respeto durante el almuerzo."
    "Le aseguras no recordar nada..."
    me "Hmmm, sera mejor si hablo con mi ATC, talvez pueda decirme algo."
    show atci
    with dissolve
    me "Acabo de recibir una queja de nuestro contacto en Japon sobre una falta durante el almuerzo. Crees que podrias ayudarme a aclararlo?"
    atc "Japon, hmmm, bueno el informe que pediste era sobre cultura oriental y solo cubri las generalidades, puede que el fallo haya estado ahi."
    hide atci
    with dissolve
menu:
    "Le cuento todo lo que hice durante la cena, talvez pueda aclararme que hice mal":
        jump scene2ATC
    "Lo recrimino en el acto, el deberia haberme pedido mas informacion.":
        $ atc_fired = True
        jump scene2Final
        
label scene2ATC:
    show atci
    with dissolve
    atc "Hmmm, ya veo, creo que ya se donde esta el error."
    atc "Para los japonese colocar los palillos verticalmente en el tazon es una simbolo de muerte y poca esperanza..."
    me "Jamas se me hubiera imaginado..."
    atc "Bueno, es que es un detalle muy pequeno."
    hide atci
    with dissolve
menu:
    "La recrimino por no haber tomado en cuenta este detalle.":
        $ atc_fired = True
        jump scene2Final
    "Le agradezco su ayuda aclarando el problema y le pido que redacte un nuevo informe, ahora con un enfasis en Japon":
        $ atc_fired = False
        jump scene2Final

label scene2Final:
    hide atci
    with dissolve
    "Ok... Este dia se esta volviendo interesante"
    jump scene3Start