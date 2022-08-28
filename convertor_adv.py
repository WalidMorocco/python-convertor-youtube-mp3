# Importing packages
from pytube import YouTube
import os
import wx


class MyFrame(wx.Frame):    
    def __init__(self):
        # Set window and panel
        super().__init__(parent=None, title='MP3 Youtube Convertor')
        panel = wx.Panel(self)
        
        # Set sizer to add the objects and align them vertically with Add()
        my_sizer = wx.BoxSizer(wx.VERTICAL) 
    
        # URL Label
        self.url_label = wx.StaticText(panel, label='URL')
        my_sizer.Add(self.url_label, 0, wx.ALL | wx.EXPAND, 5)
        
        # URL Input Field
        self.url_input = wx.TextCtrl(panel)
        my_sizer.Add(self.url_input, 0, wx.ALL | wx.EXPAND, 5)
        
        # Name Label
        self.name_label = wx.StaticText(panel, label='Set a title for the file: (leave empty if you want to keep the original title)')
        my_sizer.Add(self.name_label, 0, wx.ALL | wx.EXPAND, 5)
        
        # Name Input Field
        self.name_input = wx.TextCtrl(panel)
        my_sizer.Add(self.name_input, 0, wx.ALL | wx.EXPAND, 5)

        # Destination Label
        self.destination_label = wx.StaticText(panel, label='Destination folder: (leave empty if you want to save on this folder)')
        my_sizer.Add(self.destination_label, 0, wx.ALL | wx.EXPAND, 5)
        
        # Destination Input Field
        self.destination_input = wx.TextCtrl(panel)
        my_sizer.Add(self.destination_input, 0, wx.ALL | wx.EXPAND, 5)
        
        # Button
        my_btn = wx.Button(panel, label='Convert')
        my_btn.Bind(wx.EVT_BUTTON, self.save)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)
        
        # Sets layout to window
        panel.SetSizer(my_sizer)
        self.Show()
        
    
    def save(self, event):
        # Assign inputs to variables
        value = self.url_input.GetValue()
        name = self.name_input.GetValue()
        destination = self.destination_input.GetValue() or '.'
        
        # Make sure user enter url
        if not value:
            # Error msg
            print("Enter an URL!")
        else:
            # Use pytube library to download video
            yt = YouTube(value)
            video = yt.streams.filter(only_audio=True).first()  
            out_file = video.download(output_path=destination)

            # Give default title or chosen title depending on the user input
            if name:
                title = destination + '/' + name
            else:
                base, ext = os.path.splitext(out_file)
                title = base
            
            # Save the video
            new_file = title + '.mp3'
            os.rename(out_file, new_file)
            print(title + " has been successfully downloaded.")

# Run
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()