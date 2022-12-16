
from PIL import Image, ImageTk
import os

class ResizedImage:
  
    @staticmethod
    def resize(self,path):
        w = self.q.winfo_screenwidth()
        h = self.q.winfo_screenheight()
        img = (Image.open(os.path.join(self.base_folder,path)))
        resizedImage = img.resize((w,h), Image.ANTIALIAS)
        bg = ImageTk.PhotoImage(resizedImage)
        return bg