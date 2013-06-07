#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
ImageRGB.py

To process images in PIL's format.

Created by Ernesto Costa on 2008-10-10.
Copyright (c) 2008 University of Coimbra. All rights reserved.
"""

import sys
import os

import PIL.Image

class ImageRGB(object):
	
	WIDTH_INDEX = 0


	def __init__(self,file_name):
		""" Create an obect of type Image with the contents of the image 
		whose name is file_name
		"""
		self.im = PIL.Image.open(file_name)
		self.name= file_name
		self.matrix=[]
	
	def translate(self):
		"""Translate an image in PIL format into an image represented
		as a matrix of (r,g,b) pixel tuples, or raise 'Bad image type' 
		if it is not a suitable image type.
		JPEG is a suitable type, while GIF and PNG are not.
		"""
		imageData = list(self.im.getdata())
		if not isinstance(imageData[0], tuple) or not len(imageData[0]) == 3:
			raise 'Bad image type', self.name
		return _make_matrix(imageData, self.im.size[WIDTH_INDEX])

	def new(self,matrix):
		"""Return an image object made from the (r,g,b) pixel tuples in matrix.
		Two image object methods:
		show() displays the image in a window
		save(str) saves the image in a jpeg file named by the string
		"""

		width = len(matrix[0])
		height = len(matrix)
		im = PIL.Image.new('RGB', (width, height))
		im.putdata(_flatten_matrix(matrix))
		return im

	def _make_matrix(lst, numCols):
		self.matrix = []
		for i in range(0, len(lst), numCols):
			self.matrix.append(lst[i : i+numCols])
		return self.matrix


	def _flatten_matrix(matrix):
		width = len(matrix[0])
		lst = []
		for index in range(len(matrix)):
			row = matrix[index]
			if width != len(row):
				raise 'Matrix is ragged (rows not all of the same length)'
			lst = lst + row
		return lst
	
if __name__ == '__main__':
	imagem= ImageRGB('/tempo/heron.jpg')
	imagem.translate()
	print imagem
	
