import sublime, sublime_plugin
import os
from random import randint as rnd

def md(*t):
	t = ' '.join([str(el) for el in t])
	sublime.message_dialog(t)

def sm(*t):
	t = ' '.join([str(el) for el in t])
	sublime.status_message(t)

def em(*t):
	t = ' '.join([str(el) for el in t])
	sublime.error_message(t)

def get_indent(text):
	indent = 0
	for char in text:
		if char == '\t':
			indent += 1
		else:
			return indent

class CounterWraperCommand(sublime_plugin.TextCommand):

	def get_setting(self, name, default=None):
		return self.setting.get(name) or default

	def run(self, edit, *arg, **args):
		self.window = self.view.window()
		self.selection = sublime.Selection(self.view.id())
		self.setting = self.view.settings()

		for region in self.view.sel():
			region = self.view.full_line(region)
			indent = get_indent(self.view.substr(region))
			nb = str(rnd(100, 1000))
			code = ' # counter' + nb
			text = ('\t' * indent) + 'counter = 0' + code + '\n'
			text += self.view.substr(region)
			text += ('\t' * indent) + '\tcounter += 1' + code + '\n'
			text += ('\t' * indent) + '\tif counter > 100:' + code + '\n'
			text += ('\t' * indent) + '\t\tprint("end up counter ' + nb + '")' + code + '\n'
			text += ('\t' * indent) + '\t\treturn False' + code + '\n'

			self.view.replace(edit, region, text)

