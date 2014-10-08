from pippi import dsp

out = dsp.tone(dsp.stf(5), freq=220, amp=0.2)
out = dsp.env(out, 'hann')
dsp.write(out, 'test')
