import tkinter as tk
from tkinter import ttk

class Wallpaper:
    def __init__(self, pattern, colour, length, extras, premium, lining, paste):
        self.pattern = pattern
        self.colour = colour
        self.length = length
        self.extra = extras
        self.premium = premium
        self.lining = lining
        self.paste = paste


colours = ['gold','lightSeaGreen',  'darkSlateGray4', 'deepSkyBlue', 'purple', 'violetRed2']

# init GUI
root = tk.Tk()
root.title("DIY Wallpaper")

# Create Canvas
def createCanvas():
    global previewCanvas
    
    p1Canvas = tk.Canvas(root, width=100, height=100, name='pattern 1')  # initialise canvas for pattern 1
    p1Canvas.grid(row=0, column=0, padx=10 ,pady=10)
    p1Canvas.bind("<Button>", patClick)
    createPattern1(p1Canvas, 'grey')
    
    p2Canvas = tk.Canvas(root, width=100, height=100, name='pattern 2')  # initialise canvas for pattern 2
    p2Canvas.grid(row=0, column=1, padx=10, pady=10)
    p2Canvas.bind("<Button>", patClick)
    createPattern2(p2Canvas, 'grey')
    
    previewCanvas = tk.Canvas(root, width=100, height=100, name='preview')  # initialise canvas for preview
    previewCanvas.grid(row=0, column=2, padx=10, pady=10)

# Create Pattern 1
def createPattern1(canvas, colour):
    fillCol = colour

    stagger = 20    # stagger each column
    for i in range(0, 100, 20):    # 
        if(stagger == 20):
            stagger = 0
        else:
            stagger = 20
        for j in range(0, 100-stagger, 40):
            canvas.create_rectangle(j+20+stagger, i+20 , j+stagger, i, outline='black', fill=fillCol)    # create rectangle 20px x 20px

# Create Pattern 2
def createPattern2(canvas, colour):
    fillCol = 'white'

    for i in range(0, 100, 20):
        if(colour == fillCol):  # alternate colour
            fillCol = 'white'
        else:
            fillCol = colour
            
        canvas.create_polygon((i/2), 100, 50, i, 100-(i/2), 100, outline='black', fill=fillCol)    # create triangles progressively smaller
    
# Create Colour Picker
def createColourPicker():
    frame = tk.Frame(root, name='colour picker')    # initialise frame for colour picker
    frame.columnconfigure(0, weight=2)
    frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    
    for i in range(len(colours)):   # create colour picker
        colour = tk.Canvas(frame, width=20, height=20, name=colours[i].lower())
        colour.grid(row=0, column=i, padx=10, pady=10)
        colour.create_rectangle(0, 0, 20, 20, outline='black', fill=colours[i]) # create different coloured rectangles 20px x 20px
        colour.bind("<Button>", colClick)

# Create Wallpaper Preview
def createWallpaperPreview():
    previewCanvas.delete("all")
    if(wallpaper.pattern == 'pattern 1'):   # Checks which pattern is selected
        createPattern1(previewCanvas, wallpaper.colour)
    else:
        createPattern2(previewCanvas, wallpaper.colour)
        
# Create Options
def createOptions():
    global premium, lining, paste
    premium = tk.IntVar()
    lining = tk.IntVar()
    paste = tk.IntVar()
    
    frame = tk.Frame(root, name='options')    # initialise frame for options
    frame.grid(row=1, column=2, padx=10, pady=10, rowspan=2)
    
    lblLength = tk.Label(frame, text='Length (m):') # create label for length
    lblLength.grid(row=0, column=0, padx=10, pady=1)
    
    entryLength = tk.Entry(frame, name='length', width=20)  # create entry for length
    entryLength.grid(row=0, column=1, padx=10, pady=1)
    entryLength.bind("<KeyRelease>", optChange)
    
    lblExtras = tk.Label(frame, text='Extras:') # create label for extras
    lblExtras.grid(row=1, column=0, padx=10, pady=1)
    
    cmbExtras = ttk.Combobox(frame, name='extras', width=17, text='None', values=['None', 'Foil', 'Glitter', 'Embossing'], state='readonly')    # create combobox for extras
    cmbExtras.grid(row=1, column=1, padx=10, pady=1)
    cmbExtras.current(0)
    cmbExtras.bind("<<ComboboxSelected>>", optChange)
    
    lblPremium = tk.Label(frame, text='Premium Paper:') # create label for premium paper
    lblPremium.grid(row=2, column=0, padx=10, pady=1)
    
    chkPremium = tk.Checkbutton(frame, name='premium', variable=premium)  # create checkbox for premium paper
    chkPremium.grid(row=2, column=1, padx=10, pady=1)
    chkPremium.bind("<Button>", optChange)
    
    lblLining = tk.Label(frame, text='Wallpaper Lining:')   # create label for lining
    lblLining.grid(row=3, column=0, padx=10, pady=1)
    
    chkLining = tk.Checkbutton(frame, name='lining', variable=lining)    # create checkbox for lining
    chkLining.grid(row=3, column=1, padx=10, pady=1)
    chkLining.bind("<Button>", optChange)
    
    lblPaste = tk.Label(frame, text='Wallpaper Paste:') # create label for paste
    lblPaste.grid(row=4, column=0, padx=10, pady=1)
    
    chkPaste = tk.Checkbutton(frame, name='paste', variable=paste)  # create checkbox for paste
    chkPaste.grid(row=4, column=1, padx=10, pady=1)
    chkPaste.bind("<Button>", optChange)

# Options Change Event handler

def optChange(event):
    if(event.widget._name == 'length'):
        wallpaper.length = event.widget.get()   # get length from entry
        print(wallpaper.length)
        
    elif(event.widget._name == 'extras'):
        wallpaper.extras = event.widget.get()   # get extras from combobox
        print(wallpaper.extras)
        
    elif(event.widget._name == 'premium'):
        if(premium.get() == 0): # get premium from checkbox
            wallpaper.premium = True
        else:
            wallpaper.premium = False
        print("premium: " + str(wallpaper.premium))
        
    elif(event.widget._name == 'lining'):
        if(lining.get() == 0):  # get lining from checkbox
            wallpaper.lining = True
        else:
            wallpaper.lining = False
        print("lining: " + str(wallpaper.lining))
        
    elif(event.widget._name == 'paste'):
        if(paste.get() == 0):   # get paste from checkbox
            wallpaper.paste = True
        else:
            wallpaper.paste = False
        print("paste: " + str(wallpaper.paste))

# Pattern Click Event handler    
def patClick(event):
    print(event.widget._name + " clicked")
    wallpaper.pattern = event.widget._name
    createWallpaperPreview()
   
# Colour Click Event handler 
def colClick(event):
    print(event.widget._name + " clicked")
    wallpaper.colour = event.widget._name
    createWallpaperPreview()
    
wallpaper = Wallpaper('pattern 1', 'gold', 10, 'None', False, False, False)

createCanvas()
createColourPicker()
createOptions()

root.mainloop()

