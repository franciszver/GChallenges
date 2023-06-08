import base64
from itertools import cycle

message=b'GE4AFgwHAhAaVENVREAEGxYCG0NLQ04QDAMIAgIOBgZIRF1DThYQGwECDgwXRENEQAYPFQwdEBRE\nSUlDSA0JABsWBwYGCwZOX0NIBQQLABYVCgkCDR1UQ1VEQBYHHwwMDwIHTl9DSBYGAQsaFxxDR1lJ\nVBAOAgJERVNECQsIRElJQ0gTDg1IVB4='
key = bytes('franciszver', 'utf-8')
print(bytes(a ^ b for a, b in zip(base64.b64decode(message), cycle(key))))
