
songs, melody_avg = map(int, input().split())

# ceil(melody_total/songs) = melody_avg
# melody_avg-1 <(melody_total/songs) <= melody_avg

melody_total = (melody_avg-1)*songs + 1

print(melody_total)