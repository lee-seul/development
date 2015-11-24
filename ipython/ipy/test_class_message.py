# coding: utf-8
# test_class_message.py

class Message:
	def __init__(self, msg):
		self.msg = msg

	def __repr__(self):
		return 'Message: %s' % self.msg

