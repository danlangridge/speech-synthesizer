from pippi import dsp
from pippi import tune
import os
import sys



# Voice attempt 1 (AKA two tones)
def voiceAttempt1(wordLength, frequency, amplitude, symbolLength, outputfile):
	vowelA = dsp.tone(dsp.stf(wordLength*1/symbolLength), frequency, amplitude) 
	vowelA += dsp.tone(dsp.stf(wordLength*1/symbolLength), frequency, amplitude) 
	vowelA += dsp.tone(dsp.stf(wordLength*1/symbolLength), frequency*0.8, amplitude) 
	vowelA = dsp.env(vowelA, 'hann')
        dsp.write(vowelA, outputfile) 


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
		voiceAttempt1(int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), sys.argv[5])


if __name__ == "__main__":
	main() 
