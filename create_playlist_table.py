import json
import pymysql

conn = pymysql.connect(
        host="localhost",
        port=3306,
        database="spotify",
        user="root",
        password="root"
    )
cursor = conn.cursor()

create_table_query = '''
        CREATE TABLE IF NOT EXISTS playlist_empfehlungen (
            id INT AUTO_INCREMENT PRIMARY KEY,
            added_date TIMESTAMP,
            track_name VARCHAR(255),
            artist_name VARCHAR(255),
            album_name VARCHAR(255)
        );
    '''

cursor.execute(create_table_query)
conn.commit()
print("Table created successfully!")

cursor.close()
conn.close()


