update = "More text i'm working till morning "
f = open('app.txt', 'r+')
data = f.read()   
f.write(update) 
f.close()