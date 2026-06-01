violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.2],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

song_count = int(input("Сколько песен выбрать? "))
total_duration = 0

for song_number in range(1, song_count + 1):
    song_name = input(f"Название {song_number}-й песни: ")
    for song in violator_songs:
        if song[0] == song_name:
            total_duration += song[1]
            break

print(f"\nОбщее время звучания песен: {total_duration:.2f} минуты")
