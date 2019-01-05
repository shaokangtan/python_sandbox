print ((256).to_bytes(4, byteorder='big'))
print ((256).to_bytes(4, byteorder='little'))
import sys
sys.byteorder

#https://docs.python.org/2/library/struct.html
"""
Character	Byte order	Size	Alignment
@	        native	native	native
=	        native	standard	none
<	        little-endian	standard	none
>	        big-endian	standard	none
!	        network (= big-endian)	standard	none


"""
print ("struct")
import struct
print (struct.pack('@h', 1))
print (struct.pack('<h', 1))
little_endian = (struct.pack('@h', 1) == struct.pack('<h', 1))
print (little_endian)
