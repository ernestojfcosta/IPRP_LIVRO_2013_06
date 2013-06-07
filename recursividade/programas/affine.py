#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
affine.py

Created by Ernesto Costa on 2008-04-20.
Copyright (c) 2008 University of Coimbra. All rights reserved.
"""

import sys
import os

from numpy import *
import Gnuplot

# affine transformations

def translation(p, deltax,deltay):
	p[0][0] += deltax
	p[1][0] += deltay
	return p
	
def scaling(p,sh,sv):
	M=array([[sh, 0],[0,sv]])
	res= dot(M,p)
	return res
	
def reflection(p, rx,ry):
	M=array([[rx, 0],[0,ry]])
	res= dot(M,p)
	return res
	
def rotation(p,r1,r2,r3,r4):
	M=array([[r1, r2],[r3,r4]])
	res= dot(M,p)
	return res

def affine(p,a,b,c,d,e,f):
	# a,b,c,d: scale, reflection and rotation
	# e, f: translation
	M=array([[a,b,e], [c,d,f],[0,0,1]])
	p=[p[0],p[1],1]
	res=dot(M,p)
	return res
	
# plot

def plot_points(points, title):
	g=Gnuplot.Gnuplot(persist=1)
	#g('set pointsize 4.0')
	#g('set data style lines')
	c1=Gnuplot.Data([points[0]], with='points pt 3 ps 5')
	c2=Gnuplot.Data([points[1]], with='points pt 4 ps 5 ')
	c3=Gnuplot.Data([points[2]], with='points pt 5 ps 5')
	c4=Gnuplot.Data([points[3]], with='points pt 6 ps 5')
	g.plot(c1,c2,c3,c4, title=title)
	return 0		

def main():
	p=array([[2.0],[4.0]])
	print "initial point %s \n" % p
	print "After scaling, translating and rotating"
	print rotation(translation(scaling(p,2,2), 0.5,0.5),0,1,-1,0)
	return 0


if __name__ == '__main__':
	main()
	"""points=[[0,0],[1,0],[1,1],[0,1]]
	p1=points
	plot_points(p1, title='Normal')
	p2=[]
	for p in points:
		p2 +=[translation([[p[0]],[p[1]]],0.5,0.5)]
	print p2
	plot_points(array(p2[0]), title='Translation')
	#p3=scaling(points,0.5,0.5)
	#plot_points(p3, title='Scaling')
	#p4=reflection(points,-1,1)
	#plot_points(p4, title='Reflection')
	#p5=rotation(points,0,1,-1,0)
	#plot_points(p5, title='Rotation')
	"""
	"""print "translation"
	np=translation(p,0.5, 0.8)
	print np
	print "scaling"
	sh = 1.5
	sv = 2.0
	ns=scaling(p,sh,sv)
	print ns
	print "Reflection"
	nref=reflection(p,-1,1)
	print nref
	print "Rotation"
	nrot= rotation(p,0,1,-1,0)
	print nrot
	
	print "plotting"
	points=[[0,0],[1,0],[1,1],[0,1]]
	plot_points(points,'Normal')"""
	
	

