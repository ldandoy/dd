from tkinter import *
import os

from Utils.GetLastFeatures import GetLastFeatures
from functools import partial

try:
    from Window.TextWelcomeFrame import textWelcomeFrame
except ImportError:
    print("Error")

lastFeaturesObj = GetLastFeatures( 3 )

label_textinfo_config = ('Calirbi (Body)', 24, 'bold')

label_textinfo_x_position = 25
label_showmore_y_position = 100

def lastNews(q, textwelcomeframe):
    def newsShowMoreFrame(q, feature, config, y_pos):
        news_show_more_frame = Frame(q, width=1024, height=600)

        image2_path = os.path.join(os.path.dirname(__file__), '../medias/newsBg/' + feature['picture'])
        bg2 = PhotoImage(file=image2_path)
        canvas2 = Canvas(news_show_more_frame, width=1024, height=600)
        canvas2.pack(fill="both", expand=True)
        canvas2.create_image(0, 0, image=bg2, anchor="nw")
        canvas2.image = bg2

        for i, info in enumerate(feature):
            if (info != 'picture'):
                label_textinfo = Label(news_show_more_frame, text=feature[info], fg='white', bg='#0483d1')
                label_textinfo.config(font=config)
                label_textinfo.place(x=25, y=y_pos + (i * 40))

        def choice():
            news_show_more_frame.pack_forget()
            news_show_more_frame.destroy()

            textWelcomeFrame()

        ChoiceButton = Button(news_show_more_frame, text="retour", command=choice, border=0,
                              activebackground='#12c4c0', bg="#12c4c0")
        ChoiceButton.place(x=950, y=550)

        news_show_more_frame.place(x=0, y=0)
        news_show_more_frame.lower()


    def showMore(feature):
        textwelcomeframe.pack_forget()
        textwelcomeframe.destroy()
        newsShowMoreFrame(q, feature, label_textinfo_config, label_showmore_y_position)


    for i, feature in enumerate(lastFeaturesObj):
        label_textinfo = Label(textwelcomeframe, text=feature['title'][0:50], fg='white',
                               bg='#0483d1', )
        label_textinfo.config(font=label_textinfo_config)
        label_textinfo.place(x=label_textinfo_x_position + (i * 350), y=250)
        news_Button = Button(textwelcomeframe, text="En savoir plus", command=partial(showMore, feature),
                             border=0,
                             activebackground='#12c4c0',
                             bg="#12c4c0")
        news_Button.place(x=label_textinfo_x_position + (i * 350), y=300)
