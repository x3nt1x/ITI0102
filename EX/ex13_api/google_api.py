"""Google API."""
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


def get_links_from_spreadsheet(id: str, token: str) -> list:
    """
    Return a list of strings from the first column of a Google Spreadsheet with the given ID.

    Example input with https://docs.google.com/spreadsheets/d/1WrCzu4p5lFwPljqZ6tMQEJb2vSJQSGjyMsqcYt-yS4M
    get_links_from_spreadsheet('1WrCzu4p5lFwPljqZ6tMQEJb2vSJQSGjyMsqcYt-yS4M', 'token.json')

    Returns ['https://www.youtube.com/playlist?list=PLPszdKAlKCXUhU3r25SOFgBxwCEr-JHVS', ... and so on]
    """
    scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    creds = None

    if os.path.exists(token):
        creds = Credentials.from_authorized_user_file(token, scopes)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            creds = InstalledAppFlow.from_client_secrets_file('credentials.json', scopes).run_local_server(port=0)

        with open(token, 'w') as file:
            file.write(creds.to_json())

    service = build('sheets', 'v4', credentials=creds)

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=id, range='Songs!A:A').execute()
    values = result.get('values')

    return [row[0] for row in values]


def get_links_from_playlist(link: str, developer_key: str) -> list:
    """
    Return a list of links to songs in the Youtube playlist with the given address.

    Example input
    get_links_from_playlist('https://www.youtube.com/playlist?list=PLFt_AvWsXl0ehjAfLFsp1PGaatzAwo0uK', 'Key')

    Returns ['https://youtube.com/watch?v=r_It_X7v-1E', 'https://youtube.com/watch?v=U4ogK0MIzqk', ... and so on]
    """
    data = list()

    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    youtube = build("youtube", "v3", developerKey=developer_key)

    request = youtube.playlistItems().list(part="snippet", playlistId=link.split("list=")[1])

    while request:
        response = request.execute()

        for playlist_item in response["items"]:
            video_id = playlist_item["snippet"]["resourceId"]["videoId"]
            data.append(f"https://youtube.com/watch?v={video_id}")

        request = youtube.playlistItems().list_next(request, response)

    return data
