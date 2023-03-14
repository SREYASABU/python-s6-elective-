str="Python Programming by Sreya"
print(f'str: {str}\nLast 4 characters: {str[-4:]}\nSubstring from index 4 to 8: {str[4:8]}\nmin:{min(str)} max:{max(str)}')
print(f'trimming last 4 characters: {str.rstrip("reya")}\nlength of string: {len(str)}\nreplacing m with * {str.replace("m","*")}')
print(f'trimming first 4 characters: {str.lstrip("Pyth")}\nchanging cases: {str.swapcase()}\nstarting index of "gr": {str.find("gr")}')
print(f'reversed string: {str[::-1]}\nto upper case: {str.upper()}\nnumber of occurrences of "m": {str.count("m")}')
print(f'index of 1st occurrence of "t":{str.find("t")}\ncharacters in even position: {str[::2]}')
print(f'characters at even position in reverse order: {str[::-2]}')
if str.find("on")==-1:
 print(f'"on" not a substring')
else:
 print(f'"on" is a substring at {str.find("on")}\ntitlecase?:{str.istitle()}')