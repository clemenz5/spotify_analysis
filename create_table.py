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
        CREATE TABLE IF NOT EXISTS spotify_table (
            id INT AUTO_INCREMENT PRIMARY KEY,
            ts TIMESTAMP,
            username VARCHAR(255),
            platform VARCHAR(255),
            ms_played INT,
            conn_country VARCHAR(255),
            ip_addr_decrypted VARCHAR(255),
            user_agent_decrypted VARCHAR(255),
            master_metadata_track_name VARCHAR(255),
            master_metadata_album_artist_name VARCHAR(255),
            master_metadata_album_album_name VARCHAR(255),
            spotify_track_uri VARCHAR(255),
            episode_name VARCHAR(255),
            episode_show_name VARCHAR(255),
            spotify_episode_uri VARCHAR(255),
            reason_start VARCHAR(255),
            reason_end VARCHAR(255),
            shuffle BOOLEAN,
            skipped BOOLEAN,
            offline BOOLEAN,
            offline_timestamp BIGINT,
            incognito_mode BOOLEAN
        );
    '''

cursor.execute(create_table_query)
conn.commit()
print("Table created successfully!")

cursor.close()
conn.close()


