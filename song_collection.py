rock = []
country = []

def collect_songs():
    song = 'Enter a song: '
    ask = 'Type r or c. q to quit: '

    while True:
        genre = input(ask)
        if genre == 'q':
            break

        if genre == 'r':
            rk = input(song)
            rock.append(rk)

        if genre == 'c':
            cy = input(song)
            country.append(cy)

        else:
            print('invalid')

        print(rock)
        print(country)

collect_songs()
