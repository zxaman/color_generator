import tkinter as tk

def generate_color():
    red = red_scale.get()
    green = green_scale.get()
    blue = blue_scale.get()
    
    color_frame.config(bg=f"#{red:02x}{green:02x}{blue:02x}")
    color_label.config(text=f"Color: #{red:02x}{green:02x}{blue:02x}")
    rgb_label.config(text=f"RGB: ({red}, {green}, {blue})")

# Create the main window
window = tk.Tk()
window.title("Color Generator")

# Create the red scale
red_label = tk.Label(window, text="Red")
red_label.pack()
red_scale = tk.Scale(window, from_=0, to=255, orient=tk.HORIZONTAL)
red_scale.pack()

# Create the green scale
green_label = tk.Label(window, text="Green")
green_label.pack()
green_scale = tk.Scale(window, from_=0, to=255, orient=tk.HORIZONTAL)
green_scale.pack()

# Create the blue scale
blue_label = tk.Label(window, text="Blue")
blue_label.pack()
blue_scale = tk.Scale(window, from_=0, to=255, orient=tk.HORIZONTAL)
blue_scale.pack()

# Create the generate button
generate_button = tk.Button(window, text="Generate", command=generate_color)
generate_button.pack()

# Create the color frame
color_frame = tk.Frame(window, width=200, height=200)
color_frame.pack()

# Create the color label
color_label = tk.Label(window, text="Color: #000000")
color_label.pack()

# Create the RGB label
rgb_label = tk.Label(window, text="RGB: (0, 0, 0)")
rgb_label.pack()

# Start the main event loop
window.mainloop()
