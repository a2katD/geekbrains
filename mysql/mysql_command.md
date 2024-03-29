#Загрузки базы данны через консоль линукса
mysql <name_databases> < <путь к файлу>
#Выгрузка дампа базы данных через консоль линукса
mysqldump <name_databases> > <путь к файлу>.sql

################# Работа с БД ########################
CREATE DATABASE <name>; - создает БД
SHOW DATABASES; - показывает какие есть БД
SHOW VARIABLES LIKE 'datadir'; - показывает директорию где хранятся БД
DROP DATABASES <name>; - удаляет базу данных
USE <name>; - выбирает базу данных

################# Работа с Таблицами ########################
SHOW TABLES; - показывает таблицы
CREATE TABLE <name_table>; - создает таблицу
CREATE TABLE IF NOT EXISTS <name-table>; - создает таблицу если еще не существует
DESCRIBE <name_table> ;- показывает структуру таблицы

CREATE TABLE <name> (id INT(8)); - создает таблицу с инт значение в 8 символов(ведушие пробиелы)
CREATE TABLE <name> (id INT(8) ZEROFILL);  - тоже самое но ведушие нули
CREATE TABLE <name> (id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT);
# создаёт уникальное значение id
# SERIAL == BIGINT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE
CREATE TABLE <name> (id SERIAL PRIMARY KEY); - тоже самое но коротко

CREATE TEMPORARY TABLE <name> - создает временную таблицу

################# CRUD операции ######################
#SELECT - Показать
SELECT RAND(); - возвращает случайное значение от 0 до 1
SELECT <name> FROM <name_table> ORDER BY RAND() LIMIT 1;
# возвращает 1 случайное значение из таблицы

#INSERT - Вставить
INSERT INTO <name> VALUES (5); - помещает в таблицу значение 5
CREATE TABLE <name> (id DECIMAL(7,4)); - точные данные, всего 7, 4 из них после запятой

#UPDATE - обновить
UPDATE <name_table> SET <name_column> = 'значение'; - обновляет столбец name_column в таблице name_table на "значение"

#DELETE

#DROP - Удалить
DROP TABLE <name> - удаляет таблицу, если её нет = ошибка
DROP TABLE IF EXISTS <name> - удаляет таблицу если она существует
TRUCATE <name>; - очищает таблицу

#ALTER - Изменить тип данных ячеек
ALTER TABLE <name> CHANGE <id> <id> INT UNSIGNED NOT NULL; - изменяет поле <id> таблицы <name>
ALTER TABLE <name> RENAME <name_new>; - ппереименовывает таблицу
ALTER TABLE <name_table> ADD COLUMN <name_column> <тип строки> AFTER <name_colum> ###### тут разобраться ##############
# Добавляет в таблицу строку, после определенной строки
ALTER TABLE tbl ADD collect JSON; - создает коллекцию JSON (столбец)
INSERT INTO tbl VALUES (1, '{"first": "HELLO", "second": "WORLD"}'); - добавляет значение в коллекцию
SELECT collect->>"$.first" FROM tbl;
# Обращается по ключу JSON

ENUM - одно значение из списка
SET -  комбинаций значений из списка


CREATE INDEX index_of_catalog_id ON products (catalog_id);
# Добавляет ИНДЕКС значаниею каталог_ид в таблице Продукты
DROP INDEX index_of_catalog_id ON products;
#удаляет ИНДЕКС из таблицы Продукты
CREATE INDEX index_of_catalog_id USING BTREE ON products (catalog_id);
# явно требуем использовать ИНДЕКС как бинарное дерево
CREATE INDEX index_of_catalog_id USING HASH ON products (catalog_id);
# явно требуем использовать ИНДЕКС как хеш

############## РАБОТА С ДАТАМИ ########################
SELECT '2018-10-01 0:00:00'; - формат вставляемой даты
SELECT '2018-10-01 0:00:00 + INTERVAL 1 DAT'; - добавляет 1 день к указанной дате
SELECT '2018-10-01 0:00:00 + INTERVAL '1-1' YEAR_MONTH'; - добавляет 1 го и 1 месяц
#######################################################

