#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'offloading_controls.ui'
#
# Created: Tue Feb  3 00:27:00 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!
import os
import rospy
import rospkg

from python_qt_binding import loadUi
from python_qt_binding.QtGui import QWidget
from offloadable_face_recognition.msg import OffloadCommand

class Offloading_Controls_Widget(QWidget):

    def __init__(self, context):
        super(Offloading_Controls_Widget, self).__init__()

        rp = rospkg.RosPack()
        ui_file = os.path.join(rp.get_path('rqt_offloading_controls'), 'resource', 'offloading_controls.ui')
        loadUi(ui_file, self)
        
        self.setObjectName('Offloading_Controls_Widget')

        self.isAutomatic = True
        
        self.manual_offloading_commands = rospy.Publisher("manual_offload_commands", OffloadCommand, queue_size=1)
        #TODO: Add a subscriber to the actual WIFI signal
        #TODO: Add a publisher for the manual WIFI signal

        self.manual_offloading_btn.clicked.connect(self.set_manual_offloading)

        self.automatic_offloading_btn.clicked.connect(self.set_automatic_offloading)
        self.automatic_offloading_btn.setChecked(False)
        self.manual_offloading_btn.setChecked(True)
        self.offloading_percentage_slider.setEnabled(False)
        self.offloading_percentage_slider.setMaximum(100)
        self.offloading_percentage_slider.setMinimum(0)
        self.offloading_percentage_slider.valueChanged.connect(self.slider_value_updated)

        self.AUTOMATIC_COMMAND = True
        self.MANUAL_COMMAND = False
        self.NO_OFFLOAD_PERCENTAGE = 0

    def set_manual_offloading(self):
        if self.isAutomatic:
            self.offloading_percentage_slider.setEnabled(True)
            self.isAutomatic = False
            self.publish_offload_command(self.MANUAL_COMMAND, self.offloading_percentage_slider.value())


    def set_automatic_offloading(self):
        if not self.isAutomatic:
            self.offloading_percentage_slider.setEnabled(False)
            self.isAutomatic = True
            self.publish_offload_command(self.AUTOMATIC_COMMAND, self.NO_OFFLOAD_PERCENTAGE)

    def slider_value_updated(self, slider_value):
        if not self.isAutomatic:
            self.publish_offload_command(self.MANUAL_COMMAND, slider_value)

    def publish_offload_command(self, type, percentage):
            print percentage
            command = OffloadCommand()
            command.type = type
            command.percentage = percentage
            self.manual_offloading_commands.publish(command)

    #TODO: updates and publishes the current wifi signal to be user set
    def set_manual_wifi(self):
        pass

    #TODO: subscribes to incoming wifi signal and updates the view
    def set_automatic_wifi(self, wifi_msg):
        pass
