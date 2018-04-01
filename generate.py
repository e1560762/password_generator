from src import password_generator
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.base import runTouchApp
from kivy.config import Config
from kivy.core.window import Window

Config.set('graphics','resizable',0)
Window.size = (300, 400)

class RootWidget(GridLayout):
	def __init__(self, **kwargs):
		super(RootWidget, self).__init__(**kwargs)
		self.alphabet = ["lowercase", "uppercase", "digit", "punctuation"]
		for v in self.alphabet:
			key = "%s_exists" % (v)
			getattr(self, key, True)

		txtinput = TextInput(hint_text="Enter the length of password", input_filter='int', multiline=False)
		txtinput.bind(text=lambda ins, val: setattr(self,"pass_length", val))
		self.add_widget(txtinput)
		for v in self.alphabet:
			spinner = Spinner(
				text="Include %s" % (v.title()),
				values=("Include %s" % (v.title()),"Exclude %s" % (v.title())),
				)
			spinner.bind(text=self.setExist)
			self.add_widget(spinner)

		txtinput = TextInput(hint_text="Restricts number of occurrences of each set", input_filter='int', multiline=False)
		txtinput.bind(text=lambda ins, val: setattr(self,"min_occurrence", val))
		self.add_widget(txtinput)

		button = Button(text="Submit", size_hint_y=None, height=44)
		button.bind(on_release=self.submit)
		self.add_widget(button)

	def submit(self, btn):
		try:
			length = int(getattr(self,"pass_length",None))
		except ValueError:
			length = 8

		kwargs = {}
		try:
			kwargs['min'] = int(getattr(self,"min_occurrence", None))
		except:
			kwargs['min'] = None

		for v in self.alphabet:
			key = "%s_exists" % (v)
			kwargs[v] = getattr(self, key, True)
		
		pg = password_generator.PasswordGenerator()
		result, message = pg.generate(length, **kwargs)
		label = "Success"
		if message:
			result = message
			label = "Fail"	
		popup = Popup(title=label, content=Label(text=result), size_hint=(None, None), size=(300,100))
		popup.open()

	def setExist(self, btn, txt):
		val = True if txt.find("Include") > -1 else False
		key = "%s_exists" % (txt.split(" ")[1].lower())
		setattr(self,key,val)

class MainApp(App):
	def build(self):
		return RootWidget(cols=1, row_force_default = True, row_default_height=44)

if __name__ == '__main__':
	MainApp().run()