################ УСЛОВНЫЕ ОПЕРАТОРЫ ###################
DIV - целочисленное деление
MOD - тоже самое что % - остаток от деления
<=> - безопасное сравнение, может сравнить с NULL
IS NULL - тоже самое, сравнивает с NULL

AS - указание на что либо, значения не сохраняются, вычисляются каждый раз
#CREATE TABLE tbl (x INT, y INT, summ INT AS (x+y));
STORED - позволяет сохранить значение на диск значения

AND - и
OR - или
NOT - не
IN - в
#SELECT * FROM tbl WHERE id IN (1,2,5);
WHERE - ГДЕ! условие, которое выполняется, если получает TRUE
ON - тоже самое что WHERE но исльзуется при соединении таблиц, происходит ДО соединения
BETWEEN - возвращает TRUE или FALSE, если значение входит в диапазон
#SELECT 2 BETWEEN 2 AND 4; - Вернёт 1

ANY = SOME - хотябы одно условие истина = истина, пример:
#SELECT name FROM products WHERE price < ANY(SELECT price FROME products WHERE catalog_id = 1)
ALL - все условия истина = истина, ичаче лож
#SELECT name FROM products WHERE price < ALL(SELECT price FROME products WHERE catalog_id = 1)
EXISTS


LIKE - всё равно что равно, отличие в том, что поддерживает спецсимволы
% - спецсимвол - заменяет любое количество символов
_ - спецсимвол - заменяет ровно 1 символ
чтобы экранировать данные символы используется обратный слеш
#######################################################

################ РЕГУЛЯРНЫЕ ВЫРАЖЕНИЯ #################
http://website-lab.ru/article/regexp/shpargalka_po_regulyarnyim_vyirajeniyam/

RLIKE или REGEXP - регулярные выражения!
^ - привязка к началу строки если написано в начале
$ - привязка к концу строки если написано в конце
| - логическое или
. - один любой символ, кроме перевода строки
чтобы экранировать данные символы используется ДВОЙНОЙ обратный слеш

[] - классы - ограничивают поиск теми символами, которые заключены в них
#SELECT 'a' RLIKE '[abc]'; = 1
#SELECT 'a' RLIKE '[b-z]'; = 0 можно задать дипозон
[^d] - Любой символ кроме d
[^0-9] - Любой символ кроме цифр
[[:digit:]] - так экранируются классы (в этом примере поиск числа)
[[:alpha:]] - тут идёт поиск строки

Квантификаторы - идут после классов, говорят о количестве символов:
? - {0,1} - символ входит ноль или 1 раз
* - {0,} - любое количество входжений, включая ноль
+ - {1,} - одно или более вхождений символа в строку
{4} - точное указание количества символов
{1,4} - от 1 до 4 раз

Примеры:
SELECT '1' RLIKE '^[0-9]+$'; - ищет любые цифры с начала строки, минимум 1 вхождение привязка к концу строки

'^[0-9]*\\.[0-9]{2}'$ - ищет от начала строки, любое количество символов, затем
ищет точку, затем любые 2 цифры с привязкой к концу строки
#######################################################

########### ПРЕДОПРЕДЕЛЕННЫЕ ФУНКЦИИ #################
NOW() - функция возвращает текущую дату и время
DATE() - Фунеция возвращает только дату
DATE_FORMAT() - форматирование даты, пример:
#DATE_FORMAT('2018-06-12 01:59:59', 'На дворе %Y год');
#На дворе 2018 год
UNIX_TIMESTAMP() - тоже формат времени, на числом, период с 1970 по 2038, занимает 4 вместо 8 байт
FROM_UNIXTIME() - обратное преобразование
TIMESTAMPDIFF(YEAR, <дата>, <дата>) - возвращает количество ЛЕТ, прошедших с 1 по 2 даты

