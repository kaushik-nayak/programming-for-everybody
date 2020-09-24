text = "X-DSPAM-Confidence:    0.8475"
p=text.find('0')
a=text[p:]
print(float(a))
