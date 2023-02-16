from PIL import Image
from tkinter.filedialog import askopenfilename as aof


loop = True
while loop:
    file = aof(title="File Select")
    if file:
        pass
    else:
        quit()

    imageQuality = int(input(
        "Enter the quality of the compressed image (30 is recommended but feel free to experiment. You might have to compress the photo again): "))
    imageName = input(
        "Enter the name of the file: ")

    img = Image.open(file)

    if not imageName:
        imageName = img.filename+'.'+img.format.lower()

    img.save(fp=imageName, quality=imageQuality, optimize=True)

    yn = input("Do you want to compress another file yes/no?: ").lower()

    if yn == "yes" | yn == "y":
        loop = True
    elif yn == "no" | yn == "n":
        loop = False
    else:
        quit()
