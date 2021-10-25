from tkinter import *
import os


def newsShowMoreFrame(self, feature, config, y_pos):
    news_show_more_frame = Frame(self.q, width=1024, height=600)

    image2_path = os.path.join(self.base_folder, '../medias/newsBg/' + feature['picture'])
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

        self.textWelcomeFrame()

    ChoiceButton = Button(news_show_more_frame, text="retour", command=choice, border=0,
                          activebackground='#12c4c0', bg="#12c4c0")
    ChoiceButton.place(x=950, y=550)

    news_show_more_frame.place(x=0, y=0)
    news_show_more_frame.lower()


def showMore(feature, frame):
    textwelcomeframe.pack_forget()
    textwelcomeframe.destroy()
    newsShowMoreFrame(self, feature, label_textinfo_config, label_showmore_y_position)


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