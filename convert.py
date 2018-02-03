import sys

def sql_utf8():
    print("SET NAMES 'utf8';")

def sql_person(cells):
    sql = "INSERT INTO person (id, passport_number, first_name, last_name, nationality, male) " \
                    "VALUES ({}, {}, {}, {}, {}, {}) " \
                    "ON DUPLICATE KEY UPDATE passport_number = {}, first_name = {}, last_name = {}, nationality = {}, male = {};"
    print(sql.format(
        cells[0],
        cells[0],
        cells[1],
        cells[2],
        cells[3],
        cells[4],
        cells[0],
        cells[1],
        cells[2],
        cells[3],
        cells[4])
    )

def sql_person_role(cells):
    sql = "INSERT IGNORE INTO person_x_role (person_id, roles) VALUES ({}, 'FIGHTER');"
    print(sql.format(cells[0]))

with open(sys.argv[1], 'r', encoding='utf-8') as f:
    for cnt, line in enumerate(f):
        cells = line.split(";");
        cells = list(map(lambda x: x.replace("\"", "'"), cells))
        sql_utf8();
        sql_person(cells)
        sql_person_role(cells)


