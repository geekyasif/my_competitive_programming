# import youtube_downloader
# import file_converter
import pytube

# functions for downloading urls from main.py


def download_playlist(url, resolution):
    playlist = pytube.Playlist(url)
    download_videos(playlist.video_urls, resolution)


def download_videos(urls, resolution):
    for url in urls:
        download_videos(url, resolution)


# function for downloading single videos


def download_video(url, resolution):
    itag = choose_resolution(resolution)
    video = pytube.YouTube(url)
    stream = video.streams.get_by_itag(itag)
    stream.download()
    return stream.default_filename

# defining a function for choose resolution


def choose_resolution(resolution):
    if resolution in ['low', '360', '360p']:
        itag = 18
    elif resolution in ['medium', '720', '720p', 'hd']:
        itag = 22
    elif resolution in ['high', '1080', '1080p', 'fullhd', 'full_hd', "full hd"]:
        itag = 137
    elif resolution in ['very high', '2160', '2160p', '4k', '4k']:
        itag = 313
    else:
        itag = 18
    return itag



def input_links():
    print("Enter the links of the videos (end by entering 'STOP') : ")

    links = []
    link = ""

    while link != "STOP" and link != "STOP":
        link = input()
        links.append(link)

    links.pop()

    return links

if __name__ == '__main__':
    print("Welcome to WebDevCode Youtube Downloader and Converter")

    print('''
    What do you want ?
    
    (1) Download Youtube Videos Manually
    (2) Download A Youtube Playlist
    (3) Download Youtube Videos And Convert Into MP3
    
    Downloading copyright youtube videos is illegal!
    I am not responsible for your downloads! Go at your own risks!
    
    Copyright (c) WeDevCode 2021
    ''')

    choice = input("Enter your choice: ")

    if choice == '1' or choice == '2':

        quality = input("Please choose a quality (low, medium, high, very height): ")

        if choice == '2':
            link = input("Enter the link to the playlist: ")
            print("Downloading playlist...")
            download_playlist(link, quality)
            print("Download Finished!")

        if choice == '1':
            links = input_links()
            for link in links:
                download_video(link, quality)

    elif choice == '3':

        links = input_links()

        for link in links:
            print("Downloading...")
            filename = download_video(link, 'low')
            print("Converting....")
            # file_converter.convert_to_mp3(filename)
    else:
        print("Invalid Input! Terminating....")
