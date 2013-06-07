import pylab

pylab.figure()
pylab.hold(True)

I = pylab.arange(6)

pylab.plot(I,pylab.sin(I),lw=4)

pylab.plot(I,pylab.cos(I), lw=2)

pylab.plot(I,pylab.tan(I), lw=1)



pylab.show()

