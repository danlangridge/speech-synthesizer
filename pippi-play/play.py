from pippi import dsp
from pippi import tune
import os
import sys

class Voice:
	tones = []
	length = 10
	sound
		
	def generateVoice(segmentLength, tonesList):
		tones = tonesList	
		length = segmentLength

	def addTone(tone):
		tones.add(tone)

	def combineTones():
		for i in tones:
			sound = dsp.interleave(sound, i)
		return		
			
	def output(filename):
		dsp.write(sound, outputfile) 
	

def voiceAttempt2():
	wordLength = 5
	tone1 = dsp.tone(dsp.stf(wordLength), 220, 0.5) 
	tone2 = dsp.tone(dsp.stf(wordLength), 220, 0.5) 
	tone3 = dsp.tone(dsp.stf(wordLength), 220, 0.5) 
	dsp.tone(dsp.stf(wordLength), 220, 0.5) 
	voice1 = Voice(5, [tone1, tone2, tone3]


# Voice attempt 1 (AKA two tones)
def voiceAttempt1(wordLength, frequency, amplitude, outputfile):
	vowelA = dsp.tone(dsp.stf(wordLength), frequency, amplitude) 
	vowelA += dsp.tone(dsp.stf(wordLength), frequency, amplitude) 
	vowelA += dsp.tone(dsp.stf(wordLength), frequency*0.8, amplitude) 
	vowelA = dsp.env(vowelA, 'hann')
        dsp.write(vowelA, outputfile) 

	print type(dsp.tone(dsp.stf(wordLength), frequency*0.8, amplitude)) 
	print type(dsp.env(vowelA, 'hann'))

def output(duration, frequency, amplitude, wave, outputFile):
	out = dsp.tone(dsp.stf(duration), frequency, amplitude)
	out = dsp.env(out, wave)
	dsp.write(out, outputFile)

def main():
	if len(sys.argv) < 3:  
	#	output(5, 220, 0.5, 'hann', 'test')	
		voiceAttempt1(5, 220, 0.5, 'voice')	
	else: 
		#output(sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
		voiceAttempt1(int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), sys.argv[5])


if __name__ == "__main__":
	main() 
