import datetime
import random
from pathlib import Path
from tkinter import *
from tkinter.ttk import Combobox

LABEL_FONT_SIZE = 14
PATH_BASE = Path(__file__).parent
PATH_TMP = PATH_BASE.joinpath('tmp')
PATH_RES = PATH_BASE.joinpath('res')

FONT_STULE = {
    "Чорний без контуру": f"font-style:normal;font-weight:normal;line-height:1.25;font-family:sans-serif;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.2;",
    "Білий з чорнти контуром": f"font-style:normal;font-weight:normal;line-height:1.25;font-family:sans-serif;fill:#ffffff;fill-opacity:1;stroke:#000000;stroke-width:0.2;stroke-opacity:1;",
}

FILE_HEAD_SVG = """
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->

<svg
   width="297mm"
   height="210mm"
   viewBox="0 0 297 210"
   version="1.1"
   id="svg5"
   inkscape:version="1.1.2 (b8e25be833, 2022-02-05)"
   sodipodi:docname="set.svg"
   inkscape:export-xdpi="96"
   inkscape:export-ydpi="96"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:svg="http://www.w3.org/2000/svg">
  <sodipodi:namedview
     id="namedview7"
     pagecolor="#505050"
     bordercolor="#eeeeee"
     borderopacity="1"
     inkscape:pageshadow="0"
     inkscape:pageopacity="0"
     inkscape:pagecheckerboard="0"
     inkscape:document-units="mm"
     showgrid="false"
     inkscape:zoom="0.90509668"
     inkscape:cx="151.91747"
     inkscape:cy="156.88932"
     inkscape:window-width="1920"
     inkscape:window-height="1017"
     inkscape:window-x="-8"
     inkscape:window-y="-8"
     inkscape:window-maximized="1"
     inkscape:current-layer="layer1"
     showguides="true"
     inkscape:guide-bbox="true">
    <sodipodi:guide
       position="7,210"
       orientation="-1,0"
       id="guide1793"
       inkscape:label=""
       inkscape:locked="false"
       inkscape:color="rgb(0,0,255)" />
    <sodipodi:guide
       position="0,203"
       orientation="0,1"
       id="guide1797"
       inkscape:label=""
       inkscape:locked="false"
       inkscape:color="rgb(0,0,255)" />
    <sodipodi:guide
       position="290,210"
       orientation="-1,0"
       id="guide1799"
       inkscape:label=""
       inkscape:locked="false"
       inkscape:color="rgb(0,0,255)" />
    <sodipodi:guide
       position="0,7"
       orientation="0,1"
       id="guide1801"
       inkscape:label=""
       inkscape:locked="false"
       inkscape:color="rgb(0,0,255)" />
  </sodipodi:namedview>
  <defs
     id="defs2" />
  <g
     inkscape:label="Шар 1"
     inkscape:groupmode="layer"
     id="layer1">
"""
FILE_END_SVG = """
  </g>
</svg>
"""


class TempFileSVG(object):
    content = ''

    def __init__(self, obj_id="id", path_file=None):
        self.obj_id = obj_id
        self.x = 0
        self.y = 0
        if path_file:
            self.path_file = path_file
            with open(self.path_file) as file:
                s = file.read().split('<!--split-->')
                if len(s) == 3:
                    TempFileSVG.content = s[1]

    def get_str(self):
        return f'<g transform = "translate({self.x}, {self.y})" >{TempFileSVG.content}</g>\n'


class BaseSVG(object):
    def __init__(self, obj_id, x, y):
        self.obj_id = obj_id
        self.x = x
        self.y = y


class RectSGV(BaseSVG):
    def __init__(self, obj_id='id', x=0, y=0):
        super().__init__(obj_id, x, y)
        # self.style = "fill:#f1f304;stroke-width:0.232509"
        self.style = "fill:#f0f0f0;stroke-width:1;fill-opacity:1;stroke:#000000;stroke-opacity:1;stroke-miterlimit:4;stroke-dasharray:none"
        self.width = 69.5
        self.height = 97
        self.ry = "8.2346954"

    def get_str(self):
        return f'<rect style="{self.style}" id="{self.obj_id}" width="{self.width}" height="{self.height}" x="{self.x}" y="{self.y}" ry="{self.ry}" />\n'


class TextSGV(BaseSVG):
    # 1 RectSGV.height == 4.97px
    # 1px in class == 3.78px in inkscape
    font_size = 5
    style = f"font-style:normal;font-weight:normal;line-height:1.25;font-family:sans-serif;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.2;"

    def __init__(self, obj_id='id', text='word', x=0, y=0):
        super().__init__(obj_id, x, y)
        self.text = text

    def get_str(self):
        return f'<text id="{self.obj_id}" style="{TextSGV.style}font-size:{TextSGV.font_size}px;"  x="{self.x}" y="{self.y}" >{self.text}</text>\n'


