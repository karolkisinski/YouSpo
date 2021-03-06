import spotipy
import os
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
import urllib.request
import re
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

# -*- coding: utf-8 -*-

load_dotenv()
os.environ['SPOTIPY_CLIENT_ID'] = os.getenv('SPOTIPY_CLIENT_ID')
os.environ['SPOTIPY_CLIENT_SECRET'] = os.getenv('SPOTIPY_CLIENT_SECRET')
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://localhost:8080'

# spotify scopes
scope = "playlist-modify playlist-read"
# youtube scopes
scopes = ["https://www.googleapis.com/auth/youtube"]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

api_service_name = "youtube"
api_version = "v3"
client_secrets_file = "credentials.json"

spotify_username = ""
yt_playlistid = ""
spotify_playlistid = ""

flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
credentials = flow.run_console()
youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

def search_video(name):
	html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+name)
	video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
	return video_ids[0]

	
def add_video(song_name, id):
	request = youtube.playlistItems().insert(
	        part="snippet",
	        body={
	        'snippet': {
	                  'playlistId': yt_playlistid, 
	                  'resourceId': {
	                  'kind': 'youtube#video',
	                  'videoId': id
	                    }
	                  }     
	          }
	    )
	response = request.execute()
	print("Added " + song_name + " to playlist")

def check_duplicate(id):
    request = youtube.playlistItems().list(
        	part="snippet",
        	playlistId=yt_playlistid,
        	videoId=id
    )
    response = request.execute()

    return(response['pageInfo']['totalResults'])


def main(username, pl_id):
	results = sp.user_playlist_tracks(username, pl_id)
	for id, item in enumerate(results['items']):
		track = item['track']
		vid = [track['artists'][0]['name'], " - ", track['name']]
		song_to_search = ''.join(str(e) for e in vid)
		song_to_add= search_video(song_to_search.encode('ascii', 'ignore').decode('ascii').replace(" ", "+"))
		if(check_duplicate(song_to_add)>0):
			print(song_to_search + " is already in this playlist!")
		else:
			add_video(song_to_search, song_to_add)



if __name__ == "__main__":
	main(spotify_username, spotify_playlistid)
	