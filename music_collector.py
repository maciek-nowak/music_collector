def init_database(music):
    """This function reads a file music.csv and creates database in form of dictionary"""

    datafile = open('music.csv')   # reading data from csv file
    database = datafile.readlines()
    datafile.close()

    database_list = [line.split(' | ') for line in database]
    # changing string data into list of tuples
    music = [((line[0], line[1]), (int(line[2]), line[3], line[4])) for line in database_list]
    return music


def add_new_album(music):
    """This function asks user for data of new album and extends database dictionary.
        New data is being saved in music.csv file"""

    print('\033[0m' + 'You are entering new album information!')
    new_data = ['', '', '', '', '']
    new_data[0] = input("Type the artist name: " + '\033[32m')
    new_data[1] = input('\033[0m' + 'Type album name: ' + '\033[32m')
    while new_data[2].isdigit() is False:  # asks about year until gets numeric data
        new_data[2] = input('\033[0m' + 'Type the album release year [e.g. 1987]: ' + '\033[32m')
    new_data[3] = input('\033[0m' + 'Type the album genre [e.g. pop]: ' + '\033[32m')
    proper_length_input = False
    while proper_length_input is False:  # asks about album length until gets data in format mm:ss
        proper_length_input = True
        new_data[4] = input('\033[0m' + 'Type the album length[mm:ss eg. 45:25]: ' + '\033[32m')
        if new_data[4].count(':') != 1:
            proper_length_input = False
        if any(char not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':'] for char in new_data[4]):
            proper_length_input = False
        if len(new_data[4]) >= 4:
            if new_data[4][-3] != ':':
                proper_length_input = False
            if new_data[4][-2] not in ['0', '1', '2', '3', '4', '5']:
                proper_length_input = False
        else:
            proper_length_input = False

    new_data[4] += '\n'  # adds enter athe line end
    accept_text = 'Are you sure you want to save the data? [Type "yes" to save or data will be discarded]: '
    accept = (input('\033[0m' + accept_text + '\033[32m')).lower()
    if accept == 'yes':
        line_to_save = ' | '.join(new_data)  # preparing string to append to database file
        # preparing new tuple for music list
        new_data = ((new_data[0], new_data[1]), (int(new_data[2]), new_data[3], new_data[4]))
        music.append(new_data)  # adding new definition to music list

        datafile = open('music.csv', 'a')  # writing new data to the csv file
        datafile.write(line_to_save)
        datafile.close()
    else:
        print('\033[31m' + 'Recent data has been discarded!')

    return music


def print_album(album):
    """Prints all given album data"""

    print('Artist: ', album[0][0])
    print('Album name: ', album[0][1])
    print('Year of release: ', album[1][0])
    print('Genre: ', album[1][1])
    print('Length: ', album[1][2])


def find_musician_by_album(music):
    """searching through database for artist of given album"""

    print('\033[0m' + "Choose the album name: ")
    chosen_album = input('Your choice: ' + '\033[32m').lower()
    print()
    any_match = False
    for entry in music:
        if entry[0][1].lower() == chosen_album:
            print('\033[0m', entry[0][1], 'is album of', entry[0][0])
            any_match = True
    if any_match is False:
        print('\033[31m' + 'There is no such album in our database!' + '\033[0m')


def find_album_by_genre(music):
    """searching through database for albums of given genre"""

    print('\033[0m' + "Choose the genre of album:")
    chosen_genre = input('Your choice: ' + '\033[32m').lower()
    print()
    any_match = False
    for entry in music:
        if entry[1][1].lower() == chosen_genre:
            print_album(entry)
            any_match = True
    if any_match is False:
        print('\033[31m' + 'There is no album of chosen genre in our database!' + '\033[0m')


def find_album_by_musician(music):
    """searching through database for albums of given artist"""

    print('\033[0m' + "Choose the artist name: ")
    chosen_band = input('Your choice: ' + '\033[32m').lower()
    print()
    any_match = False
    for entry in music:
        if entry[0][0].lower() == chosen_band:
            print_album(entry)
            any_match = True
    if any_match is False:
        print('\033[31m' + 'There is no album of this band in our database!' + '\033[0m')


def find_album_by_letter(music):
    """searching through database for albums containing given phrase"""

    print('\033[0m' + "Type single letter or part of the album name: ")
    chosen_letter = input('Your choice: ' + '\033[32m').lower()
    print()
    any_match = False
    for entry in music:
        if chosen_letter in entry[0][1].lower():
            print_album(entry)
            any_match = True
    if any_match is False:
        print('\033[31m' + 'There is no album containing the chosen string!' + '\033[0m')


