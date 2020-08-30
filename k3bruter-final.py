#!/usr/bin/env python3
import sys, math
from itertools import permutations
# read filename from command-line arguments and import encrypted text into char_array without line feeds or spaces
char_array = [ch for ch in open(sys.argv[1]).read() if ch != '\n' if ch != ' ']
key_length = sys.argv[2]
key_list = [None] * int(key_length)
for i in range (0, int(key_length)):
  key_list[i] = int(i)
perms = permutations(key_list)
for keyguess in list(perms):
  for gridguess in range (int(key_length)+1, len(char_array)):
    # set text_length equal to the length of the char_array
    text_length = int(len(char_array))
    # read key from command line arguments and build array from key
    key_array = keyguess
    #print(key_array)
    #read grid_length from command line argument
    grid_length = gridguess
    #set up arrays and print variables
    interim_array = [None] * text_length
    interim_array_2 = [None] * text_length
    final_array = [None] * text_length
    fback = [None] * text_length
    lenarray = [None] * len(key_array)
    position = [None] * len(key_array)
    column_lengths_array = [grid_length] * math.ceil(text_length/grid_length)
    column_lengths_array[(len(column_lengths_array))-1] = text_length-(((len(column_lengths_array))-1)*grid_length)
    #print(column_lengths_array)
    row_lengths_array = [text_length//grid_length] * grid_length
    x = text_length%grid_length
    #print(x)
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

    #split the input as follows:
    #e=f=g=0
    #for e in range (0, len(key_array)):
    #  for f in range (0, position[e]):
    #    sys.stdout.write(char_array[g])
    #    g += 1
    #  sys.stdout.write("\n")

    #reorder the columns according to the key move to the correct offset, get the correct number of characters, and then read the correct number of characters from char_array into interim_array_1
    h=i=j=text=0
    for h in range (0, len(key_array)):
      i = key_array.index(h)
      offset = sum(lenarray[0:int(i)])
      numchars = position[h]
      for j in range (0, numchars):
        interim_array[offset] = char_array[text]
        offset += 1
        text += 1
    #print(interim_array)

    #print out the re-ordered rows
    #e=f=g=0
    #for e in range (0, len(key_array)):
    #  for f in range (0, lenarray[e]):
    #    sys.stdout.write(interim_array[g])
    #    g += 1
    #  sys.stdout.write("\n")

    #print(interim_array)

    # build interim array 2

    l=m=n=o=offset=p=q=r=s=t=u=v=0
    for k in range (0, int(len(row_lengths_array))):
      step = row_lengths_array[k]
      for m in range (0, step):
        interim_array_2[o] = interim_array[n+offset+s]
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

    g=h=j=col=0
    for k in range (0, grid_length):
      for i in range (0, row_lengths_array[k]):
        fback[h+col] = interim_array_2[g]
        g += 1
        h += grid_length
      col += 1
      h = 0
    #print(fback)

    final_array = fback.copy()
    final_array.reverse()
    #print(final_array)

    #with open(sys.argv[4], "w") as txt_file:
    #  for i in range (0, text_length):
    #    txt_file.write(final_array[i])
    #txt_file.close()

    keyarraystring = ''
    keyarraystring = keyarraystring.join(str(key_array))

    words = [line for line in open("top_1000_english_words.txt").read().splitlines()]
    text = ""
    test = 0
    counter = 0
    text = text.join(final_array)
    for i in range (0, len(words)):
      if len(words[i]) > 2:
        test = text.find(words[i])
      if test >= 0:
        counter += 1
    #print(counter)

    with open("results.txt", "a") as file:
      if counter >= 10:
        file.write(str(counter)+","+keyarraystring+","+str(grid_length)+","+text+"\n")
    file.close()

    test = 0
    counter = 0
    text = ""
    text = text.join(fback)
    for i in range (0, len(words)):
      if len(words[i]) > 2:
        test = text.find(words[i])
      if test >= 0:
        counter += 1
    #print(counter)

    with open("results.txt", "a") as file:
      if counter >= 10:
        file.write(str(counter)+","+keyarraystring+","+str(grid_length)+","+text+"\n")
    file.close()
