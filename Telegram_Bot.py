
from telebot import TeleBot
from telebot import types

bot = TeleBot('MY_TOKEN')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('📺 Фильмы')
    btn2 = types.KeyboardButton('🍿 Сериалы')
    btn3 = types.KeyboardButton('✨ Аниме')
    btn4 = types.KeyboardButton('🐸 Мультики')
    markup.row(btn1, btn2)
    markup.row(btn3, btn4)
    bot.send_message(message.chat.id, text='Привет, {0.first_name}!\n'
                                           'Меня зовут Питошка. Я твой виртуальный друг по подбору фильмов, сериалов, мультиков и аниме.\n'
                                           'Сейчас я тебе что-нибудь подберу.'.format(
                                               message.from_user),
                     reply_markup=markup)
    bot.send_sticker(
        message.chat.id, 'CAACAgIAAxkBAAPVY2SkvQIu2ziQ-e0FGuwtOMzd8-EAAocPAAL41whJVMSxofpMEO4qBA')


@bot.message_handler(content_types=['text'])
def choose(message):
    if (message.text == '📺 Фильмы'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('📺Комедия😂')
        btn2 = types.KeyboardButton('📺Ужасы😨')
        btn3 = types.KeyboardButton('📺Мелодрама💔')
        btn4 = types.KeyboardButton('📺Боевик😎')
        back = types.KeyboardButton('Вернуться в главное меню🔙')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(back)
        bot.send_sticker(
            message.chat.id, 'CAACAgIAAxkBAAPdY2SmcX1k1ZuXs-g9d20yEO_80lMAAjQTAALVkgABSRno54hHIrjwKgQ')
        bot.send_message(message.chat.id, text='Выбери жанр',
                         reply_markup=markup)

    elif (message.text == '🍿 Сериалы'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🍿Комедия😂')
        btn2 = types.KeyboardButton('🍿Ужасы😨')
        btn3 = types.KeyboardButton('🍿Мелодрама💔')
        btn4 = types.KeyboardButton('🍿Боевик😎')
        back = types.KeyboardButton('Вернуться в главное меню🔙')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(back)
        bot.send_sticker(
            message.chat.id, 'CAACAgIAAxkBAAPdY2SmcX1k1ZuXs-g9d20yEO_80lMAAjQTAALVkgABSRno54hHIrjwKgQ')
        bot.send_message(message.chat.id, text='Выбери жанр',
                         reply_markup=markup)

    elif (message.text == '✨ Аниме'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('✨Ещë')
        back = types.KeyboardButton('Вернуться в главное меню🔙')
        markup.row(button1)
        markup.add(back)
        bot.send_photo(message.chat.id,
                       photo='https://avatars.mds.yandex.net/get-kinopoisk-image/1599028/58e9c2e7-4f75-4bdf-acc8-79e01af8fc53/1920x',
                       caption='Бездомный Бог.\n'
                               '\nПриключения незадачливого божества в непредсказуемом мире людей. ',
                       reply_markup=markup)
    elif (message.text == '✨Ещë'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('✨Хочу ещë')
        back = types.KeyboardButton('Вернуться в главное меню🔙')
        markup.row(button1)
        markup.row(back)
        bot.send_photo(message.chat.id,
                       photo='https://www.film.ru/sites/default/files/movies/posters/3661732-1457719.jpg',
                       caption='Берсерк.\n'
                       '\n«Мир средневековья, жестокие и кровавые бои, роскошные балы, дворянские интриги»',
                       reply_markup=markup)
    elif (message.text == '✨Хочу ещë'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Для истинных любителей ✨аниме✨')
        back = types.KeyboardButton('Вернуться в главное меню🔙')
        markup.row(button1)
        markup.add(back)
        bot.send_photo(message.chat.id,
                       photo='https://p.favim.com/orig/2018/11/23/ray-emma-yakusoku-no-neverland-Favim.com-6615549.jpg',
                       caption='Обещанный Неверленд.\n'
                               '\nВ приюте «Грейс Филд» под чутким надзором Мамы живёт группа детей разных возрастов. '
                               'Самые умненькие — 11-летние Норман, Эмма и Рэй — лучшие друзья всю свою жизнь. '
                               'Каждый ребёнок ждёт не дождётся усыновления, и когда он поедет в новую семью, '
                               'а пока детишки играют целыми днями в догонялки и не знают бед и невзгод. Но однажды '
                               'Норман и Эмма узнают о приюте жуткую правду, и теперь у них остаётся выбор — '
                               'сбежать или умереть. ',
                       reply_markup=markup)

    elif (message.text == 'Для истинных любителей ✨аниме✨'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Вернуться в главное меню🔙')
        markup.add(back)
        bot.send_message(message.chat.id,
                         text='{0.first_name},поздравляю, вы дошли до скрытой кнопки для истинных аниме-любителей!'.format(
                             message.from_user),
                         reply_markup=markup)
        bot.send_photo(message.chat.id,
                       photo='https://www.kino-teatr.ru/movie/poster/31567/108817.jpg',
                       caption='Ван-Пис.\n'
                               '\nГол Д. Роджер — король пиратов, добившийся за свою жизнь богатства, славы и власти - '
                               'спрятал где-то на просторах этого мира загадочное сокровище, которое все называют «Ван-Пис».'
                               ' После смерти Роджера множество смельчаков кинулись на поиски этого большого куша. '
                               'И наступила великая эпоха пиратов! Вот и паренёк по имени Луффи, живущий в маленькой '
                               'прибрежной деревушке, мечтает стать пиратом. Ещё в детстве он ненароком съел дьявольский '
                               'плод «резина-резина» и приобрёл невероятные способности. Повзрослев, он покидает родные '
                               'места в погоне за величайшим сокровищем! ',
                       reply_markup=markup)
        bot.send_message(message.chat.id,
                         text='{0.first_name}, на этом все, новые рекомендации будут позже!'.format(
                             message.from_user),
                         reply_markup=markup)

    elif (message.text == '🐸 Мультики'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('🐸Ещë')
        back = types.KeyboardButton('Вернуться в главное меню🔙')
        markup.row(button1)
        markup.add(back)
        bot.send_photo(message.chat.id,
                       photo='https://avatars.mds.yandex.net/get-kinopoisk-image/1704946/8dadd6f8-7f8e-42de-9691-006bddcb0c06/1920x',
                       caption='Иван Царевич и Серый Волк.\n'
                               '\nЦаревна-карьеристка влюбляется в мечтателя Ивана.',
                       reply_markup=markup)
    elif (message.text == '🐸Ещë'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('🐸Хочу ещë')
        back = types.KeyboardButton('Вернуться в главное меню🔙')
        markup.row(button1)
        markup.row(back)
        bot.send_photo(message.chat.id,
                       photo='https://avatars.mds.yandex.net/get-kinopoisk-image/1777765/0e6d2ab8-3e03-4461-92f2-c9224677ffcb/1920x',
                       caption='Алеша Попович и Тугарин Змей.\n'
                       '\nПоповский сын слывет недотепой, но свой город он в обиду не даст.',
                       reply_markup=markup)
    elif (message.text == '🐸Хочу ещë'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Вернуться в главное меню🔙')
        markup.add(back)
        bot.send_photo(message.chat.id,
                       photo='https://www.kino-teatr.ru/movie/poster/124350/86746.jpg',
                       caption='По ту сторону изгороди.\n'
                               '\nВ центре событий находятся два брата: Грег и Вирт. '
                               'Им предстоит путешествие через таинственный и страшный лес, и только пройдя его, '
                               'они смогут попасть домой. ',
                       reply_markup=markup)
        bot.send_message(message.chat.id, text='{0.first_name}, на этом все, новые рекомендации будут позже!'.format(message.from_user),
                         reply_markup=markup)

    elif (message.text == '📺Комедия😂'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('📺Ещë😂')
        back = types.KeyboardButton('Вернуться в главное меню🔙')
        markup.row(button1)
        markup.row(back)
        bot.send_photo(message.chat.id, photo='https://www.timeout.ru/wp-content/uploads/kpposters/6039.jpg',
                       caption='Маска.\n'
                               '\nСкромный и застенчивый служащий банка чувствует себя неуверенно с красивыми девушками '
                               'и вообще рядом с людьми. \n'
                               'Волей судьбы к нему попадает волшебная маска, и Стенли Ипкис приобретает способность '
                               'превращаться в неуязвимое мультяшное существо с озорным характером.',
                       reply_markup=markup)
    elif (message.text == '📺Ещë😂'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('📺Хочу ещë😂')
        back = types.KeyboardButton('Вернуться в главное меню🔙')
        markup.row(button1)
        markup.row(back)
        bot.send_photo(message.chat.id,
                       photo='https://pic.uma.media/pic/cardimage/1b/68/1b68a9be2345815b54147aede3c5e573.jpg',
                       caption='Моя ужасная няня.\n'
                       '\nПопав в дом к недавно овдовевшему мистеру Брауну, няня-волшебница пытается усмирить '
                       'его семерых непослушных детей. Эти сорванцы, возглавляемые Саймоном, уже избавились '
                       'от 17 предыдущих нянь и поэтому не сомневаются, что и 18-ю ждет та же участь. \n'
                       '\nОднако, когда няне Макфи все-таки удается взять ситуацию под контроль, детишки вдруг '
                       'начинают замечать, что их ужасное поведение волшебным образом приводит к совершенно '
                       'удивительным и непредсказуемым результатам…',
                       reply_markup=markup)
    elif (message.text == '📺Хочу ещë😂'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Вернуться в главное меню🔙')
        markup.add(back)
        bot.send_photo(message.chat.id,
                       photo='https://avatars.mds.yandex.net/get-kinopoisk-image/6201401/a7ef44b8-1983-4992-a889-da6f87a3f559/1920x',
                       caption='Иван Васильевич меняет профессию.\n'
                               '\nИван Грозный отвечает на телефон, пока его тезка-пенсионер сидит на троне. Советский '
                               'хит о липовом государе.',
                       reply_markup=markup)
        bot.send_message(message.chat.id, text='{0.first_name}, на этом все, новые рекомендации будут позже!'.format(message.from_user),
                         reply_markup=markup)

    elif (message.text == '📺Ужасы😨'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('📺Ещë😨')
        back = types.KeyboardButton('Вернуться в главное меню🔙')
        markup.row(button1)
        markup.row(back)
        bot.send_photo(message.chat.id, photo='https://userpic.fishki.net/2018/08/03/1488958/16f963ca2c3b49f97eeaba7edd45d019.jpg',
                       caption='Мама.\n'
                               '\nПара берет в дом девочек-сирот, а вместе с ними — зловещее нечто. \n', reply_markup=markup)
    elif (message.text == '📺Ещë😨'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('📺Хочу ещë😨')
        back = types.KeyboardButton('Вернуться в главное меню🔙')
        markup.row(button1)
        markup.row(back)
        bot.send_photo(message.chat.id,
                       photo='https://avatars.mds.yandex.net/get-kinopoisk-image/1777765/bfdef7f7-8454-48f3-8efc-dd8af05ec805/1920x',
                       caption='Корабль-призрак.\n'
                       '\nВ отдаленной части Берингова моря команда спасателей обнаруживает огромный '
                       'пассажирский лайнер, который считается пропавшим уже 40 лет.'
                       '\nОказавшись на борту судна, спасатели сталкиваются с жутким прошлым корабля и теперь '
                       'им придётся вступить в смертельную схватку с неизвестным',
                       reply_markup=markup)
    elif (message.text == '📺Хочу ещë😨'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Вернуться в главное меню🔙')
        markup.add(back)
        bot.send_photo(message.chat.id,
                       photo='https://avatars.dzeninfra.ru/get-zen_doc/3512190/pub_5fba685093538c303926838d_5fba68cc9d2ffe38eec4ce74/scale_1200',
                       caption='Поезд в Пусан.\n'
                               '\nБеспощадный вирус превращает скоростной поезд в смертельную ловушку. Самый популярный '
                               'южнокорейский хоррор.',
                       reply_markup=markup)
        bot.send_message(message.chat.id, text='{0.first_name}, на этом все, новые рекомендации будут позже!'.format(message.from_user),
                         reply_markup=markup)

    elif (message.text == '📺Мелодрама💔'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('📺Ещë💔')
        back = types.KeyboardButton('Вернуться в главное меню🔙')
        markup.row(button1)
        markup.row(back)
        bot.send_photo(message.chat.id, photo='https://avatars.mds.yandex.net/get-kinopoisk-image/1777765/c7e260aa-7894-4295-9516-109d243b35f4/1920x',
                       caption='Век Адалин.\n'
                               '\nВечно молодая Адалин встречает мужчину, ради которого готова состариться. ',
                       reply_markup=markup)
    elif (message.text == '📺Ещë💔'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('📺Хочу ещë💔')
        back = types.KeyboardButton('Вернуться в главное меню🔙')
        markup.row(button1)
        markup.row(back)
        bot.send_photo(message.chat.id,
                       photo='https://images.kinorium.com/movie/shot/709968/w1500_856170.jpg',
                       caption='Девочка со спичками.\n'
                               '\nСобытия фильма происходят «в канун Нового года в некоем северном городке». '
                               'Карен, маленькая девочка в лохмотях, не сумев продать спешащим прохожим ни одной спички, '
                               'не видит возможности в свою хибарку, засыпает под забором, присыпанная снегом, и ей снится сон..',
                       reply_markup=markup)
    elif (message.text == '📺Хочу ещë💔'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Вернуться в главное меню🔙')
        markup.add(back)
        bot.send_photo(message.chat.id,
                       photo='http://data22.i.gallery.ru/albums/gallery/165018-bb0e4-65343088-m750x740-ue5c44.jpg',
                       caption='Один день.\n'
                               '\nПосле одной ночи вместе они встречаются каждый год 15 июля.',
                       reply_markup=markup)
        bot.send_message(message.chat.id, text='{0.first_name}, на этом все, новые рекомендации будут позже!'.format(message.from_user),
                         reply_markup=markup)

    elif (message.text == '📺Боевик😎'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('📺Ещë😎')
        back = types.KeyboardButton('Вернуться в главное меню🔙')
        markup.row(button1)
        markup.row(back)
        bot.send_photo(message.chat.id, photo='https://www.1c-interes.ru/images/2015/16/21806348_DeadPool_DVD.jpg',
                       caption='Дэдпул.\n'
                               '\nБывший наемник становится сверхчеловеком поневоле.',
                       reply_markup=markup)
    elif (message.text == '📺Ещë😎'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('📺Хочу ещë😎')
        back = types.KeyboardButton('Вернуться в главное меню🔙')
        markup.row(button1)
        markup.row(back)
        bot.send_photo(message.chat.id,
                       photo='https://thumbs.dfs.ivi.ru/storage6/contents/d/7/8bb8c496696401756432507fa05712.jpg',
                       caption='Шпион по соседству.\n'
                               '\nРусская мафия наносит визит агенту ЦРУ, когда он нянчится с детьми своей девушки.',
                       reply_markup=markup)
    elif (message.text == '📺Хочу ещë😎'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Вернуться в главное меню🔙')
        markup.add(back)
        bot.send_photo(message.chat.id,
                       photo='https://xl.movieposterdb.com/08_06/2005/386140/xl_386140_8fa3416e.jpg',
                       caption='Маска Зорро.\n'
                               '\nПостаревший защитник бедняков, легендарный Зорро передает свои навыки молодому вору.',
                       reply_markup=markup)
        bot.send_message(message.chat.id, text='{0.first_name}, на этом все, новые рекомендации будут позже!'.format(message.from_user),
                         reply_markup=markup)

    elif (message.text == '🍿Комедия😂'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('🍿Ещë😂')
        back = types.KeyboardButton('Вернуться в главное меню🔙')
        markup.row(button1)
        markup.row(back)
        bot.send_photo(message.chat.id, photo='https://otzyvy.pro/image.php?nocache=1&img=uploads/posts/2019-04/1554304551_posts_737482.jpg',
                       caption='Детективное агентство Дирка Джентли.\n'
                               '\nО приключениях эксцентричного «холистического детектива» Дирка Джентли'
                               ' и его вынужденного напарника Тодда Бротцмана, которые расследуют необычные дела.',
                       reply_markup=markup)
    elif (message.text == '🍿Ещë😂'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('🍿Хочу ещë😂')
        back = types.KeyboardButton('Вернуться в главное меню🔙')
        markup.row(button1)
        markup.row(back)
        bot.send_photo(message.chat.id,
                       photo='https://thumbs.dfs.ivi.ru/storage23/contents/6/c/88548aad7ac743a1076201bf9a74e6.jpg',
                       caption='Сваты.\n'
                               '\nГородские интеллигенты и сельские жители подружатся благодаря общей внучке.',
                       reply_markup=markup)
    elif (message.text == '🍿Хочу ещë😂'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Вернуться в главное меню🔙')
        markup.add(back)
        bot.send_photo(message.chat.id,
                       photo='https://avatars.mds.yandex.net/get-kinopoisk-image/1599028/7bbd225f-e6db-4326-b600-1ac294cf9d99/1920x',
                       caption='Офис.\n'
                               '\n«Комедия для тех, у кого босс - идиот». Скучающие от безделья клерки пытаются '
                               'ужиться с безумным боссом.',
                       reply_markup=markup)
        bot.send_message(message.chat.id, text='{0.first_name}, на этом все, новые рекомендации будут позже!'.format(message.from_user),
                         reply_markup=markup)

    elif (message.text == '🍿Ужасы😨'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('🍿Ещë😨')
        back = types.KeyboardButton('Вернуться в главное меню🔙')
        markup.row(button1)
        markup.row(back)
        bot.send_photo(message.chat.id, photo='https://img.persik.by/covers/48a1aa71f8d3a358396881dd9d776c2a.jpg',
                       caption='Ходячие мертвецы.\n'
                               '\nЗомби-эпидемия захлестнула планету. Шериф Рик Граймс путешествует с семьей'
                               ' и небольшой группой выживших в поисках безопасного места. Но постоянный страх смерти '
                               'каждый день приносит тяжелые потери, заставляя товарищей по несчастью чувствовать '
                               'глубины человеческой жестокости. Рик пытается спасти близких и понимает, '
                               'что всепоглощающий страх людей может быть опаснее ходячих мертвецов.',
                       reply_markup=markup)
    elif (message.text == '🍿Ещë😨'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('🍿Хочу ещë😨')
        back = types.KeyboardButton('Вернуться в главное меню🔙')
        markup.row(button1)
        markup.row(back)
        bot.send_photo(message.chat.id,
                       photo='https://avatars.mds.yandex.net/get-kinopoisk-image/1898899/01d36aea-0f7c-4a4b-b338-38c15cf32063/1920x',
                       caption='Американская история ужасов.\n'
                               '\nОт призраков и ведьм до серийных убийц. Хоррор-антология Райана Мёрфи, которая стала современной классикой.',
                       reply_markup=markup)
    elif (message.text == '🍿Хочу ещë😨'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Вернуться в главное меню🔙')
        markup.add(back)
        bot.send_photo(message.chat.id,
                       photo='https://ovideo.ru/images/posters/0001/9929/0002.jpg',
                       caption='Байки из склепа.\n'
                               '\nВ основе сериала лежат отличные друг от друга истории, но объединённые одной темой — '
                               'совершающие плохие поступки всегда расплачиваются за содеянное.',
                       reply_markup=markup)
        bot.send_message(message.chat.id, text='{0.first_name}, на этом все, новые рекомендации будут позже!'.format(message.from_user),
                         reply_markup=markup)

    elif (message.text == '🍿Мелодрама💔'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('🍿Ещë💔')
        back = types.KeyboardButton('Вернуться в главное меню🔙')
        markup.row(button1)
        markup.row(back)
        bot.send_photo(message.chat.id, photo='https://avatars.mds.yandex.net/get-kinopoisk-image/1900788/2fd93342-fdc6-48a5-85d5-54bb8fa780b9/1920x',
                       caption='Почему женщины убивают.\n'
                               '\nЛюбящие и ранимые, они умеют ненавидеть и готовы дать отпор.',
                       reply_markup=markup)
    elif (message.text == '🍿Ещë💔'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('🍿Хочу ещë💔')
        back = types.KeyboardButton('Вернуться в главное меню🔙')
        markup.row(button1)
        markup.row(back)
        bot.send_photo(message.chat.id,
                       photo='https://avatars.mds.yandex.net/get-kinopoisk-image/4303601/d8580a1e-7d49-4916-b452-f5ed06a5ce8a/1920x',
                       caption='Ты.\n'
                               '\nНа что вы готовы ради любви? \n'
                               'Когда успешный менеджер книжного магазина встречает '
                               'талантливую начинающую писательницу, для него ответ очевиден: абсолютно на все. '
                               'Используя соцсети, он узнает мельчайшие подробности о жизни девушки, чтобы подобраться '
                               'к ней как можно ближе. Милая влюбленность перерастает в опасную одержимость. '
                               '\nПарень готов тихо и методично устранить любое препятствие на пути к своей цели, '
                               'даже если это препятствие — человек.',
                       reply_markup=markup)
    elif (message.text == '🍿Хочу ещë💔'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Вернуться в главное меню🔙')
        markup.add(back)
        bot.send_photo(message.chat.id,
                       photo='https://a.viewy.ru/2022/06/11/dyshevno16549525024134.jpg',
                       caption='Истинная красота.\n'
                               '\nДевушка с несовершенной внешностью овладевает искусством макияжа. ',
                       reply_markup=markup)
        bot.send_message(message.chat.id, text='{0.first_name}, на этом все, новые рекомендации будут позже!'.format(message.from_user),
                         reply_markup=markup)

    elif (message.text == '🍿Боевик😎'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('🍿Ещë😎')
        back = types.KeyboardButton('Вернуться в главное меню🔙')
        markup.row(button1)
        markup.row(back)
        bot.send_photo(message.chat.id, photo='https://pic.rutubelist.ru/video/9f/02/9f02ebdcfd143513fbca6756d18eb8bb.jpg',
                       caption='Бумажный дом.\n'
                               '\nИстория о преступниках, решивших ограбить Королевский монетный двор Испании и украсть 2,4 млрд евро.',
                       reply_markup=markup)
    elif (message.text == '🍿Ещë😎'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('🍿Хочу ещë😎')
        back = types.KeyboardButton('Вернуться в главное меню🔙')
        markup.row(button1)
        markup.row(back)
        bot.send_photo(message.chat.id,
                       photo='https://avatars.mds.yandex.net/get-kinopoisk-image/1629390/76b5a130-0cb1-4f7c-90c3-23aa2334f538/1920x',
                       caption='Гримм.\n'
                               '\nКоп из Портленда начинает видеть в людях пугающие сущности.',
                       reply_markup=markup)
    elif (message.text == '🍿Хочу ещë😎'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Вернуться в главное меню🔙')
        markup.add(back)
        bot.send_photo(message.chat.id,
                       photo='https://thumbs.dfs.ivi.ru/storage9/contents/b/2/315440b08343188854733e1ab4f4ff.jpg',
                       caption='Легенда об Искателе.\n'
                               '\nЕщё вчера юный Ричард Сайфер был всего лишь лесным проводником, а нынче ему '
                               'выпал на долю тяжкий жребий Искателя Истины. Тяжкий, ибо магия не приносит радости, '
                               'а за истину, как и за могущество, расплачиваются дорогой ценой. Тяжкий — '
                               'ибо Искателю Истины надлежит вступить с величайшим из черных магов трех королевств, '
                               'безжалостным Даркеном Ралом, повелителем Д\'Хары в смертельную схватку...',
                       reply_markup=markup)
        bot.send_message(message.chat.id, text='{0.first_name}, на этом все, новые рекомендации будут позже!'.format(message.from_user),
                         reply_markup=markup)

    elif (message.text == 'Вернуться в главное меню🔙'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('📺 Фильмы')
        btn2 = types.KeyboardButton('🍿 Сериалы')
        btn3 = types.KeyboardButton('✨ Аниме')
        btn4 = types.KeyboardButton('🐸 Мультики')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        bot.send_sticker(
            message.chat.id, 'CAACAgIAAxkBAAIC7GNk64QZrN1sGx4M6fBTJ3b2mh6CAAI0EwAC1ZIAAUkZ6OeIRyK48CoE')
        bot.send_message(message.chat.id, text='{0.first_name}, сейчас я подберу тебе что-нибудь'.format(message.from_user),
                         reply_markup=markup)

    else:
        bot.send_sticker(
            message.chat.id, 'CAACAgIAAxkBAAPjY2SmiefL9f3_w_k1MsWdp9ghKa0AAq8TAAKNjQhJTLCsORtNPngqBA')
        bot.send_message(
            message.chat.id, text='На такую команду я не запрограммирован..')


bot.polling(none_stop=True, interval=0)
