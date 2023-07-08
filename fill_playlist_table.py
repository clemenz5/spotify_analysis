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


    for playlist in json_data["playlists"]:
        if playlist is not None and playlist["name"]=="Empfehlungen": 
            for track in playlist["items"]:
                track['addedDate'] = datetime.strptime(track['addedDate'], '%Y-%m-%d').strftime('%Y-%m-%d')
                track["trackName"] = track["track"]["trackName"]
                track["artistName"] = track["track"]["artistName"]
                track["albumName"] = track["track"]["albumName"]
                insert_query = '''
                    INSERT INTO `playlist_empfehlungen` (
                        added_date, track_name, artist_name, album_name
                    ) 
                    VALUES (
                        %(addedDate)s, %(trackName)s, %(artistName)s, %(albumName)s
                    );
                '''
                cursor.execute(insert_query, track)
    conn.commit()
    print("Data inserted successfully!")

        


paths = [
"data/AccountData/Playlist1.json",]
# Example usage

for path in paths:
    insert_data_from_file(path)

cursor.close()
conn.close()