# YouSpo

YouSpo is an application that allows you to automatically copy songs from Spotify playlist to YouTube playlist.

## Table of Contents

* [Installation](#installation)
* [Requirements](#requirements)
* [Credentials](#credentials)
* [Usage](#usage)

## Installation

Download the application using the command below:

`git clone https://github.com/karolkisinski/YouPo.git`

Then go to the next section.


## Requirements

Python 3.* and the following modules are required to run the application:

* spotipy
* python-dotenv
* google-auth-oauthlib
* google-api-python-client

Install modules using pip:

```sh
pip install module_name
```

## Credentials

The application requires the use of the Spotify and Youtube API.

#### Spotify

To use the Spotify API, go to [Dashboard](https://developer.spotify.com/dashboard) and log in. Then create a new application.

In the next step, go to `Edit settings` and add `Redirect URIs`, in this case it will be:

`http://localhost:8080`

Then create an .env file (in Linux shell `nano .env` ) in the directory with the downloaded application and place the following data in it:

```sh
SPOTIPY_CLIENT_ID = "your_spotify_client_id"
SPOTIPY_CLIENT_SECRET = "your_spotify_client_secret"
```

### YouTube

To use the Spotify API, go to [Google Console](https://console.cloud.google.com) and create a new project.

Then navigate to `Credentials` and `Create Credentials`.
Choose OAuth client ID. Choose `Desktop app` and click `Create`.
After that, just click `Download JSON`, rename file to `credentials.json` and put it in the directory with the downloaded application.

After that, navigate to OAuth consent screen and choose Add users. Use the email, that is assignated with your YouTube account, which you want to use (which is connected with playlist you want to use).

## Usage

If the above requirements are met, complete the following data in the application code (YouSpo.py):

```sh
spotify_username = "your_spotify_username"
yt_playlistid = "youtube_playlist_id"
spotify_playlistid = "spotify_playlist_id"
```

Then run the application from the console:

```sh
python3 YouSpo.py
```

Then go to the generated link and copy the authorization code. 
Paste it in the console and press Enter.

Here is a [video](https://youtu.be/4dhAyLSJiJ4) that shows how to download, configure and use this application:




