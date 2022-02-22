import tkinter as tk

HEIGHT = 700
WIDTH = 800

#this is the stuff we want to put into the label
def format_responce(student):
    name = student['jim']
    return name
    
    
#this is the stuff that the button one does
def get_students(student):
    print("Button clicked")
    
    label['text'] = format_responce(student)
    

#this is the made GUI
root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='background.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='red', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.4, relheight=1)

button1 = tk.Button(frame, text="Check Student", font=40, command=get_students)
button1.place(relx=0.7, relheight=1, relwidth=0.3)

#button2 = tk.Button(frame, text="Add Student", font=40, command=add_student)
#button2.place(relx=0.45, relheight=1, relwidth=0.2)

lower_frame = tk.Frame(root, bg='red', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor ='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()


