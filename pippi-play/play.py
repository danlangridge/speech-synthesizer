from pippi import dsp
from pippi import tune
import os
import sys




def voiceAttempt1(wordLength, frequency, amplitude, outputfile):
	vowelA = dsp.tone(dsp.stf(wordLength*1/3.0), frequency, amplitude) 
	vowelA += dsp.tone(dsp.stf(wordLength*1/3.0), frequency, amplitude) 
	vowelA += dsp.tone(dsp.stf(wordLength*1/3.0), frequencyi*0.8, amplitude) 
	vowelA = dsp.env(vowelA, 'hann')
        dsp.write(vowelA, outputFile) 


def output(duration, frequency, amplitude, wave, outputFile):
	out = dsp.tone(dsp.stf(duration), frequency, amplitude)
	out = dsp.env(out, wave)
	dsp.write(out, outputFile)

def main():
	if len(sys.argv) < 4:  
		output(5, 220, 0.5, 'hann', 'test')	
	else: 
		output(sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])


if __name__ == "__main__":
	main() 
