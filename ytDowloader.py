from pytube import YouTube
import os

def download(video_resolutions, videos):
    while True:
        i = 1
        for resolution in video_resolutions:
            print(f'{i}. {resolution.resolution} \t {resolution.mime_type}')
            i += 1

        choice = int(input('\nSelect a resolution please: '))
        print('---------------------------------------')

        if (choice < i) or (choice >=1):
            resolution_to_download = video_resolutions[choice - 1]
            print(f"\nYou're now downloading the video with resolution {resolution_to_download.resolution}...")

            videos[choice - 1].download(os.path.expanduser('~'))

            print("\nVideo was successfully downloaded!")
            print(f"\nFind your video here: {os.path.expanduser('~')}")
            break

        else:
            print("Invalid choice!!\n\n")


def sort_resolutions(url):
    # URL (user input)
    my_video = YouTube(url)
    print(f'\nVideo Title: {my_video.title}')
    print('---------------------------------------')

    print(f"\nThumbnail URL: {my_video.thumbnail_url}")
    print('---------------------------------------')

    video_resolutions = []
    videos = []

    for stream in my_video.streams.filter(progressive=True).order_by('resolution'):
        video_resolutions.append(stream)
        videos.append(stream)

    return video_resolutions, videos

url = "https://www.youtube.com/watch?v=rJNBGqiBI7s"
url = str(input('\nPaste the URL of the video: '))
video_resolutions, videos = sort_resolutions(url)

download(video_resolutions, videos)
