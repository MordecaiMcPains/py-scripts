import tkinter as tk
from tkinter import filedialog
from PIL import Image


def set_color(color):
    """Function to set the selected color"""
    global selected_color
    selected_color = color


class PixelArtUI:
    def __init__(self, master):
        self.master = master
        self.canvas_width = 500
        self.canvas_height = 500
        self.pixel_size = 20
        self.zoom_scale = 1.0
        self.create_widgets()

    def create_widgets(self):
        # Create a canvas to draw the pixels on
        self.canvas = tk.Canvas(self.master, width=self.canvas_width, height=self.canvas_height, bg='white',
                                scrollregion=(0, 0, self.canvas_width, self.canvas_height))
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Define the available colors
        self.colors = ['black', 'red', 'green', 'blue', 'cyan', 'magenta', 'yellow']

        # Set the initial color
        global selected_color
        selected_color = self.colors[0]

        # Create an 8x8 grid of pixels
        for i in range(32):
            for j in range(32):
                # Calculate the coordinates for the pixel
                x1 = i * self.pixel_size
                y1 = j * self.pixel_size
                x2 = x1 + self.pixel_size
                y2 = y1 + self.pixel_size
                # Draw the pixel on the canvas
                pixel = self.canvas.create_rectangle(x1, y1, x2, y2, fill='white')

        # Create a frame to hold the color selection buttons
        color_frame = tk.Frame(self.master)
        color_frame.pack()

        # Create a button for each color
        for color in self.colors:
            button = tk.Button(color_frame, bg=color, width=2, command=lambda c=color: set_color(c))
            button.pack(side=tk.LEFT)

        # Create the "Clear", "Fill", and "Save as JPG" buttons
        clear_button = tk.Button(self.master, text="Clear", command=self.clear_canvas)
        clear_button.pack(side=tk.LEFT, padx=5)

        fill_button = tk.Button(self.master, text="Fill", command=self.fill_canvas)
        fill_button.pack(side=tk.LEFT, padx=5)

        save_button = tk.Button(self.master, text="Save as JPG", command=self.save_canvas)
        save_button.pack(side=tk.LEFT, padx=5)

        # Create the zoom slider
        self.zoom_label = tk.Label(self.master, text='Zoom')
        self.zoom_label.pack(side=tk.LEFT, padx=5)

        self.zoom_slider = tk.Scale(self.master, from_=5, to=0.2, resolution=0.1, orient=tk.HORIZONTAL,
                                    command=self.on_zoom_slide)
        self.zoom_slider.pack(side=tk.LEFT, padx=5)
        self.zoom_slider.set(1.0)

        # Bind the left mouse button click and drag event to the whole canvas
        self.canvas.bind('<B1-Motion>', self.on_pixel_drag)

        # Bind the mouse wheel event to the canvas
        self.canvas.bind("<MouseWheel>", self.on_mousewheel)

        # Bind the middle mouse button event to the canvas
        self.canvas.bind("<Button-2>", self.on_middle_button_press)
        self.canvas.bind("<B2-Motion>", self.on_middle_button_drag)
        self.canvas.bind("<ButtonRelease-2>", self.on_middle_button_release)

        # Disable the maximize screen button
        self.master.resizable(False, False)

    def on_pixel_drag(self, event):
        """Function called when a pixel is being dragged"""

        # Find the closest pixel to the current mouse position and change its color
        closest_pixel = self.canvas.find_closest(event.x, event.y)[0]
        self.canvas.itemconfig(closest_pixel, fill=selected_color)

    def clear_canvas(self):
        """Function to clear the canvas"""

        # Set all pixels to white
        for pixel in self.canvas.find_withtag('all'):
            self.canvas.itemconfig(pixel, fill='white')

    def fill_canvas(self):
        """Function to fill the canvas with the selected color"""

        # Set all pixels to the selected color
        for pixel in self.canvas.find_withtag('all'):
            self.canvas.itemconfig(pixel, fill=selected_color)

    def save_canvas(self):
        """Function to save the canvas as a JPEG file"""

        # Get the file path where the user wants to save the file
        file_path = filedialog.asksaveasfilename(defaultextension='.jpg')

        if file_path:
            # Create an image from the canvas and save it as a JPEG file
            canvas_image = Image.new('RGB', (self.canvas_width, self.canvas_height), 'white')
            canvas_image.putdata(self.canvas.find_enclosed(0, 0, self.canvas_width, self.canvas_height))
            canvas_image.save(file_path)

    def on_zoom_slide(self, val):
        """Function to handle zoom slider value change"""

        # Update the zoom scale and apply the new scale to the canvas
        self.zoom_scale = float(val)
        self.canvas.scale(tk.ALL, 0, 0, self.zoom_scale, self.zoom_scale)

    def on_mousewheel(self, event):
        """Function called when the mouse wheel is scrolled"""

        # Update the zoom slider and apply the new scale to the canvas
        self.zoom_scale *= 1.0 + event.delta / 1000.0
        self.zoom_slider.set(self.zoom_scale)
        self.canvas.scale(tk.ALL, event.x, event.y, 1.0 + event.delta / 1000.0, 1.0 + event.delta / 1000.0)

    def on_middle_button_press(self, event):
        """Function called when the middle mouse button is pressed"""

        # Activate the canvas panning mode
        self.canvas.config(cursor='fleur')
        self.canvas.scan_mark(event.x, event.y)
        self.middle_press_x = event.x
        self.middle_press_y = event.y

    def on_middle_button_drag(self, event):
        """Function called when the middle mouse button is being dragged"""

        # Calculate the difference between the current and previous mouse positions
        diff_x = event.x - self.middle_press_x
        diff_y = event.y - self.middle_press_y

        # Pan the canvas in the direction of the mouse
        self.canvas.scan_dragto(event.x, event.y, gain=1)
        self.canvas.move('grid', -diff_x, -diff_y)

        # Update the middle press coordinates for the next drag event
        self.middle_press_x = event.x
        self.middle_press_y = event.y

    def on_middle_button_release(self, event):
        """Function called when the middle mouse button is released"""

        # Deactivate the canvas panning mode
        self.canvas.config(cursor='arrow')

    def get_pixel_coords(self, pixel):
        """Function to get the (x, y) coordinates of a pixel on the canvas"""
        x1, y1, x2, y2 = self.canvas.coords(pixel)
        x = int(x1 / self.pixel_size)
        y = int(y1 / self.pixel_size)
        return x, y


root = tk.Tk()
app = PixelArtUI(root)
root.mainloop()