import tkinter as tk
from tkinter import ttk

def recommend_channels():
    selected_genre = genre_var.get()
    recommendations = [channel for channel, genre in channels.items() if genre == selected_genre]
    result_var.set(", ".join(recommendations))

# Create the main window
root = tk.Tk()
root.title("TV Channel Recommendations")

# List of TV channels and their genres
channels = {
    "BBC": "News",
    "CNN": "News",
    "Discovery": "Documentary",
    "National Geographic": "Documentary",
    "HBO": "Entertainment",
    "ESPN": "Sports"
}

# Create a StringVar to hold the selected genre
genre_var = tk.StringVar(root)
genre_var.set("News")  # Set the default value

# Create a StringVar to hold the recommendation result
result_var = tk.StringVar(root)

# Create a label and OptionMenu for genre selection
genre_label = tk.Label(root, text="Select Genre:")
genre_label.pack(pady=5)
genre_menu = ttk.Combobox(root, textvariable=genre_var, values=list(set(channels.values())))
genre_menu.pack(pady=5)

# Create a button to get recommendations
recommend_button = tk.Button(root, text="Get Recommendations", command=recommend_channels)
recommend_button.pack(pady=10)

# Create a label to display the recommendations
result_label = tk.Label(root, textvariable=result_var)
result_label.pack(pady=10)

# Run the application
root.mainloop()