VERSION() - возвращает версию
DATABASE() - возвращает текущую базу данных
USER() - возвращает текущего пользователя
LAST_INSERT_ID() - возвращает значения автоинкремента

RAND() - рандомайзер, возвращает от 0 до 1 не вкл, пример
#SELECT * FROM users ORDER BY RAND() - выдаст записи в случайном порядке
POW() - возводит в квадрат
SQRT() - возврвщает квадратный корень числа
SIN() - возвращает синус
COS() - возвращает косинус
RADIANS() - преобразовывает угол в радианы (180градусов = ПИ = 3.141592653589793)

ROUND(<значение>, <кол-во знаков после запятой>) - округляет значение, математически
CEILING() - округляет в большую сторону
FLOOR() - округляет в меньшую сторону

MIN(<name>) - минимум
MAX(<name>) - максимум
AVG(<name>) - среднее
SUM(<name>) - сумма
COUNT(<name>) - считает количество, принимает в качестве аргумента имя столбца, игнорирует NULL (исключение *)
# SELECT catalog_id, COUNT(*) AS total FROM products GROUP BY catalog_id - отдельно посчитает каждую группу

SUBSTRING(<значение>, <откуда вырезать> ,<кол-во символов>) - вырезает строку
CONCAT() - соединяет строки

IF() - принимает 3 значения через запятую, условие, если истина, если лож
#SELECT IF('Условие', 'в случае тру', 'в случае фолс')
CASE() - многозадачное условие, пример:
SELECT 
  CASE
    WHEN color = 'red' THEN 'красный'
    WHEN color = 'blue' THEN 'синий'
    WHEN color = 'green' THEN 'зеленый'
    ELSE 'белый'
  END
FROM rainbow;

INET_ATON('192.168.1.1') - превращает IP в число
INET_NTOA ('3232235777') - обратная фунеция
UUID() - уникальный универсальный идентификатор
######################################################

############### СОРТИРОВКА ############################
ORDER BY - сортировка по столбцу, можно указать несколько значений
DESC - обратная сортировка, пишется в конце
#SELECT * FROM catalog ORDER BY name DESC;

LIMIT - Ограничивает количество извлекаемых записей
LIMIT 2, 4 - извлекает 4 записи, начиная со ТРЕТЬЕЙ!
LIMIT 4 OFFSET 4 - тоже самое

DISTINCT - показывает только уникальные записи, пишется перед именем таблицы
#SELECT DISTINCT catalog FROM products ORDER BY catalog_id;
ALL - выводит ВСЕ значения столбца(стоит по умолчанию)

################ ГРУППИРОВКА ДАННЫХ ##################
GROUP BY - группирует данные, пример
SELECT catalog_id FROM products GROUP BY catalog_id
# порядок, сперва GROUP BY(группировка), затем ORDER BY(сортировка), только потом LIMIT(лимит)
GROUP_CONCAT(<name>) - показывает содержимое группы, канкатенируя его, если оно сгруппировано
GROUP_CONCAT(<name> SEPARATOR ' ') - указывает какой будет разделитель

HEVING = WHERE, идёт после конструкции GROUP BY
ANY_VALUE = случайное значение
WITH ROLLUP - последняя результирующая строка, с количествоим всех пользователей. NULL во все остальные столбцы

################ СОЗДАНИЕ СВЯЗЕЙ ###################
ALTER TABLE profiles  - изменить таблицу профили
  ADD CONSTRAINT profiles_user_id_fk - добавить ключ
    FOREIGN KEY (user_id) REFERENCES users(id) - для колонки узер_ид, ссылающийся на таблицу юзер, колонку ид
      ON DELETE CASCADE; - в случае если нет - удалить
#     ON DELETE RESTRICT; - не позволит удалить, пока есть связи


При обращении к другой таблице синтаксис такой:
UPDATE <имя в какой таблице> SET <имя столбца> = 