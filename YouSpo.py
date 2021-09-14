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
<<<<<<< HEAD
	                  'playlistId': yt_playlistid, 
	                  'playlistId': 'youtube_playlist_id', 
=======
	                  'playlistId': 'PL8b3Q6hDVVosmy4O2yvbk6UQeA5nYjfof', 
>>>>>>> parent of ab5e538... Added check_duplicate function
	                  'resourceId': {
	                          'kind': 'youtube#video',
	                      'videoId': search_video(id)
	                    }
	                  }     
	          }
	    )
	response = request.execute()
	print("Added " + song_name + " to playlist")

def main(username, pl_id):
	results = sp.user_playlist_tracks(username, pl_id)
	for id, item in enumerate(results['items']):
		track = item['track']
		# print(id, track['artists'][0]['name'], " - ", track['name'])
		vid = [track['artists'][0]['name'], " - ", track['name']]
		song_to_search = ''.join(str(e) for e in vid)
		song_to_add= song_to_search.encode('ascii', 'ignore').decode('ascii').replace(" ", "+")
		add_video(song_to_search, song_to_add)

<<<<<<< HEAD
if __name__ == "__main__":
	main('spotify_username', spotify_playlistid)
	

=======

main('karol.kisinski', "37i9dQZF1DWWRktbhJiuqL")
>>>>>>> parent of ab5e538... Added check_duplicate function
