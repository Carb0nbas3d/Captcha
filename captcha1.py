import PySimpleGUI as sg
import os
import random

tags = {}
image = []
for root, dirs ,files in os.walk("captchacontent"):
    for f in files:
        if f[-4:] == ".png":
            image.append(os.path.join(root, f))
            taglist = f[:-4].split("_")
            for t in taglist:
                if t in tags:
                    tags[t].append(image[-1])
                else:
                    tags[t] = [image[-1]]

print("alle meine image names",image)
print(tags)

#suche tag mit min 3 einträgen
tlist = [t for t in tags.keys() if len(tags[t]) > 2]
print(tlist)

good_tag = random.choice((tlist))
print("good tag", good_tag)

bad_list = []
#print(random.choice(bad_list))

for name in image:
    if good_tag not in name:
        bad_list.append(name)

#print("alle meine image names (2)",    image)  
print("bad list",bad_list)  
bad_image = random.choice(bad_list)

good_images = tags[good_tag][:]
random.shuffle(good_images)
good_images = good_images[:3]
good_images.insert(random.randint(0,3), bad_image)

sg.change_look_and_feel('DarkAmber')    # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text(key="k", text="welches bild ist NICHT mit dem folgenden begriff assoziert: {}".format(good_tag), size=(60,1),  font=("Helvetica", 25))],
            
            [sg.Button("0", button_color=sg.TRANSPARENT_BUTTON,
               image_filename=good_images[0], image_size=(250,250)),
            sg.Button("1", button_color=sg.TRANSPARENT_BUTTON,
               image_filename=good_images[1], image_size=(250,250)),
            sg.Button("2", button_color=sg.TRANSPARENT_BUTTON,
               image_filename=good_images[2], image_size=(250,250)),
            sg.Button("3", button_color=sg.TRANSPARENT_BUTTON,
               image_filename=good_images[3], image_size=(250,250)),
             ],
            [sg.Text(key="r", text="Result"), sg.Button(key="x", button_color=sg.TRANSPARENT_BUTTON, image_filename=os.path.join("results", "result_neutral.png"), image_size = (250, 250))],
            [sg.Text('Bravo richtig'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
        break
    print(event, values)
    if event in ("0","1","2","3"):
        i = int(event)
        if good_images[i] == bad_image:
            print("Bravo richtig")
            window["r"].update("good123")
            window["x"].update(image_filename=os.path.join("results", "result_good.png"))
            sg.Popup('This is my first Popup')

        else:
            print("01100110 01100001 01101100 01110011 01100011 01101000") 
            window["r"].update("bad")
            window["x"].update(image_filename=os.path.join("results", "result_bad.png"))
            sg.Popup("blkjasöldkjf")
        #--- wieder bereit für nächste Frage
        window["r"].update("result")
        window["x"].update(image_filename=os.path.join("results","result_neutral.png"))
        good_tag = random.choice((tlist))
        print("good tag", good_tag)

        bad_list = []
        #print(random.choice(bad_list))

        for name in image:
            if good_tag not in name:
                bad_list.append(name)

        #print("alle meine image names (2)",    image)  
        print("bad list",bad_list)  
        bad_image = random.choice(bad_list)
        good_images = tags[good_tag][:]
        random.shuffle(good_images)
        print("-----good images -----")
        good_images = good_images[:3]
        
        good_images.insert(random.randint(0,3), bad_image)
        print(good_images)
        
        
        window["k"].update("welches bild ist NICHT mit dem folgenden begriff assoziert: {}".format(good_tag))
        window["0"].update(image_filename=good_images[0])
        window["1"].update(image_filename=good_images[1])
        window["2"].update(image_filename=good_images[2])
        window["3"].update(image_filename=good_images[3])


 
window.close()
