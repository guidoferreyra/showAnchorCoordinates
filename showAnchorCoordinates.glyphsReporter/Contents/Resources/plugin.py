# encoding: utf-8

###########################################################################################################
#
#
#	Reporter Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Reporter
#
#
###########################################################################################################

from __future__ import division, print_function, unicode_literals
import objc
from GlyphsApp import *
from GlyphsApp.plugins import *

fontColor1 =  0.58, 0.2, 0.2, 0.7
fontColor1 = NSColor.colorWithCalibratedRed_green_blue_alpha_( *fontColor1 )

fontSize = 10

class showAnchorCoordinates(ReporterPlugin):
	@objc.python_method
	def settings(self):
		self.menuName = Glyphs.localize({'en': u'Anchor Coordinates'})
	
	@objc.python_method
	def foregroundInViewCoords(self, layer = None):
		try:
			windowController = self.controller.view().windowController()
		except:
			windowController = self.controller.view().window().windowController()
		
		if windowController.toolDrawDelegate().className() == "GlyphsToolHand" or windowController.toolDrawDelegate().className() == "GlyphsToolText":
			return
		try:
			layer = self.activeLayer()
			self._pos = self.activePosition()
			self._scale = self.getScale()

		
			for thisAnchor in layer.anchors:
				x = int(round(thisAnchor.position[0]))
				y = int(round(thisAnchor.position[1]))
				text = str(x)+ ", " + str(y)
				self.drawText( text, (x, y), fontSize, fontColor1, 'bottomleft')

					
		except Exception as e:
			import traceback
			print(traceback.format_exc())
	
	@objc.python_method
	def drawText(self, text, textPosition, fontSize, fontColor, textAlign):
		try:
			string = NSString.alloc().initWithString_(text)
			drawPos = (textPosition[0] * self._scale + self._pos.x + 1 , textPosition[1] * self._scale + self._pos.y + 1)
			string.drawAtPoint_color_alignment_handleSize_(drawPos, fontColor, 0, -1)
		except Exception as e:
			print (e)
			pass

	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
