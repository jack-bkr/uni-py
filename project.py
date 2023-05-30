import tkinter as tk
from tkinter import ttk

class Wallpaper:
    def __init__(self, pattern, colour, length, extras, premium, lining, paste):
        self.pattern = pattern
        self.colour = colour
        self.length = float(length)
        self.extras = extras
        self.premium = premium
        self.lining = lining
        self.paste = paste
        self.rolls = 0
        self.lRolls = 0
        self.area = 0
        self.tubs = 0
        self.price = 0
        
    def calculate(self):
        self.price = 0
        self.rolls = (float(self.length) // 10.05001) + 1  # calculate number of rolls needed
        self.lRolls = (float(self.length) // 20.00001) + 1  # calculate number of lining rolls needed
        self.area = self.rolls * 10.05 * 0.52    # calculate area of order[orderID] needed
        self.tubs = (self.area // 53) + 1    # calculate number of tubs of paste needed
        
        if (self.extras == 'None'):  # calculate price of extras
            extras = 0
        elif(self.extras == 'Foil'):
            extras = 0.12 * self.rolls * 10.05
        elif(self.extras == 'Glitter'):
            extras = 0.18 * self.rolls * 10.05
        elif(self.extras == 'Embossing'):
            extras = 0.06 * self.rolls * 10.05
        extras = round(extras, 2)
        
        paper = 0.003 * self.rolls * 52260    # calculate price of paper
        if(self.premium):    # calculate price of premium paper
            paper = 0.006 * self.rolls * 52260
        
        lining = 0
        if(self.lining):    # calculate price of lining
            lining = 7.63 * self.lRolls
            self.tubs = 2 * self.tubs
            
        paste = 0
        if(self.paste): # calculate price of paste
            paste = self.tubs * 13.99
        
        self.price = extras + paper + lining + paste # calculate total price
        
        return self.price
            

colours = ['gold', 'lightSeaGreen',  'darkSlateGray4', 'deepSkyBlue', 'purple', 'violetRed2']

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
def createWallpaperPreview(id):
    previewCanvas.delete("all")
    print("col: " + order[id].colour + ", pat: " + order[id].pattern + ",id: " + str(id))
    if(order[id].pattern == 'pattern 1'):   # Checks which pattern is selected
        createPattern1(previewCanvas, order[id].colour)
    else:
        createPattern2(previewCanvas, order[id].colour)
        
# Create Options
def createOptions():
    global premium, lining, paste, lblPrice, cmbOrders
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
    
    btnCalculate = tk.Button(frame, text='Calculate', command=calculate)    # create button for calculate
    btnCalculate.grid(row=5, column=0, padx=10, pady=1)
    
    lblTotal = tk.Label(frame, text='Total:')   # create label for total
    lblTotal.grid(row=6, column=0, padx=10, pady=1)
    
    lblPrice = tk.Label(frame, text='£0.00') # create label for price
    lblPrice.grid(row=6, column=1, padx=10, pady=1)
    
    orderFrame = tk.Frame(root, name='order frame')    # initialise frame for order
    orderFrame.grid(row=2, column=0, padx=10, pady=10)
    
    cmbOrders = ttk.Combobox(orderFrame, name='orders', width=20, text='1', values=[1], state='readonly')    # create combobox for orders
    cmbOrders.grid(row=0, column=0, padx=10, pady=10)
    cmbOrders.current(0)
    cmbOrders.bind("<<ComboboxSelected>>", optChange)
    
    btnAddOrder = tk.Button(orderFrame, text='Add Order', command=addOrder)    # create button for add order
    btnAddOrder.grid(row=0, column=1, padx=10, pady=10)

# Calculate Wallpaper Price
def calculate():
    lblPrice.config(text='£' + str(order[orderID].calculate()))    # set price label to price

def addOrder():
    global orderID
    order.append(Wallpaper('pattern 1', 'gold', 10, 'None', False, False, False))
    orderID = order[len(order) - 1].orderID
    orders = []
    for i in range(len(order)):
        orders.append(i+1)
    cmbOrders.config(values=orders)
    cmbOrders.current(orderID)
    createWallpaperPreview(orderID)

# Options Change Event handler

def optChange(event):
    global orderID
    if(event.widget._name == 'length'):
        order[orderID].length = event.widget.get()   # get length from entry
        print(order[orderID].length)
        
    elif(event.widget._name == 'extras'):
        order[orderID].extras = event.widget.get()   # get extras from combobox
        print(order[orderID].extras)
        
    elif(event.widget._name == 'premium'):
        if(premium.get() == 0): # get premium from checkbox
            order[orderID].premium = True
        else:
            order[orderID].premium = False
        print("premium: " + str(order[orderID].premium))
        
    elif(event.widget._name == 'lining'):
        if(lining.get() == 0):  # get lining from checkbox
            order[orderID].lining = True
        else:
            order[orderID].lining = False
        print("lining: " + str(order[orderID].lining))
        
    elif(event.widget._name == 'paste'):
        if(paste.get() == 0):   # get paste from checkbox
            order[orderID].paste = True
        else:
            order[orderID].paste = False
        print("paste: " + str(order[orderID].paste))
    
    elif(event.widget._name == 'orders'):
        print("order: " + event.widget.get())
        orderID = int(event.widget.get()) - 1
        createWallpaperPreview(orderID)

# Pattern Click Event handler    
def patClick(event):
    global orderID
    print(event.widget._name + " clicked")
    order[orderID].pattern = event.widget._name
    createWallpaperPreview(orderID)
   
# Colour Click Event handler 
def colClick(event):
    global orderID
    print(event.widget._name + " clicked")
    order[orderID].colour = event.widget._name
    createWallpaperPreview(orderID)

orderID = 0
order = []
order.append(Wallpaper('pattern 1', 'gold', 0, 'None', False, False, False))

createCanvas()
createColourPicker()
createOptions()
createWallpaperPreview(orderID)

root.mainloop()

