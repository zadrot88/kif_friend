import sqlite3

def select_one(arg):
    if arg == 'Шишки':
        a = ['🍀Шишки (LSD, OG KUSH)', '☘️ 1гр - 200 грн','☘️ 2гр - 350 грн' ,'☘️ 3гр - 450грн', '(Фото Товара) https://postimg.cc/gallery/1qcfl6i94/']
        return a
    elif arg == 'Амф':
        a = ['💭Амфетамин HQ','🌬 0.5гр - 350 грн', '🌬 1гр - 600 грн', '(Фото Товара) https://postimg.cc/XpDQK5p1']
        return a
    elif arg == 'Экстази':
        a = ['💊ЭКСТАЗИ (Pink Monkey, KENZO) 250mg', '🎁 1 шт - 300 грн', '🎁 2 шт - 550 грн' , '(Фото Товара) https://postimg.cc/FfXqcS65']
        return a
    elif arg == 'Кокаин':
        a = ['❄️Cocaine UHQ 95%', '🌨 0.5гр - 90 $', '🌨 1гр - 160 $', '(Фото Товара) https://postimg.cc/62kMZ2z4']
        return a
    elif arg == 'Марка':
        a = ['🍭Марки LSD', '🌈 1шт - 200 грн', '🌈 2шт - 300 грн', '(Фото Товара) https://postimg.cc/cgwQVDM6']
        return a
    elif arg == 'Гашиш':
        a = ['🍁Гашиш Марокко', '🍂 0.25гр - 300 грн',
                '🍂 0.5гр - 500 грн',
                '🍂 1гр - 800 грн',
                '(Фото Товара) https://postimg.cc/bsNmth9T']
        return a
    elif arg == 'Кристалы MDMA':
        a = ['Ⓜ️MDMA CRISTAL 98%',
            '💎 0.5гр - 800 грн',
            '💎 1гр - 1500 грн',
            '(Фото Товара) https://postimg.cc/3kNfPTyR']
        return a
    else:
        return 'NO'

def user_init(id, user_name, first_name):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    flag = False
    cursor.execute('SELECT id FROM users')
    words = cursor.fetchall()
    for i in words:
        if i[0] == id:
            flag = True
    if flag == True:
        pass
    else:
        cursor.execute('INSERT INTO users (id, user_name, first_name) VALUES (?, ?, ?)',
                       (id, user_name, first_name))
    conn.commit()
    cursor.close()
    conn.close()

def all_id():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM users')
    words = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return words[0]

def all_about_user():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    words = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return words

