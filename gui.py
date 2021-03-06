#!/usr/bin/env python
# -*- coding: utf8 -*-
import AutoArea
import csv
import tkinter as tk
import tkinter.messagebox as tkm


with open('parameter.csv', 'r') as fr:
    reader = csv.reader(fr)
    line = [row for row in reader]

scale = line[0][1]
ext = line[1][1]
name = line[2][1]
HSV_hu = line[3][1]
HSV_su = line[4][1]
HSV_vu = line[5][1]
HSV_hl = line[6][1]
HSV_sl = line[7][1]
HSV_vl = line[8][1]
cl = line[9][1]
gauk = line[10][1]
gaun = line[11][1]
closing_on = line[12][1]

# GUI parameter
win_x = 600
win_y = 450
box_w = 8
x1 = 50
x2 = 190
x3 = 330
x4 = 470
y_set = 60
y_m = 30
y_l = 50

root = tk.Tk()

root.title(u"AutoArea")
root.geometry('{0}x{1}'.format(win_x, win_y))


def get_value(event):
    scale = float(E_scale.get())
    ext = str(E_ext.get())
    name = str(E_name.get())
    HSV_hu = int(E_HSV_hu.get())
    HSV_su = int(E_HSV_su.get())
    HSV_vu = int(E_HSV_vu.get())
    HSV_u = [HSV_hu, HSV_su, HSV_vu]
    HSV_hl = int(E_HSV_hl.get())
    HSV_sl = int(E_HSV_sl.get())
    HSV_vl = int(E_HSV_vl.get())
    HSV_l = [HSV_hl, HSV_sl, HSV_vl]
    cl = int(E_cl.get())
    gauk = int(E_gauk.get())
    gaun = int(E_gaun.get())
    closing_on = Val.get()
    with open('parameter.csv', 'w', newline="") as fw:
        writer = csv.writer(fw)
        writer.writerow(["scale", scale])
        writer.writerow(["ext", ext])
        writer.writerow(["name", name])
        writer.writerow(["HSV_hu", HSV_hu])
        writer.writerow(["HSV_su", HSV_su])
        writer.writerow(["HSV_vu", HSV_vu])
        writer.writerow(["HSV_hu", HSV_hl])
        writer.writerow(["HSV_su", HSV_sl])
        writer.writerow(["HSV_vu", HSV_vl])
        writer.writerow(["cl", cl])
        writer.writerow(["gauk", gauk])
        writer.writerow(["gaun", gaun])
        writer.writerow(["closing_on", closing_on])
    fulltime = AutoArea.main(scale, ext, name, HSV_u,
                             HSV_l, cl, gauk, gaun, closing_on)
    tkm.showinfo('info', '>>> complete {0:.2f} sec <<<'.format(fulltime))
    return


S_title = tk.Label(text=u'GUI Mode of AutoArea')
S_title.place(x=x1, y=20)

Button = tk.Button(text=u'Calculation', width=box_w)
Button.bind("<Button-1>", get_value)
Button.place(x=300, y=20)

S_scale = tk.Label(text=u'Scale Transration')
S_scale.place(x=x1, y=y_set)
E_scale = tk.Entry(width=box_w)
E_scale.insert(tk.END, u'{0}'.format(scale))
E_scale.place(x=x2, y=y_set)

y_set += y_m
S_ext = tk.Label(text=u'Extension')
S_ext.place(x=x1, y=y_set)
E_ext = tk.Entry(width=box_w)
E_ext.insert(tk.END, u'{0}'.format(ext))
E_ext.place(x=x2, y=y_set)

y_set += y_m
S_name = tk.Label(text=u'Folder name')
S_name.place(x=x1, y=y_set)
E_name = tk.Entry(width=box_w)
E_name.insert(tk.END, u'{0}'.format(name))
E_name.place(x=x2, y=y_set)

y_set += y_l
y_upper = y_set + y_m
y_lower = y_set + 2 * y_m
S_HSV = tk.Label(text=u'HSV values')
S_HSV_h = tk.Label(text=u'H(0-180)')
S_HSV_s = tk.Label(text=u'S(0-255)')
S_HSV_v = tk.Label(text=u'V(0-255)')
S_HSV.place(x=x1, y=y_set)
S_HSV_h.place(x=x2, y=y_set)
S_HSV_s.place(x=x3, y=y_set)
S_HSV_v.place(x=x4, y=y_set)
S_HSV_upper = tk.Label(text=u'Uppers')
S_HSV_lower = tk.Label(text=u'Lowers')
S_HSV_upper.place(x=x1, y=y_upper)
S_HSV_lower.place(x=x1, y=y_lower)

E_HSV_hu = tk.Entry(width=box_w)
E_HSV_hu.insert(tk.END, u'{0}'.format(HSV_hu))
E_HSV_hu.place(x=x2, y=y_upper)
E_HSV_su = tk.Entry(width=box_w)
E_HSV_su.insert(tk.END, u'{0}'.format(HSV_su))
E_HSV_su.place(x=x3, y=y_upper)
E_HSV_vu = tk.Entry(width=box_w)
E_HSV_vu.insert(tk.END, u'{0}'.format(HSV_vu))
E_HSV_vu.place(x=x4, y=y_upper)

E_HSV_hl = tk.Entry(width=box_w)
E_HSV_hl.insert(tk.END, u'{0}'.format(HSV_hl))
E_HSV_hl.place(x=x2, y=y_lower)
E_HSV_sl = tk.Entry(width=box_w)
E_HSV_sl.insert(tk.END, u'{0}'.format(HSV_sl))
E_HSV_sl.place(x=x3, y=y_lower)
E_HSV_vl = tk.Entry(width=box_w)
E_HSV_vl.insert(tk.END, u'{0}'.format(HSV_vl))
E_HSV_vl.place(x=x4, y=y_lower)

y_set += + 2 * y_m + y_l
S_cl = tk.Label(text=u'Closing kernel (Odd)')
S_cl.place(x=x1, y=y_set)
E_cl = tk.Entry(width=box_w)
E_cl.insert(tk.END, u'{0}'.format(cl))
E_cl.place(x=x2, y=y_set)

# extra contents
y_set += y_l
S_extra = tk.Label(text=u'Extra Settings')
S_extra.place(x=x1, y=y_set)

y_set += y_m
S_gauk = tk.Label(text=u'Gauss kernel (Odd)')
S_gauk.place(x=x1, y=y_set)
E_gauk = tk.Entry(width=box_w)
E_gauk.insert(tk.END, u'{0}'.format(gauk))
E_gauk.place(x=x2, y=y_set)

S_gaun = tk.Label(text=u'Gauss number (Odd)')
S_gaun.place(x=x3, y=y_set)
E_gaun = tk.Entry(width=box_w)
E_gaun.insert(tk.END, u'{0}'.format(gaun))
E_gaun.place(x=x4, y=y_set)

y_set += y_m
Val = tk.BooleanVar()
Val.set(closing_on)
CheckBox = tk.Checkbutton(text=u"Closing ON", variable=Val)
CheckBox.place(x=x1, y=y_set)

root.mainloop()
