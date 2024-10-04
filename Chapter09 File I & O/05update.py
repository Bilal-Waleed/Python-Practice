update = "More text i'm working"
f = open('app.txt', 'r+')
data = f.read()   
f.write(update) 
f.close()