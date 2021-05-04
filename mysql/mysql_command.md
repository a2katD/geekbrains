CREATE DATABASE <name>; - создает БД
SHOW DATABASES; - показывает какие есть БД
SHOW VARIABLES LIKE 'datadir'; - показывает директорию где хранятся БД
DROP DATABASES <name>; - удаляет базу данных

USE <name>; - выбирает базу данных
show tables; - показывает таблицы
create table <name-table>; - создает таблицу
create table if not exists <name-table>; - создает таблицу если еще не существует
describe <name-table> ;- показывает структуру таблицы

CREATE TABLE <name> (id INT(8)); - создает таблицу с инт значение в 8 символов(ведушие пробиелы)
CREATE TABLE <name> (id INT(8) ZEROFILL);  - тоже самое но ведушие нули
CREATE TABLE <name> (id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT);
# создаёт уникальное значение id
# SERIAL == BIGINT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE
CREATE TABLE <name> (id SERIAL PRIMARY KEY); - тоже самое но коротко


INSERT INTO <name> VALUES (5); - помещает в таблицу значение 5
CREATE TABLE <name> (id DECIMAL(7,4)); - точные данные, всего 7, 4 из них после запятой

DROP TABLE <name> - удаляет таблицу, если её нет = ошибка
DROP TABLE IF EXISTS <name> - удаляет таблицу если она существует
TRUCATE <name>; - очищает таблицу

ALTER TABLE <name> CHANGE <id> <id> INT UNSIGNED NOT NULL; - изменяет поле <id> таблицы <name>

DESCRIBE <name>\G - показывает структуру таблицы (\G показывает вертикально)

############## РАБОТА С ДАТАМИ ########################
SELECT '2018-10-01 0:00:00'; - формат вставляемой даты
SELECT '2018-10-01 0:00:00 + INTERVAL 1 DAT'; - добавляет 1 день к указанной дате
SELECT '2018-10-01 0:00:00 + INTERVAL '1-1' YEAR_MONTH'; - добавляет 1 го и 1 месяц
#######################################################
ENUM - одно значение из списка
SET -  комбинаций значений из списка

ALTER TABLE tbl ADD collect JSON; - создает коллекцию JSON
INSERT INTO tbl VALUES (1, '{"first": "HELLO", "second": "WORLD"}');
# добавляет значение в коллекцию
SELECT collect->>"$.first" FROM tbl;
# Обращается по ключу JSON

CREATE INDEX index_of_catalog_id ON products (catalog_id);
# Добавляет ИНДЕКС значаниею каталог_ид в таблице Продукты
DROP INDEX index_of_catalog_id ON products;
#удаляет ИНДЕКС из таблицы Продукты
CREATE INDEX index_of_catalog_id USING BTREE ON products (catalog_id);
# явно требуем использовать ИНДЕКС как бинарное дерево
CREATE INDEX index_of_catalog_id USING HASH ON products (catalog_id);
# явно требуем использовать ИНДЕКС как хеш
