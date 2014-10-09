from pippi import dsp
import os
import sys


def output( frequency, amplitude, wave, outputFile):
	out = dsp.tone(dsp.stf(5), frequency, amplitude)
	out = dsp.env(out, wave)
	dsp.write(out, outputFile)


def main():
	if len(sys.argv) < 4:  
		output(220, 0.5, 'hann', 'test')	
	else: 
		output(sys.argv[0], sys.argv[1], sys.argv[2]. sys.argv[3])


if __name__ == "__main__":
	main() 
