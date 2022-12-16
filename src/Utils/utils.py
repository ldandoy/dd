import os
from PIL import Image, ImageTk

def imageTk(self, path) -> ImageTk:

  if len(path.split(".")) == 1:
    path += ".png"

  bgImagePath = os.path.join(self.base_folder, '../medias/', path)
  img = Image.open(bgImagePath)
  img = img.resize((self.w, self.h), Image.ANTIALIAS)
  img = ImageTk.PhotoImage(img)
  return img
