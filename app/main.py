import psycopg2

conn = psycopg2.connect(
    dbname="yakovlev",
    user="username",
    password="secret",
    host="db",
    port="5432"
)
cur = conn.cursor()

def get_max_age_for_short_names(length):
    cur.execute("""SELECT MAX(age) FROM test_table WHERE length(name) < %s""", (length,))
    result = cur.fetchone()
    return result[0] if result else None
def get_min_age_for_short_names(length):
    cur.execute("""SELECT MIN(age) FROM test_table WHERE length(name) < %s""", (length,))
    result = cur.fetchone()
    return result[0] if result else None


if __name__ == '__main__':
    length = 6
    max = get_max_age_for_short_names(length)
    print(f"Максимальный возраст для имен, длина которых меньше {length} символов, равняется: {max}")
    min = get_min_age_for_short_names(length)
    print(f"Минимальный возраст для имен, длина которых меньше {length} символов: {min}")
