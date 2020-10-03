from tkinter import *
from PIL import ImageTk, Image
import math

root = Tk()  # create the window
root.title("O-Ring Compression Calculator ver 0.3")
root.geometry("800x500")

# Place frame for input section

frame_input = LabelFrame(root, padx=5, pady=5)
frame_input.grid(row=0, column=0, padx=10, pady=10, stick=W + N)

# Place label for input section
input_section_title = Label(frame_input, text="Input Section", font=("", 15))
input_section_title.grid(row=0, column=0, columnspan=4)

tolerance_minus_sign_label = Label(frame_input, text="Tol -", font=("",(10)))
tolerance_minus_sign_label.grid(row=1, column=2)

tolerance_plus_sign_label = Label(frame_input, text="Tol +", font=("",(10)))
tolerance_plus_sign_label.grid(row=1, column=3)

oring_id_label = Label(frame_input, text="Enter o-ring inner diameter A:")
oring_id_label.grid(row=2, column=0, stick=W)

oring_dia_label = Label(frame_input, text="Enter o-ring x-section diameter B:")
oring_dia_label.grid(row=3, column=0, stick=W)

bore_dia_lable = Label(frame_input, text="Enter bore diameter C:")
bore_dia_lable.grid(row=4, column=0, stick=W)

# oring_OD_label = Label(frame_1, text="Enter outer diameter for the o-ring:")
# oring_OD_label.grid(row=4, column=0,stick=W)

shaft_dia_label = Label(frame_input, text="Enter shaft diameter D:")
shaft_dia_label.grid(row=5, column=0, stick=W)

groove_dia_label = Label(frame_input, text="Enter groove diameter E:")
groove_dia_label.grid(row=6, column=0, stick=W)

groove_width_label = Label(frame_input, text="Enter groove width F:")
groove_width_label.grid(row=7, column=0, stick=W)

groove_r_label = Label(frame_input, text="Enter groove radius G:")
groove_r_label.grid(row=8, column=0, stick=W)


# Place input box for input section

oring_ID_input = Entry(frame_input, width=15, borderwidth=1)
oring_ID_input.grid(row=2, column=1)

oring_section_input = Entry(frame_input, width=15, borderwidth=1)
oring_section_input.grid(row=3, column=1)

bore_input = Entry(frame_input, width=15, borderwidth=1)
bore_input.grid(row=4, column=1)

shaft_od_input = Entry(frame_input, width=15, borderwidth=1)
shaft_od_input.grid(row=5, column=1)

groove_dia_input = Entry(frame_input, width=15, borderwidth=1)
groove_dia_input.grid(row=6, column=1)

groove_width_input = Entry(frame_input, width=15, borderwidth=1)
groove_width_input.grid(row=7, column=1)

groove_r_input = Entry(frame_input, width=15, borderwidth=1)
groove_r_input.grid(row=8, column=1)



# Place input box for tolerance section

oring_id_minus_tolerance_input = Entry(frame_input, width=10, borderwidth=1)
oring_id_minus_tolerance_input.grid(row=2, column=2)

oring_id_plus_tolerance_input = Entry(frame_input, width=10, borderwidth=1)
oring_id_plus_tolerance_input.grid(row=2, column=3)

oring_cs_minus_tolerance_input = Entry(frame_input, width=10, borderwidth=1)
oring_cs_minus_tolerance_input.grid(row=3, column=2)

oring_cs_plus_tolerance_input = Entry(frame_input, width=10, borderwidth=1)
oring_cs_plus_tolerance_input.grid(row=3, column=3)

bore_minus_tolerance_input = Entry(frame_input, width=10, borderwidth=1)
bore_minus_tolerance_input.grid(row=4, column=2)

bore_plus_tolerance_input = Entry(frame_input, width=10, borderwidth=1)
bore_plus_tolerance_input.grid(row=4, column=3)

shaft_od_minus_tolerance_input = Entry(frame_input, width=10, borderwidth=1)
shaft_od_minus_tolerance_input.grid(row=5, column=2)

shaft_od_plus_tolerance_input = Entry(frame_input, width=10, borderwidth=1)
shaft_od_plus_tolerance_input.grid(row=5, column=3)

groove_dia_minus_tolerance_input = Entry(frame_input, width=10, borderwidth=1)
groove_dia_minus_tolerance_input.grid(row=6, column=2)

groove_dia_plus_tolerance_input = Entry(frame_input, width=10, borderwidth=1)
groove_dia_plus_tolerance_input.grid(row=6, column=3)

groove_width_minus_tolerance_input = Entry(frame_input, width=10, borderwidth=1)
groove_width_minus_tolerance_input.grid(row=7, column=2)

groove_width_plus_tolerance_input = Entry(frame_input, width=10, borderwidth=1)
groove_width_plus_tolerance_input.grid(row=7, column=3)