def find_album_by_year(music):
    """searching through database for albums released in given year"""

    chosen_year = ''
    while chosen_year.isdigit() is False:   # asks about year until gets numeric data
        print('\033[0m' + "Choose the album year of release:")
        chosen_year = input('Your choice: ' + '\033[32m')
        print()
    any_match = False
    for entry in music:
        if entry[1][0] == int(chosen_year):
            print_album(entry)
            any_match = True
    if any_match is False:
        print('\033[31m' + 'There is no album released that year in our database!' + '\033[0m')


def count_artist_albums(music):
    """searching through database and counting albums of given artist"""

    print('\033[0m' + "Choose the musician's or band name:")
    chosen_band = input('Your choice: ' + '\033[32m').lower()
    print()
    count = 0
    for entry in music:
        if entry[0][0].lower() == chosen_band:
            count += 1
    print('\033[32m' + 'There are', count, 'albums of this artist in our database!' + '\033[0m')


def print_albums_age(music):
    """gives information about age of every album in database"""

    import datetime
    now = datetime.datetime.now().year  # takes current date
    print()
    for entry in music:
        print()
        print_album(entry)
        age = now - entry[1][0]
        print('Album age:', age, 'years')
        if age < 0:
            print('Wow, this album is from the future!')    # if album release year is higher than current year


def choose_random_album_by_genre(music):
    """chooses randomly and prints album of given genre"""

    from random import randint
    chosen_genre_list = []
    print('\033[0m' + "Choose the genre of album: ")
    chosen_genre = input('Your choice: ' + '\033[32m').lower()
    print()
    any_match = False
    for entry in music:
        if entry[1][1].lower() == chosen_genre:
            chosen_genre_list.append(entry)
            any_match = True
    if any_match is False:
        print('\033[31m' + 'There is no album of chosen genre in our database!' + '\033[0m')
    else:
        print_album(chosen_genre_list[randint(0, len(chosen_genre_list)-1)])


def find_longest_album(music):
    """searching through database for longest album"""

    longest_album = music[0]
    for entry in music:
        time_longest_list = longest_album[1][2].split(':')  # changes string into pair of integers
        time_longest = int(time_longest_list[0]) * 60 + int(time_longest_list[1])  # calculating duration in seconds
        time_entry_list = entry[1][2].split(':')    # changes string into pair of integers
        time_entry = int(time_entry_list[0]) * 60 + int(time_entry_list[1])  # calculating duration in seconds
        if time_longest < time_entry:
            longest_album = entry
    print_album(longest_album)


def main(music):
    """base part of program, asks user to choose task"""

    user_option = ''
    music = init_database(music)
    menu = '\033[33m' + """
        Welcome in the CoolMusic! Choose the action:
         1) Add new album
         2) Find albums by musician
         3) Find albums by year
         4) Find musician by album
         5) Find albums by letter
         6) Find albums by genre
         7) Calculate the age of all albums
         8) Choose random album by genre
         9) Show the amount of albums by artist
        10) Find the longest album
         0) Exit""" + '\033[0m'
    print(chr(27) + "[2J")  # clear terminal screen
    while user_option != '0':   # main loop asking user for option until '0' is entered
        print(menu)
        user_option = input('\033[0m' + 'Choose option from list above [0 - 10]: ' + '\033[32m')
        print('\033[0m')
        if user_option == '1':
            music = add_new_album(music)
        elif user_option == '2':
            find_album_by_musician(music)
        elif user_option == '3':
            find_album_by_year(music)
        elif user_option == '4':
            find_musician_by_album(music)
        elif user_option == '5':
            find_album_by_letter(music)
        elif user_option == '6':
            find_album_by_genre(music)
        elif user_option == '7':
            print_albums_age(music)
        elif user_option == '8':
            choose_random_album_by_genre(music)
        elif user_option == '9':
            count_artist_albums(music)
        elif user_option == '10':
            find_longest_album(music)
        elif user_option == '0':
            print('\033[33m' + 'Thank you for using CoolMusic! See you next time.' + '\033[0m')
        else:
            print('\033[31m' + "Can't find chosen option!" + '\033[0m')


music = []  # main database
main(music)
