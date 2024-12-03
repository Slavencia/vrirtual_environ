from flask import Flask
import random
app = Flask(__name__)

facts = ["Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс, когда они находятся вне зоны покрытия сети или не могут использовать свои устройства.",
         "Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.",
         "Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время."]

koin = ["Орёл","Решка"]

@app.route("/")
def hello_world():
    return '''<h1>Добро пожаловать на сайт, чтобы увидеть случайчный факт перейдите на следущую старницу по ссылке:</h1><a href="/random">Посмотреть случайный факт!</a><br>
    <a href="/reverse">Страница с монеткой!</a>'''

@app.route("/random")
def randomslov():
    return f'<p>{random.choice(facts)}</p><a href="/">Главная старница!</a><br><a href="/reverse">Страница с монеткой!</a>'

@app.route("/reverse")
def reverse():
    return f'<p>Выпала монетка: {random.choice(koin)}</p><a href="/random">Посмотреть случайный факт!</a><br><a href="/">Главная старница!</a>'

@app.route("/prikol")
def prikol():
    return '''<body>
    
    <div class="wapper">
        
        <div class="square">
            
    <h1>Технологические зависимости!</h1>
    <p>Технологические зависимости - Это такой вид зависимости, когда человек не может обойтись без использования определенных
        технологий и устройств.
        Эта зависимость может привести к тому, что человек потеряет способность функционировать без
        этих технологий совсем... Что может сказаться на уровне его жизни.</p>
    <h2>Вот самые распространенные технологические зависимости:</h2>
             <ul>
                   <li>Социальные сети и мессенджеры: социальные сети уменьшают время, которое мы проводим в реальном мире. А еще привыкаем к постоянному обновлению новостей и сообщений.</li>
                   <li>Смартфоны и планшеты: смартфоны и планшеты могут стать привычным способом общения c миром, и люди могут стать зависимыми от постоянной проверки уведомлений! </li>
                   <li> Игры и онлайн-развлечения: игры и онлайн-развлечения могут стать зависимостью, особенно в случаях, когда люди проводят слишком много времени в виртуальном мире вместо реальной жизни.</li>
                   <li>Интернет-шопинг и онлайн-покупки: люди могут стать зависимыми от онлайн-шопинга, особенно если они используют eго для удовлетворения эмоциональных потребностей. </li>
                   
                   
                </div>
                </ul>
                
                <div style="position:relative; overflow:hidden;"><a href="https://yandex.ru/maps/13/tambov/?utm_medium=mapframe&utm_source=maps" style="color:#eee;font-size:12px;position:absolute;top:100px;"></a><a href="https://yandex.ru/maps/13/tambov/?ll=41.420790%2C52.769744&utm_medium=mapframe&utm_source=maps&z=15" style="color:#00ff0d;font-size:12px;right: 4200px;top: 1400px;"></a><iframe src="https://yandex.ru/map-widget/v1/?ll=41.420790%2C52.769744&z=15" width="380" height="320" frameborder="1" allowfullscreen="true" style="position:relative; right:-830px; top:10px;"></iframe></div>
                <iframe src="https://www.meteoblue.com/en/weather/widget/daily/ip_romania_675514?geoloc=fixed&days=5&tempunit=CELSIUS&windunit=KILOMETER_PER_HOUR&precipunit=MILLIMETER&coloured=coloured&pictoicon=1&maxtemperature=1&mintemperature=1&windspeed=1&windgust=0&winddirection=1&uv=0&humidity=0&precipitation=0&precipitationprobability=0&spot=0&pressure=0&layout=light"  frameborder="0" scrolling="NO" allowtransparency="true" sandbox="allow-same-origin allow-scripts allow-popups allow-popups-to-escape-sandbox" style="width: 270px; height: 420px"></iframe><div><!-- DO NOT REMOVE THIS LINK --><a href="https://www.meteoblue.com/en/weather/week/ip_romania_675514?utm_source=daily_widget&utm_medium=linkus&utm_content=daily&utm_campaign=Weather%2BWidget" target="_blank" rel="noopener"></a></div>
                <img src="https://empathycenter.ru/upload/medialibrary/1fb/jnmf90lr32spzxanbvy7y0h3w7pop6uk.jpg" alt="Image 1">;
       
</body>'''


app.run(debug=True)