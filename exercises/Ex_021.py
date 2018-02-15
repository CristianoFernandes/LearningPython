print('#' * 45)
print('#' * 15, 'Exercício 021', '#' * 15)

from pygame import mixer
import time

mixer.init()
mixer.music.load('music.mp3')
print('Playing music...')
mixer.music.play()
time.sleep(60)

print('#' * 45)
