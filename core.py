import tkinter as tk
from tkinter import ttk, messagebox
import random
import time

# Initialize the Tkinter window
root = tk.Tk()
root.title("Sorting Algorithm Visualizer")

# Frame for algorithm selection and other controls
control_frame = ttk.Frame(root, padding="10")
control_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

# Dropdown menu for algorithm selection
algorithm_label = ttk.Label(control_frame, text="Algorithm:")
algorithm_label.grid(row=0, column=0, sticky=tk.W)
algorithm_var = tk.StringVar()
algorithm_options = ["Bubble Sort", "Selection Sort", "Insertion Sort"]
algorithm_dropdown = ttk.Combobox(control_frame, textvariable=algorithm_var, values=algorithm_options, state="readonly")
algorithm_dropdown.grid(row=0, column=1, sticky=(tk.W, tk.E))
algorithm_dropdown.current(0)

# Slider for array size
array_size_label = ttk.Label(control_frame, text="Array Size:")
array_size_label.grid(row=2, column=0, sticky=tk.W)
array_size_var = tk.IntVar(value=50)
array_size_slider = ttk.Scale(control_frame, from_=10, to=100, variable=array_size_var, orient="horizontal")
array_size_slider.grid(row=2, column=1, sticky=(tk.W, tk.E))

# Label to show the current array size
array_size_value_label = ttk.Label(control_frame, text="")
array_size_value_label.grid(row=2, column=2)
def update_array_size_label(event=None):
    array_size_value_label["text"] = str(array_size_var.get())
array_size_slider.bind("<Motion>", update_array_size_label)

# Slider for sorting speed
speed_label = ttk.Label(control_frame, text="Speed:")
speed_label.grid(row=3, column=0, sticky=tk.W)
speed_var = tk.IntVar(value=1)
speed_slider = ttk.Scale(control_frame, from_=1, to=10, variable=speed_var, orient="horizontal")
speed_slider.grid(row=3, column=1, sticky=(tk.W, tk.E))

# Label to show the current speed
speed_value_label = ttk.Label(control_frame, text="")
speed_value_label.grid(row=3, column=2)
def update_speed_label(event=None):
    speed_value_label["text"] = str(speed_var.get())
speed_slider.bind("<Motion>", update_speed_label)

# Start and Stop buttons
def start_sorting():
    arr = generate_array()
    algo = algorithm_var.get()
    if algo == "Bubble Sort":
        bubble_sort(arr)
    elif algo == "Selection Sort":
        selection_sort(arr)
    elif algo == "Insertion Sort":
        insertion_sort(arr)

start_button = ttk.Button(control_frame, text="Start", command=start_sorting)
start_button.grid(row=4, column=0, sticky=(tk.W, tk.E))

stop_button = ttk.Button(control_frame, text="Stop", command=lambda: print("Stop Sorting"))
stop_button.grid(row=4, column=1, sticky=(tk.W, tk.E))

# [?] button for algorithm explanations
def show_algorithm_info():
    algo = algorithm_var.get()
    info = f"Information about {algo} will be shown here."
    tk.messagebox.showinfo("Algorithm Info", info)

info_button = ttk.Button(control_frame, text="?", command=show_algorithm_info)
info_button.grid(row=0, column=2)

# Canvas for sorting visualization
canvas = tk.Canvas(root, bg="black", height=600, width=800)
canvas.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Generate an array of random integers
def generate_array():
    array_size = array_size_var.get()
    return [random.randint(1, 100) for _ in range(array_size)]

# Draw the array as bars on the canvas
def draw_array(arr):
    canvas.delete("all")
    canvas_height = 600
    canvas_width = 800
    bar_width = canvas_width // len(arr)
    
    for i, val in enumerate(arr):
        bar_height = val * 6
        canvas.create_rectangle(i * bar_width, canvas_height, (i + 1) * bar_width, canvas_height - bar_height, fill="blue")

# Function to regenerate and redraw the array when the slider changes
def update_array(event=None):
    new_array = generate_array()
    draw_array(new_array)

# Attach the update_array function to the array size slider
array_size_slider.bind("<Motion>", update_array)

# Bubble Sort with visualization
def bubble_sort_iteration(arr, i, n):
    swapped = False
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swapped = True

    draw_array(arr)

    if not swapped:
        return

    root.after(100, bubble_sort_iteration, arr, i+1, n)

def bubble_sort(arr):
    bubble_sort_iteration(arr, 0, len(arr))

# Selection Sort with visualization
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        draw_array(arr)
        root.after(100)

# Insertion Sort with visualization
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        draw_array(arr)
        root.after(100)

# Generate and draw an initial array when the program starts
initial_array = generate_array()
draw_array(initial_array)

# Start the Tkinter event loop
root.mainloop()
