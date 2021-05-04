import os
import glob
from pythonopensubtitles.opensubtitles import OpenSubtitles
from pythonopensubtitles.utils import File
ost = OpenSubtitles() 
ost.login(input('Username:  '), input('Password: '))

# changing type of slash depending on os.name for usability in windows and other operating systems.

if os.name == 'nt':
    s = "\\"            # s is for slash
else:
    s = '/'

nfdict = {}                                             
newlist = []
goodmv1 = []
avgmv1 = []
tmv1 = []

# a function to rename filename from subtitle_id.srt to movie_name.srt

def rename_file(file_root, id_subtitle_file, fname):                
    sub = file_root + s + str(id_subtitle_file) + '.srt'                # changes last 4 letters of extension from .xxx to .srt
    print(sub)
    newsub = file_root + s + fname[1][:-4] + '.srt'
    print(newsub)
    os.rename(sub, newsub)

# this function separates movies based on their imdb rating into 3 lists.

def imdb_rating(gmvlst, avgmvlst, tmvlst, data, fname):
    imdb = float(data[0].get('MovieImdbRating'))
    
    
    if imdb >= 8:
        gmvlst.append(fname[1] + ' :   {}'.format(str(imdb)))
    
    elif 7 < imdb and imdb < 8:
        avgmvlst.append(fname[1] + ' :   {}'.format(str(imdb)))
    
    else:
        tmvlst.append(fname[1] + ' :   {}'.format(str(imdb)))

def downloader(file_list, search):

        for file_path in file_list:

            if search == 'hash':                                        
                fname = os.path.split(file_path)                    # fname stores file name and root directory path in a tuple
                #print('fname', '      ', fname)
                file_root = fname[0]                                             
                print('some more bs', file_root, '\n', file_path)
                f = File(file_path)                                 # File class has methods to get hash and size of file
                data = ost.search_subtitles([{'sublanguageid': 'all', 'moviehash': f.get_hash(), 'moviebytesize': f.size}])     # this method stores multiple subtitle's data in a list in multiple dictionaries using file hash and size.
                                                                                                                                # data stores hash, size ,imdbrating, and much more
            elif search == 'query':
                fname = os.path.split(nfdict[file_path])            
                #print('fname', '      ', fname)
                file_root = fname[0]
                print('some more bs', file_root, '\n', file_path)
                print('file root:  ', file_root)
                data = ost.search_subtitles([{'sublanguageid': 'all', 'query': file_path}])        # uses file name to search for subs and stores sub data in a list.
            
            if data == []:
                print('Could not find sub in opensubtitles.org')    # if sub not found data will be empty
                                                                    # file path and name will be adden to a dict as values and keys 
                if search == 'query':                               # respectively for hash search, and only name to a list for name search
                    newlist.append(fname[1])
                
                elif search == 'hash':
                    nfdict[fname[1]] = file_path
                
                continue
            
            else:
                id_subtitle_file = data[0].get('IDSubtitleFile')    # gets sub id (a 6 digit num)
                #print(data)
                imdb_rating(goodmv1, avgmv1, tmv1, data, fname)
                newsub = file_root + s + fname[1][:-4] + '.srt'     # a string with the name of the final sub file
                                                                    # used below to check if file already exists.
                if os.path.exists(newsub):
                    print("sub for this exists so i don't think downloading it again will do shit....")
                    continue
                
                else:                                               # downloads subtitles using sub id from data and stores sub in output dir.
                    ost.download_subtitles([id_subtitle_file], output_directory=file_root, extension='srt')
                    sub = file_root + s + str(id_subtitle_file) + '.srt'
                    
                    if os.path.exists(sub) == False:                # debugging to check if download failed
                        print("Probably subtitle downloading limit reached(for the account).")

                    try:
                        rename_file(file_root, id_subtitle_file, fname)
                        
                    except FileExistsError:
                        print('file exists so deleting the newly made file')
                        os.remove(sub)

def get_subtitles(movie_folder):
    
    # file_list stores the file paths of all *.xxx extensions by searching recursively in given directory using glob module

    file_list = list(glob.iglob(movie_folder + s + "**" + s + "*.mp4",recursive = True)) + list(glob.iglob(movie_folder + s + "**" + s + "*.mkv",recursive = True)) + list(glob.iglob(movie_folder + s + "**" + s + "*.flv",recursive = True))
    print(file_list)
    
    downloader(file_list, 'hash')           

    if list(nfdict.keys()) == []:
        print('\n\n\nsubtitles for all files were found....\n\n')
    
    else:
        print('\n\n\nsub for these files could not be found: ')
        print(list(nfdict.keys()), '\n\n')

    if input("well.... if u r that desperate for subs i could try to search them by name \nbut its not as accurate...., still wanna continue?? Y/N : ")[0].lower() == 'y':
        downloader(list(nfdict.keys()), 'query')                        # search by name

    if newlist == []:
        print('\n\n\nsubtitles for all files were found....\n\n') 
    
    else:
        print('\n\n\nthese are hopeless cases search on ur own: ')
        print(newlist, '\n\n')

    if input("want movie suggestion?? Y/N : ")[0].lower() == 'y':
        print('\nThese are some good movies with imdb rating > 8: \n\n')
        print(*goodmv1, sep = '\n')
        print('\nThese are some watchable movies with imdb rating 7-8: \n\n')
        print(*avgmv1, sep = '\n')
        print('\nThese are some avg/below-avg movies (according to imdb not me) rating < 7: \n\n')
        print(*tmv1, sep = '\n')
        
get_subtitles(input('path of the movie folder: '))


input("\nMade By: bibhu901 TM .... \nPress Enter to exit")


























'''for movie in nfdict:
            fname = os.path.split(movie)
            file_root = fname[0]


            data = ost.search_subtitles([{'sublanguageid': 'all', 'query': movie}])
            if data == []:
                continue
            else:

                id_subtitle_file = data[0].get('IDSubtitleFile')
                imdb_rating(goodmv1, avgmv1, tmv1)
                newsub = file_root + s + fname[1][:-4] + '.srt'
                if os.path.exists(newsub):
                    print("sub for this exists so i don't think downloading it again will do shit....")
                    continue
                else:
                    ost.download_subtitles([id_subtitle_file], output_directory=file_root, extension='srt')
                    rename_file()'''