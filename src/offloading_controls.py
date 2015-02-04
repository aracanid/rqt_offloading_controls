#!/usr/bin/env python

from rqt_gui_py.plugin import Plugin
from offloading_controls_widget import Offloading_Controls_Widget

class Offloading_Controls(Plugin):

	def __init__(self, context):
		super(Offloading_Controls, self).__init__(context)
		self.setObjectName('Offloading_Controls')

		self._widget = Offloading_Controls_Widget(context)
		if context.serial_number() > 1:
			self._widget.setWindowTitle(self._widget.windowTitle() + (' (%d)' % context.serial_number()))
		context.add_widget(self._widget)

	def shutdown_plugin(self):
		# TODO unregister all publishers here
		pass