import telebot
from telebot import types
import psycopg2

token=
bot=telebot.TeleBot(token)

conn=psycopg2.connect(database="timetable_db",
                      user="postgres",
                      password="25lol25lol25",
                      host="localhost",
                      port="5432")

def execute_read_query(connection,query):
    cursor=connection.cursor()
    result=None
    try:
        cursor.execute(query)
        result=cursor.fetchall()
        return result
    except Error as e:
        bot.send_message(message.chat.id,"Ошибка '{e}' обнаружена!",
                         reply_markup=markup)

@bot.message_handler(commands=['start','back'])
def start_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt1=types.KeyboardButton('/help')
    bt2=types.KeyboardButton('/timetable')
    bt3=types.KeyboardButton('/subjects')
    bt4=types.KeyboardButton('/teachers')
    markup.add(bt1)
    markup.add(bt2)
    markup.add(bt3)
    markup.add(bt4)
    bot.send_message(message.chat.id,"Здравствуйте, я буду помогать Вам ориентироваться в расписании!\n"
                     "Чтобы узнать на что я способен напишите команду /help"
                                      " или нажмите соответствующую кнопку.",
                     reply_markup=markup)

@bot.message_handler(commands=['help'])
def help_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt1=types.KeyboardButton('/timetable')
    bt2=types.KeyboardButton('/subjects')
    bt3=types.KeyboardButton('/teachers')
    markup.add(bt1)
    markup.add(bt2)
    markup.add(bt3)
    bot.send_message(message.chat.id, "Вы можете посмотреть расписание, "
                                      "список предметов и имена преподавателей:\n"
                                      "/timetable - посмотреть расписание.\n"
                                      "/subjects - посмотреть список предметов.\n"
                                      "/teachers - посмотреть имена преподавателей.",
                     reply_markup=markup)

@bot.message_handler(commands=['subjects'])
def subjects_message(message):
    sql_com="SELECT * FROM subjects_tab"
    otvet=execute_read_query(conn,sql_com)
    bot.send_message(message.chat.id,str(otvet))

@bot.message_handler(commands=['teachers'])
def teachers_meddage(message):
    sql_com="SELECT full_name,subject FROM teachers_tab"
    otvet=execute_read_query(conn,sql_com)
    bot.send_message(message.chat.id,str(otvet))


@bot.message_handler(commands=['timetable'])
def timetable_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt1=types.KeyboardButton('/понедельник')
    bt2=types.KeyboardButton('/вторник')
    bt3=types.KeyboardButton('/среда')
    bt4=types.KeyboardButton('/четверг')
    bt5=types.KeyboardButton('/пятница')
    markup.add(bt1)
    markup.add(bt2)
    markup.add(bt3)
    markup.add(bt4)
    markup.add(bt5)
    bot.send_message(message.chat.id,"На какой день посмотрим расписание?",
                     reply_markup=markup)

@bot.message_handler(commands=['понедельник'])
def mond_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt1=types.KeyboardButton('/back')
    markup.add(bt1)
    sql_com="SELECT subject,room,time FROM timetable_tab WHERE day = 'Понедельник'"
    otvet=execute_read_query(conn,sql_com)
    for i in range(0,5):
        mes=otvet[i]
        bot.send_message(message.chat.id,mes,reply_markup=markup)

@bot.message_handler(commands=['вторник'])
def tues_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt1=types.KeyboardButton('/back')
    markup.add(bt1)
    sql_com="SELECT subject,room,time FROM timetable_tab WHERE day = 'Вторник'"
    otvet=execute_read_query(conn,sql_com)
    bot.send_message(message.chat.id,str(otvet),reply_markup=markup)

@bot.message_handler(commands=['среда'])
def wedn_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt1=types.KeyboardButton('/back')
    markup.add(bt1)
    sql_com="SELECT subject,room,time FROM timetable_tab WHERE day = 'Среда'"
    otvet=execute_read_query(conn,sql_com)
    bot.send_message(message.chat.id,str(otvet),reply_markup=markup)

@bot.message_handler(commands=['четверг'])
def thur_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt1=types.KeyboardButton('/back')
    markup.add(bt1)
    sql_com="SELECT subject,room,time FROM timetable_tab WHERE day = 'Четверг'"
    otvet=execute_read_query(conn,sql_com)
    bot.send_message(message.chat.id,str(otvet),reply_markup=markup)

@bot.message_handler(commands=['пятница'])
def frid_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt1=types.KeyboardButton('/back')
    markup.add(bt1)
    sql_com="SELECT subject,room,time FROM timetable_tab WHERE day = 'Пятница'"
    otvet=execute_read_query(conn,sql_com)
    bot.send_message(message.chat.id,str(otvet),reply_markup=markup)


bot.infinity_polling()
    









    

