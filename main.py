import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty

class MainLayout(GridLayout):
	text_to_display=StringProperty("")
	
	def encrypt(self):
		given_text=self.ids.textinput.text
		changed_text=""
		no=len(given_text)%1114111			
		for ch in given_text:
			changed_text += chr(ord(ch)+no)
			self.text_to_display=changed_text
		
			
	def decrypt(self):
		given_text=self.ids.textinput.text
		changed_text=""
		no=len(given_text)%1114111			
		for ch in given_text:
			changed_text += chr(ord(ch)-no)
			self.text_to_display=changed_text
		
		
class SecretChat(App):
	pass
	
SecretChat().run()