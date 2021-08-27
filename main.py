import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty

class Calc(App):
	pass
	
class MainLayout(GridLayout):
	text_to_display = StringProperty("")
	
	def normal_button(self, widget):
		self.text_to_display += widget.text
		if self.text_to_display[-1] in "×÷+-":
			self.ids.plus.disabled = True
			self.ids.minus.disabled = True
			self.ids.multiply.disabled = True
			self.ids.divide.disabled = True
			self.ids.equal.disabled = True
		else:
			self.ids.plus.disabled = False
			self.ids.minus.disabled = False
			self.ids.multiply.disabled = False
			self.ids.divide.disabled = False
			self.ids.equal.disabled = False
				
	def clear_button(self, widget):
		self.text_to_display = ""
		
	def equal_button(self, widget):
		
		output=self.text_to_display
		if "×" in output:
			output=output.replace("×", "*")
		if "÷" in output:
			output=output.replace("÷", "/")
		try:
			output=str(eval(output))
		except:
			output="Bad Expression!!!"
			
		self.text_to_display = ""
		self.text_to_display = output
					
Calc().run()