groove_r_minus_tolerance_input = Entry(frame_input, width=10, borderwidth=1)
groove_r_minus_tolerance_input.grid(row=8, column=2)

groove_r_plus_tolerance_input = Entry(frame_input, width=10, borderwidth=1)
groove_r_plus_tolerance_input.grid(row=8, column=3)


# Place frame for output section

frame_output = LabelFrame(root, padx=5, pady=5)
frame_output.grid(row=2, column=0, padx=10, pady=10, stick=W + N)

# Place frame for image
frame_image = LabelFrame(root, padx=5, pady=5)
frame_image.grid(row=0, column=1, rowspan=3, padx=10, pady=10, stick=E + N)

my_img = ImageTk.PhotoImage(Image.open("o_ring_ceetak.PNG"))
my_label = Label(frame_image, image=my_img)
my_label.pack()


def stretch_vs_reduction(x):
    if (x>=3):
        y = 0.56 + (0.59 * x) - 0.0046 * math.pow(x, 2)

    else:
        y = 0.01 + (1.06 * x) - 0.1 * math.pow(x, 2)

    return y



def calculate():
    GD = float(groove_dia_input.get())
    BD = float(bore_input.get())
    CS = float(oring_section_input.get())
    ID = float(oring_ID_input.get())
    SO = float(shaft_od_input.get())
    GW = float(groove_width_input.get())
    GR = float(groove_r_input.get())

    GD_MIN = GD - float(groove_dia_minus_tolerance_input.get())
    GD_MAX = GD + float(groove_dia_plus_tolerance_input.get())

    GW_MIN = GW - float(groove_width_minus_tolerance_input.get())
    GW_MAX = GW + float(groove_width_plus_tolerance_input.get())

    GR_MIN = GR - float(groove_r_minus_tolerance_input.get())
    GR_MAX = GR + float(groove_r_plus_tolerance_input.get())

    BD_MIN = BD - float(bore_minus_tolerance_input.get())
    BD_MAX = BD + float(bore_plus_tolerance_input.get())

    ID_MIN = ID - float(oring_id_minus_tolerance_input.get())
    ID_MAX = ID + float(oring_id_plus_tolerance_input.get())

    CS_MIN = CS - float(oring_cs_minus_tolerance_input.get())
    CS_MAX = CS + float(oring_cs_plus_tolerance_input.get())

    SO_MIN = SO - float(shaft_od_minus_tolerance_input.get())
    SO_MAX = SO + float(shaft_od_plus_tolerance_input.get())

    # Calculate o-ring stretch rate
    nom_stretch_rate = (GD-ID)/ID*100
    min_stretch_rate = (GD_MIN - ID_MAX)/ID_MAX*100
    max_stretch_rate = (GD_MAX - ID_MIN)/ID_MIN*100


    nominal_S = str(nom_stretch_rate)
    min_S = str(min_stretch_rate)
    max_S = str(max_stretch_rate)

    nom_cs_reduction = stretch_vs_reduction(nom_stretch_rate)
    min_cs_reduction = stretch_vs_reduction(min_stretch_rate)
    max_cs_reduction = stretch_vs_reduction(max_stretch_rate)

    nom_cs_after_reduction = CS*(1-nom_cs_reduction/100)
    max_cs_after_reduction = CS_MAX*(1-min_cs_reduction/100)
    min_cs_after_reduction = CS_MIN*(1-max_cs_reduction/100)



    min_groove_area = min(GW_MIN*(BD_MIN-GD_MAX)/2 - 2*pow(GR_MAX,2) + 3.142*pow(GR_MAX,2)/2,
                          GW_MIN*(BD_MAX-GD_MIN)/2 - pow(2*GR_MAX,2) + 3.142*pow(GR_MAX,2)/2)
    max_groove_area = max(GW_MAX * (BD_MIN - GD_MAX) / 2 - pow(2*GR_MIN, 2) + 3.142 * pow(GR_MIN, 2) / 2,
                          GW_MAX * (BD_MAX - GD_MIN) / 2 - 2 * pow(GR_MIN, 2) + 3.142 * pow(GR_MIN, 2) / 2)



    min_fill_rate = str(3.142 * pow(min_cs_after_reduction / 2, 2) / max_groove_area*100)
    max_fill_rate = str(3.142 * pow(max_cs_after_reduction / 2, 2) / min_groove_area*100)


    nom_compression_rate = str((nom_cs_after_reduction-(BD-GD)/2)/nom_cs_after_reduction*100)
    min_compression_rate = str((min_cs_after_reduction-(BD_MAX-GD_MIN)/2)/min_cs_after_reduction*100)
    max_compression_rate = str((max_cs_after_reduction-(BD_MIN-GD_MAX)/2)/max_cs_after_reduction*100)

    extrusion_gap = BD_MAX - SO_MIN

    min_ecc_compression_rate = str((min_cs_after_reduction-(SO_MAX-GD_MIN)/2-extrusion_gap)/min_cs_after_reduction*100)
    max_ecc_compression_rate = str((max_cs_after_reduction-(SO_MIN-GD_MAX)/2)/max_cs_after_reduction*100)

    global nominal_compression_result_label
    nominal_compression_result_label = Label(frame_output, text=nom_compression_rate[0:4] + "%")
    nominal_compression_result_label.grid(row=2, column=2, stick=E)

    global min_compression_result_label
    min_compression_result_label = Label(frame_output, text=min_compression_rate[0:4] + "%")
    min_compression_result_label.grid(row=2, column=1, stick=E)

    global max_compression_result_label
    max_compression_result_label = Label(frame_output, text=max_compression_rate[0:4] + "%")
    max_compression_result_label.grid(row=2, column=3, stick=E)


    global min_ecc_compression_result_label
    min_ecc_compression_result_label = Label(frame_output, text=min_ecc_compression_rate[0:4] + "%")
    min_ecc_compression_result_label.grid(row=3, column=1, stick=E)

    global max_ecc_compression_result_label
    max_ecc_compression_result_label = Label(frame_output, text=max_ecc_compression_rate[0:4] + "%")
    max_ecc_compression_result_label.grid(row=3, column=3, stick=E)

    global nominal_stretch_result_label
    nominal_stretch_result_label = Label(frame_output, text=nominal_S[0:4] + "%")
    nominal_stretch_result_label.grid(row=4, column=2, stick=E)

    global min_stretch_result_label
    min_stretch_result_label = Label(frame_output, text=min_S[0:4] + "%")
    min_stretch_result_label.grid(row=4, column=1, stick=E)

    global max_stretch_result_label
    max_stretch_result_label = Label(frame_output, text=max_S[0:4] + "%")
    max_stretch_result_label.grid(row=4, column=3, stick=E)


    global min_housing_fill_result_label
    min_housing_fill_result_label = Label(frame_output, text=min_fill_rate[0:4] + "%")
    min_housing_fill_result_label.grid(row=5, column=1, stick=E)

    global max_housing_fill_result_label
    max_housing_fill_result_label = Label(frame_output, text=max_fill_rate[0:4] + "%")
    max_housing_fill_result_label.grid(row=5, column=3, stick=E)

