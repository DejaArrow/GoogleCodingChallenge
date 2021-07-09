"""A video player class."""

from os import truncate
from src import video, video_playlist
from .video_library import VideoLibrary
from src import video_library
import random

class VideoPlayerError(Exception):
    pass



class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.is_playing = False
        self.video_playing_id = "None"
        self.is_paused = False
    
    def Video_Name(self, video_id):
        video = self._video_library.get_video(video_id)
        return video.title

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        print("Here's a list of all available videos:")
        available_videos = self._video_library.get_all_videos()
        available_videos.sort(key=lambda video: video.title)
                    
        for item in available_videos:
            
            print (f"{item.title}, ({item.video_id}), {item.tags}")


    def play_video(self, video_id):
    
        
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        video = self._video_library.get_video(video_id)

        try:
            temp = video.title
            if self.is_playing == False:
                print(f"Playing Video: {video.title}")
                self.is_playing = True
                self.is_paused = False
                self.video_playing_id = video_id

            else:
                print(f"Stopping video: {self.Video_Name(self.video_playing_id)}")
                print(f"Playing Video: {video.title}")
                self.video_playing_id = video_id
                self.is_playing = False
               
        except:
            print("Cannot play video: Video does not exist")

            
            

      

    def stop_video(self):
        """Stops the current video."""

        
        if self.is_playing == True:
            print(f"Stopping video: {self.Video_Name(self.video_playing_id)}")
            self.is_playing = False
        else:
            print(f"Cannot stop video: No video is currently playing.")

    def play_random_video(self):
        """Plays a random video from the video library."""

        videos = self._video_library.get_all_videos()

        random_video = videos[ random.randint(0, len(videos) -1) ]
        self.play_video(random_video._video_id)

    def pause_video(self):
        """Pauses the current video."""

        if self.is_paused == False and self.video_playing_id != "None":
            print(f"Pausing video:{self.Video_Name(self.video_playing_id)}")
            self.is_paused = True
        elif self.is_paused == True and self.video_playing_id != "None":
            print(f"Video already paused: {self.Video_Name(self.video_playing_id)}")
        else:
            print("Cannot pause video: No video is currently playing")

        

    def continue_video(self):
        """Resumes playing the current video."""

        if self.is_paused == False: 
            print("Cannot continue video: Video is not paused")
        elif self.video_playing_id  == "None":
            print("Cannot continue video: No video is currently playing")
        else:
            print(f"Continuing video: {self.Video_Name(self.video_playing_id)}")

    def show_playing(self):
        """Displays video currently playing."""

        if self.video_playing_id != "None":
            print(f"Currently playing: {self.Video_Name(self.video_playing_id)}")
        elif self.is_paused == True:
            print(f"Currently playing: {self.Video_Name(self.video_playing_id)} - PAUSED")
        else:
            print("No video is currently playing")
            

       

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
