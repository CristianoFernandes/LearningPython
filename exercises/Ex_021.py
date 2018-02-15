print('#' * 45)
print('#' * 15, 'Exercício 021', '#' * 15)

from pygame import mixer
import time

mixer.init()

mixer.music.load('music.mp3')
mixer.music.play()
end = mixer.music.get_endevent()

time.sleep(240)

print('#' * 45)
