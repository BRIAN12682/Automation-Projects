from tkinter import *
import webview
  
# define an instance of tkinter
tk = Tk()
  
#  size of the window where we show our website
tk.geometry("550x550")
  
# Open website
webview.create_window('CHATGPT', 'https://chat.openai.com/')
webview.start()
