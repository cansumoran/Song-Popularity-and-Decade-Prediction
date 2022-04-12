from musixmatch import Musixmatch
import pandas as pd
musixmatch = Musixmatch('2eef3dcabd0f3f0708cc609767a0acc0')

df = pd.read_csv("df3_eng.csv") #change to the csv file with the song list to be retrieved
c = 0  # Counter
period = {60 : 0, 70 : 0, 80 : 0, 90 : 0, 0 : 0, 10 : 0}
df_new = pd.DataFrame()
pd.set_option('display.max_colwidth', None)

for index, row in df.iterrows():
    artist = row["artists"].split("'")[1]
    title = row["name"]
    try:
        song = musixmatch.matcher_lyrics_get(title, artist)
        lyrics = song['message']['body']['lyrics']['lyrics_body']
        lyrics = lyrics.replace("******* This Lyrics is NOT for Commercial use *******", "")
        #print(lyrics)
        new_row = row
        new_row["lyrics"] = lyrics
        df_new = df_new.append(new_row)
        c += 1
        period[row["period"]] += 1
        print("Song grabbed:", title, artist)
        print(period)
    except :
        print("some exception at ", title, artist)

print(period)
df_new.to_csv('musicxmatch.csv', mode='w')