def clicked():
    TextSGV.style = FONT_STULE.get(combo3.get())
    TextSGV.font_size = int(combo4.get())
    # lbl3.configure(text="Я же просил...")
    # words_of_cart = combo.get()
    count_words_of_cart = int(combo.get())
    words_lst = text.get("1.0", "end").split('\n')
    # words_lst = ['Адреса поштової скриньки', 'w1', 'w2', 'w3', 'w4', 'w5', 'w6', 'w7', 'w8', 'w9', 'w10', 'w11', 'w12',
    #              'w13', 'w14', 'w15', 'w16', 'w17', 'w18', 'w19', 'w20', 'w21', 'w22', 'w23', 'w24', 'w25', 'w26',
    #              'w27', 'w28', 'w29']
    words_lst.pop()
    words_lst_len = len(words_lst)

    if is_random.get():
        random.shuffle(words_lst)

    print("is_random.get():", is_random.get())
    carts_count = words_lst_len // count_words_of_cart + bool(words_lst_len % count_words_of_cart)
    print(combo.get())
    print(words_lst)
    start_words_lst = 0
    # print(RectSGV().height - 20)
    # print(round(TextSGV().font_size * 3.78 / 4.97, 2))
    # print((RectSGV().height - 10 - round(TextSGV().font_size * 3.78 / 4.97, 2) * count_words_of_cart))
    padding_bottom_word = round(
        (RectSGV().height - 14 - round(TextSGV.font_size * 3.78 / 4.97, 2) * count_words_of_cart) / (
                count_words_of_cart - 1), 3)

    # end_words_lst = count_words_of_cart if (start_words_lst + count_words_of_cart) <= words_lst_len else words_lst_len
    if (start_words_lst + count_words_of_cart) <= words_lst_len:
        end_words_lst = count_words_of_cart
    else:
        end_words_lst = words_lst_len

    date = str(datetime.datetime.now()).replace(':', '_')
    with open(PATH_RES.joinpath(f'{date}.svg'), 'w', encoding='utf-8') as file:
        file.write(FILE_HEAD_SVG)

        if combo2.get() == 'default':
            class_svg_object = RectSGV
        else:
            class_svg_object = TempFileSVG
            TempFileSVG('g_1', PATH_TMP.joinpath(combo2.get()))

        for i_cart in range(carts_count):
            rect = class_svg_object(f'rect{i_cart}')
            rect.x = 7 + 71.083 * (i_cart % 4)
            rect.y = 7 + 99 * bool(i_cart >= 4)
            file.write(rect.get_str())

            i = 0
            if add_number.get():
                for i_word in range(start_words_lst, end_words_lst):
                    text_svg = TextSGV(f'text{i_word}', str(i + 1) + ' ' + words_lst[i_word])
                    text_svg.x = rect.x + 8
                    text_svg.y = rect.y + 12 + (round(TextSGV.font_size * 3.78 / 4.97, 2) + padding_bottom_word) * i
                    file.write(text_svg.get_str())
                    i += 1
            else:
                for i_word in range(start_words_lst, end_words_lst):
                    text_svg = TextSGV(f'text{i_word}', words_lst[i_word])
                    text_svg.x = rect.x + 8
                    text_svg.y = rect.y + 12 + (round(TextSGV.font_size * 3.78 / 4.97, 2) + padding_bottom_word) * i
                    file.write(text_svg.get_str())
                    i += 1

            start_words_lst = end_words_lst
            # end_words_lst = start_words_lst + count_words_of_cart if (start_words_lst + count_words_of_cart) <= words_lst_len else words_lst_len
            if (start_words_lst + count_words_of_cart) <= words_lst_len:
                end_words_lst = start_words_lst + count_words_of_cart
            else:
                end_words_lst = words_lst_len

        file.write(FILE_END_SVG)
        lbl3.configure(text="генерація пройшла успішно")


window = Tk()
window.title("Вітаю у програмі генерації карток")
window.geometry('430x680')

lbl1 = Label(window, text="Оберіть кількість слів на карткі", font=("Arial Bold", LABEL_FONT_SIZE))
lbl1.grid(column=0, row=0)

combo = Combobox(window)
combo['values'] = (3, 4, 5, 6, 7, 8)
combo.current(3)  # default value
combo.grid(column=0, row=1)

lbl4 = Label(window, text="Оберіть шаблон", font=("Arial Bold", LABEL_FONT_SIZE))
lbl4.grid(column=0, row=2)


def get_files_name(path, template):
    res = []
    for p in sorted(path.glob(template)):
        res.append(p.name)
    return tuple(res)


combo2 = Combobox(window)
combo2['values'] = ('default',) + get_files_name(PATH_TMP, '*.svg')
combo2.current(0)  # default value
combo2.grid(column=0, row=3)

lbl6 = Label(window, text="Виберіть розмір шрифту", font=("Arial Bold", LABEL_FONT_SIZE))
lbl6.grid(column=0, row=4)

combo4 = Combobox(window)
combo4['values'] = (3, 4, 5, 6)
combo4.current(2)  # default value
combo4.grid(column=0, row=5)

lbl2 = Label(window, text="Виберіть стиль шрифту", font=("Arial Bold", LABEL_FONT_SIZE))
lbl2.grid(column=0, row=6)

combo3 = Combobox(window)
combo3['values'] = tuple(FONT_STULE.keys())
combo3.current(0)  # default value
combo3.grid(column=0, row=7)

lbl5 = Label(window, text="Введть всі необхідні слова", font=("Arial Bold", LABEL_FONT_SIZE))
lbl5.grid(column=0, row=8)

text = Text(window, height=20, width=52)
text.grid(column=0, row=9)

add_number = IntVar()
c1 = Checkbutton(window, text='Додати нумерацію слів?', variable=add_number, onvalue=1, offvalue=0)
c1.grid(column=0, row=10)

is_random = IntVar()
c2 = Checkbutton(window, text='Перемішати слова?', variable=is_random, onvalue=1, offvalue=0)
c2.grid(column=0, row=11)

btn = Button(window, text="Згенерувати", bg="black", fg="red", command=clicked)
btn.grid(column=0, row=12)

lbl3 = Label(window, text="", font=("Arial Bold", LABEL_FONT_SIZE))
lbl3.grid(column=0, row=13)

window.mainloop()
