# Subtitle-Downloader
Python script and executable to download subtitles for movies/tv-series.

Search for subtitles by hash of the file and search by name( if hash search fails).

Suggests movies by sorting them based on IMDb ratings.

Searches for video files recursively in the path provided by user and searches for subtitles in opensubtitles.org.

User has to create his/her own account in opensubtitles.org as api only available for logged users.

Downloads subtitle and changes its name to movie_name.srt and stores it in the movie folder.

Shows names of files whose sub couldn't be found and asks user if they want to continue search by name.

Shows names of file whose sub couldn't be found even after name search.

If sub with same name(as file) exists skips file.

# Usage:
Download sub.py file which can be run on both windows and other os(like linux).

Download sub.exe file for windows os.

Input username and password after creating an account in opensubtitles.org .

Copy adress of path where movies/tv-series are stored and paste in input.

The srt files will be created next to your movie files.

Also input yes/no to see suggestion for movies in path based on imdb rating.

# Development
I would love it if you can contribute to make this project better. Here's how you can do it:

Fork the project.

Commit changes or bugfixes to your repo.

Submit a pull request
