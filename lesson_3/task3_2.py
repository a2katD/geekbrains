# Выполнить функцию, которая принимает несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def user_info(name, surname, year_birth, sity_life, email, phone, sity_birth):
    print(f"""{surname} {name} родился в {year_birth} году в городе {sity_birth}, проживает в городе {sity_life},
его адрес электронной почты: {email}, а телефон: {phone}""")


user_info(phone="8(800)333-02-95", surname="Навальный", name="Алексей", year_birth=1976, email="fbk@fbk.info",
          sity_life="Москва", sity_birth="Москва")
