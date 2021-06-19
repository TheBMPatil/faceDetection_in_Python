from tkinter import *
from tkinter import messagebox, Label, Button
import face_recognition
from PIL import Image, ImageDraw

top = Tk()
# size
top.title('Face Detection App')
top.geometry("500x400")
selimg:Label= Label(top,
                      text="Click the Button to detect Faces",
                      font=("Eras Demi ITC", "20")).place(x=50,y=50)


def detectface():
    messagebox.showinfo("DetectFace", message="Detecting Faces")
    test_image = face_recognition.load_image_file('./face_data/test1.jpg')
    face_locations = face_recognition.face_locations(test_image)
    pil_image = Image.fromarray(test_image)
    draw = ImageDraw.Draw(pil_image)

    # Loop through faces in test image
    for (t, r, b, l), face_encoding in zip(face_locations, test_image):
        #  Draw Box
        draw.rectangle(((l, t), (r, b)), outline=(0, 750, 0), width=3)
        # Draw label
    del draw
    # Display image
    pil_image.show()


findface: Button = Button(top,
                          text="Detect face"
                          , command=detectface).place(x=200, y=200)

# Entering the event main loop
top.mainloop()
