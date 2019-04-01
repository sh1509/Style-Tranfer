import matplotlib.pyplot as plt

t = [0, 50, 100, 150, 200, 250, 300]
sl = [432.34521, 103.347694, 21.192739, 7.963869, 4.342989, 2.661353, 1.956453]
cl = [103.4321, 17.190935, 16.772572, 13.913394, 11.616838, 10.120035, 9.193060]

s, = plt.plot(t, sl, 'r-', label="Style Loss")
c, = plt.plot(t, cl, 'c-', label="Content Loss")
plt.title('Loss Graph')
plt.legend(handles=[s, c])
plt.xlabel('Run')
plt.ylabel('Loss')
plt.axes()
plt.savefig('chuneet.png')