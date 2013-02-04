# Example from Pi Educational Manual v1.0 P. 98
# Provided under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License

import numpy
import wave
import pygame
# sample rate of a WAV file
SAMPLERATE = 44100 # Hz
def createSignal(frequency, duration):
    samples = int(duration*SAMPLERATE)
    period = SAMPLERATE / frequency # in sample points
    omega = numpy.pi * 2 / period
    xaxis = numpy.arange(samples, dtype=numpy.float) * omega
    yaxis = 16384 * numpy.sin(xaxis)
        # 16384 is maximum amplitude (volume)
    return yaxis.astype('int16').tostring()
def createWAVFile(filename, signal):
    file = wave.open(filename, 'wb')
    file.setparams((1, 2, SAMPLERATE, len(signal), 'NONE', 'noncompressed'))
    file.writeframes(signal)
    file.close()
def playWAVFile(filename):
    pygame.mixer.init()
    sound = pygame.mixer.Sound(filename)
    sound.play()

    # wait for sound to stop playing
    while pygame.mixer.get _ busy():
        pass

# main program starts here
filename = '/tmp/440hz.wav'
signal = createSignal(frequency=440, duration=4)
createWAVFile(filename, signal)
playWAVFile(filename)
