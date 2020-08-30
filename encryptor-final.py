#!/usr/bin/env python3
import sys, math
# read filename from command-line arguments and import encrypted text into char_array without line feeds or spaces
char_array = [ch for ch in open(sys.argv[1]).read() if ch != '\n' if ch != ' ']
# set text_length equal to the length of the char_array
text_length = int(len(char_array))
# read key from command line arguments and build array from key
key_array = [ch for ch in (sys.argv[2])]
#read grid_length from command line argument
grid_length = int(sys.argv[3])
#set up arrays and print variables
interim_array = [None] * text_length
interim_array_2 = [None] * text_length
final_array = [None] * text_length
lenarray = [None] * len(key_array)
position = [None] * len(key_array)
column_lengths_array = [grid_length] * math.ceil(text_length/grid_length)
column_lengths_array[(len(column_lengths_array))-1] = text_length-(((len(column_lengths_array))-1)*grid_length)
#print(column_lengths_array)
row_lengths_array = [text_length//grid_length] * grid_length
x = text_length%grid_length
for y in range (0, x):
  row_lengths_array[y] = math.ceil(text_length/grid_length)
#print(row_lengths_array)


#print(char_array)
print("Key is:", key_array)
print("Grid length is:", grid_length)

# build array of lengths
for a in range (0, len(key_array)):
  b = 0
  b = (text_length-(((text_length//grid_length)*(grid_length%int(len(key_array))))+((text_length)-(text_length//grid_length)*grid_length)%int(len(key_array))))//len(key_array)
  if a < (grid_length%(len(key_array))):
    b += (text_length//grid_length)
  if a < (text_length-((text_length//grid_length)*grid_length))%int((len(key_array))):
    b += 1
  lenarray[a] = b
#print(lenarray)

# build array for starting positions
for c in range (0, len(key_array)):
  d = 0
  d = (text_length-(((text_length//grid_length)*(grid_length%int(len(key_array))))+((text_length)-(text_length//grid_length)*grid_length)%int(len(key_array))))//len(key_array)
  if c < (grid_length%(len(key_array))):
    d += (text_length//grid_length)
  if c < (text_length-((text_length//grid_length)*grid_length))%int((len(key_array))):
    d += 1
  position[int(key_array[c])] = d
#print(position)

fback = char_array
fback.reverse()

#print(fback)

#f=0
#for e in range (0, text_length):
#  sys.stdout.write(fback[e])
#  f += 1
#  if f == grid_length:
#    sys.stdout.write("\n")
#    f = 0
#sys.stdout.write("\n")

g=h=j=col=0
for k in range (0, grid_length):
  for i in range (0, row_lengths_array[j]):
    interim_array[g] = fback[h+col]
    g += 1
    h += grid_length
  col += 1
  h = 0
  j += 1

#print(interim_array)


l=m=n=o=offset=p=q=r=s=t=u=v=0
for k in range (0, int(len(row_lengths_array))):
  step =  row_lengths_array[k]
  for m in range (0, step):
    interim_array_2[n+offset+s] = interim_array[o]
    n += 1
    o += 1
  n = 0
  offset += lenarray[p]
  p += 1
  q += 1
  if q == int(len(key_array)):
    q = 0
    p = 0
    offset = 0
    r += 1
  s = 0
  for u in range (0, r):
    s += int(row_lengths_array[q+v])
    v += len(key_array)
  v = 0
#print(interim_array_2)

# build final array
first_char = 0
for k in range (0, len(key_array)):
  u = (key_array[k])
  start = sum(position[0:int(u)])
  for a in range (0, lenarray[k]):
    final_array[start] = interim_array_2[first_char]
    first_char += 1
    start += 1
print(final_array)

for i in range (0, text_length):
  sys.stdout.write(final_array[i])
sys.stdout.write("\n")

with open(sys.argv[4], "w") as txt_file:
  for i in range (0, text_length):
    txt_file.write(final_array[i])
txt_file.close() 
