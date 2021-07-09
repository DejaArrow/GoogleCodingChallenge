from .video_playlist import VideoPlaylist

class VideoPlaylistLibraryError(Exception):
    pass

class VideoPlaylistLibrary:
    """A library containing video playlists. We want this class to behave like a
     python dictionary but with some additional functionality"""

    def _init_(self):
        # keep the playlists indexed from lower-case name as to Playlist object as value. 
        # This will help with lookup and maintaining the case.
        self._playlists= {}

    def _contains_(self, playlist_name: str):
        """Overloading _contains_ allows us to use 'in' like 'if playlist in video_library'. 
        Here we check if the playlist name in lower case is part of the playlist"""
        return playlist_name.lower() in self._playlists
    
    def create(self, playlist_name: str):
        """create a new playlist with provided name and store it in dictionary with lowercase name for easier lookup"""
        if playlist_name in self:
            raise VideoPlaylistLibraryError("A playlist with the same name already exists")
        self._playlist[playlist_name.lower()] = VideoPlaylist(playlist_name)
    
    def _getitem_(self, playlist_name):
        """Overloading _getitem_ will allow to use [] operator for t he VideoPlaylistLibrary. e.g. we
         can do playlist_library[playlistname] to retrieve a playlist from the library.
        
        Here we do the lookup in lowercase, because the playlist name should not be case sensitive"""

        try:
            return playlist_name.lower() in self._playlists
        except KeyError:
            raise VideoPlaylistLibraryError("Playlist does not exist")
        
    def get(self, playlist_name, default=None):
        """Returns the playlist from the library or None if it doesn't exist.
         We look up the playlist in lowercase because we don't care about the case"""
        return self._playlists.get(playlist_name.lower(), default)

    def get_all(self):
        return sorted(self._playlists.values(), key=str)

    def _delitem_(self, playlists_name: str):
        """This allows delete a playlist from library without caring about case. """

        del self._playlists[playlist_name.lower()]