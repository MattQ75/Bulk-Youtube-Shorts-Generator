from tiktok_uploader import upload_video, upload_videos
from tiktok_uploader import AuthBackend

video = "/Users/matteoscarcella/Dropbox/Matteo/python_exp/videos/2.mp4"

# upload_video(video, 
#             description='this is my description', 
#             cookies='cookies.txt')

# Multiple Videos
videos = [
    {
        'path': 'video.mp4', 
        'description': 'this is my description'
    },
    {
        'path': 'video2.mp4', 
        'description': 'this is also my description'
    }
]

auth = AuthBackend(cookies='cookies.txt')
upload_videos(videos=videos, auth=auth)