def clear():
    groove_dia_input.delete(0, END)
    bore_input.delete(0, END)
    oring_ID_input.delete(0, END)
    oring_section_input.delete(0, END)
    shaft_od_input.delete(0,END)

    groove_dia_plus_tolerance_input.delete(0, END)
    groove_dia_minus_tolerance_input.delete(0, END)
    bore_minus_tolerance_input.delete(0, END)
    bore_plus_tolerance_input.delete(0, END)
    oring_id_plus_tolerance_input.delete(0, END)
    oring_id_minus_tolerance_input.delete(0, END)
    oring_cs_plus_tolerance_input.delete(0, END)
    oring_cs_minus_tolerance_input.delete(0, END)
    shaft_od_plus_tolerance_input.delete(0,END)
    shaft_od_minus_tolerance_input.delete(0,END)

    nominal_compression_result_label.destroy()
    min_compression_result_label.destroy()
    max_compression_result_label.destroy()
    nominal_stretch_result_label.destroy()
    min_stretch_result_label.destroy()
    max_stretch_result_label.destroy()

    min_ecc_compression_result_label.destroy()
    max_ecc_compression_result_label.destroy()


# Place label for Output section
output_section_title = Label(frame_output, text="Output Section", font=("", 15))
output_section_title.grid(row=0, column=0, columnspan=4)

min_result_label = Label(frame_output, text="Min")
min_result_label.grid(row=1, column=1)

nominal_result_label = Label(frame_output, text="Nom")
nominal_result_label.grid(row=1, column=2)

max_result_label = Label(frame_output, text="Max")
max_result_label.grid(row=1, column=3)

compression_label = Label(frame_output, text="Compression Rate: ")
compression_label.grid(row=2, column=0, stick=W)

eccentric_compression_label = Label(frame_output, text="Eccentric Compression Rate: ")
eccentric_compression_label.grid(row=3, column=0, stick=W)

stretch_label = Label(frame_output, text="Stretch Rate: ")
stretch_label.grid(row=4, column=0, stick=W)

housing_fill_label = Label(frame_output, text="Housing fill Rate: ")
housing_fill_label.grid(row=5, column=0, stick=W)

# Place button
calculate_button = Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0)

clear_button = Button(root, text="Clear", command=clear)
clear_button.grid(row=3, column=1)


root.mainloop()
