# You can place the script of your game in this file.
# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg outside = "OfficeFrontScene.png"
image bg myoffice = "MyOfficeScene.png"
# Declare characters used by this game.
define me = Character('Yo', color="#EB6621")

# The game starts here.
label start:
    show bg outside
    with dissolve
    "Welcome/Bienvenido/Wielkomen a BarBarBar, un juego sobre como las diferencias culturales pueden afectar nuestro trabajo"
    "Más especificamente un proyecto...{p=1.0}.{p=1.0}.{p=1.0}.o más bien SU proyecto"
    "¡Felicitaciones, ha sido ascendido!"
    #Insertar musica feliz aqui(Standing Ovation/Oscars)
    "Usted es un nuevo director de proyecto que fue asignado a un equipo multicultural hace poco."
    "Ya lleva unos meses trabajando con su equipo, superando retos y tomando decisiones."
    "Hoy es un día como cualquier otro{p=2.0}...¿verdad?"
    
    #Cambiamos al frente de la oficina
    me "Todo parece indicar que hoy sera un dia sencillo."

    jump scene1Start
    

label final:
    show bg outside
    with fade
    "Bueno, ha sido un largo dia, veamos los resultados"
    "Sobre la escena de los componentes atrasados:"
    if dock_bad == True:
        "Mala idea amenazar al capitan. Ellos no estaban trabajando porque tenian libre para celebrar un dia sagrado."
        "Ambos reportaron el incidente y su supervisor se enfado contigo por tu falta de sensibilidad y obligarlos a trabajar en uno de sus dias mas sagrados."
        "Adicionalmente el supervisor te informa que se te habia informado de este dato antes de la entrega."
        "Deciden cambiar el barco que hace las entregas, el nuevo barco es una carcacha y el nuevo capitan es irresponsable y problematico."
    if dock_good:
        "Despues de hablar con el capitan y su supervisor se aclara el malentendido, ellos no estaban trabajando porque tenian libre para celebrar un dia sagrado."
        "Para el futuro se decide reclutar a un teniente que habla excelente ingles."
    if call_hamzah:
        "Excelente decision, el error se corregio rapidamente. El tiempo perdido del proyecto fue minimo."
        "El supervisor de proveeduria abandono la compania no mucho despues."
    if force_shipment:
        "Ellos no estaban trabajando porque tenian libre para celebrar un dia sagrado."
        "La compania de manufactura presento una queja formal por discriminacion cultural y cancelaron el contrato."
        "... Aun estas buscando un sustituto..."
        "Adicionalmente la OIT(Organizacion Internacional del Trabajo) presento una demanda para sancionar a la compania por violacion de los derechos de trabajadores internacionales."
        "...La ganaron..."
    "Sobre la escena de almuerzo"
    if atc_fired:
        "Decides cambiar a tu ATC."
        "El nuevo ATC no sabe nada sobre cultura oriental"
        "Tus negociaciones van de mal en peor..."
    else:
        "Le pides a tu ATC que redacte una mejor guia cultural y te disculpas por especificar que los clientes eran japoneses."
        "Tu ATC te ayuda a redactar una disculpa al estilo japones para enviarla."
        "Tus clientes estan muy sorprendidos con la disculpa y tambien se disculpan por ser tan sensibles."
        "Tu relacion con ellos ahora es excelente y usan la anecdota en entrenamientos de la empresa."
    "Sobre la escena de Alaric:"
    if alaric_fired:
        "Alaric fue reasignado y se decidio contratar a ingenieros espanoles para hacer el trabajo."
        "La comunicacion mejoro sustantivamente..."
        "... pero su nivel tecnico dejaba bastante que desear, asi que el proyecto tuvo problemas tecnicos hasta el final."
        "Ahora los clientes estan exigiendo que soluciones los problemas tecnicos de la entrega... El costo y tiempo de tu proyecto acaba de crecer en un 60%."
    else:
        "Conservaste a Alaric en el equipo"
        "Cuando analizaste mejor las metricas de tu equipo te diste cuenta que los companeros que trabajaban con Alaric, tenian malas metricas porque no estaban familiarizados con la tecnologia."
        "La directora de RRHH te refirio a unos recursos que se acababan de liberar, todos hablaban excelente ingles y uno de ellos coreano basico."
        "Decides cambiar a los integrantes de tu equipo, rapidamente Alaric aprovecha y empieza a entrenar a los nuevos recursos."
        "La entrega se hace algo atrasada, pero con una calidad excelente, el cliente esta muy complacido."
    "Bueno, este dia ha sido algo duro, pero ya ha terminado."
    "Juega de nuevo y trata de obtener el mejor resultado!"
    return
