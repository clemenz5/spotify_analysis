import json
import pymysql
import os
from datetime import datetime

conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        database="spotify"
    )
cursor = conn.cursor()

# Function to insert JSON objects into the table
def insert_data_from_file(file_path):
    

    with open(file_path, 'r') as file:
        json_data = json.load(file)

    for obj in json_data:
        if obj is not None: 
            obj['ts'] = datetime.strptime(obj['ts'], '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d %H:%M:%S')
            album_name = obj.get('master_metadata_album_album_name')
            if album_name is not None:
                album_name = album_name[:255]
            else:
                album_name = 'None'

            # Update the 'master_metadata_album_album_name' value in the object
            obj['master_metadata_album_album_name'] = album_name

            insert_query = '''
                INSERT INTO `spotify_table` (
                    ts, username, platform, ms_played, conn_country, 
                    ip_addr_decrypted, user_agent_decrypted, master_metadata_track_name, 
                    master_metadata_album_artist_name, master_metadata_album_album_name, 
                    spotify_track_uri, episode_name, episode_show_name, spotify_episode_uri, 
                    reason_start, reason_end, shuffle, skipped, offline, 
                    offline_timestamp, incognito_mode
                ) 
                VALUES (
                    %(ts)s, %(username)s, %(platform)s, %(ms_played)s, %(conn_country)s, 
                    %(ip_addr_decrypted)s, %(user_agent_decrypted)s, %(master_metadata_track_name)s, 
                    %(master_metadata_album_artist_name)s, %(master_metadata_album_album_name)s, 
                    %(spotify_track_uri)s, %(episode_name)s, %(episode_show_name)s, %(spotify_episode_uri)s, 
                    %(reason_start)s, %(reason_end)s, %(shuffle)s, %(skipped)s, %(offline)s, 
                    %(offline_timestamp)s, %(incognito_mode)s
                );
            '''
            cursor.execute(insert_query, obj)
    conn.commit()
    print("Data inserted successfully!")

        


paths = [
"data/Streaming_History_Audio_2015-2016_0.json",
"data/Streaming_History_Audio_2016-2017_1.json",
"data/Streaming_History_Audio_2017-2018_2.json",
"data/Streaming_History_Audio_2018-2019_3.json",
"data/Streaming_History_Audio_2019_4.json",
"data/Streaming_History_Audio_2019-2020_5.json",
"data/Streaming_History_Audio_2020_6.json",
"data/Streaming_History_Audio_2020-2021_7.json",
"data/Streaming_History_Audio_2021_8.json",
"data/Streaming_History_Audio_2021_9.json",
"data/Streaming_History_Audio_2021-2022_10.json",
"data/Streaming_History_Audio_2022_11.json",
"data/Streaming_History_Audio_2022_12.json",
"data/Streaming_History_Audio_2022-2023_13.json"]
# Example usage

for path in paths:
    insert_data_from_file(path)

cursor.close()
conn.close()