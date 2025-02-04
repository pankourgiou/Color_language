import tkinter as tk
from tkinter import ttk
import math

LETTER_COLORS = {
    'a': '#FF6B6B', 'b': '#4ECDC4', 'c': '#45B7D1', 
    'd': '#96CEB4', 'e': '#FFEEAD', 'f': '#D4A5A5',
    'g': '#9B59B6', 'h': '#3498DB', 'i': '#F1C40F',
    'j': '#E74C3C', 'k': '#2ECC71', 'l': '#E67E22',
    'm': '#1ABC9C', 'n': '#CC66FF', 'o': '#FF99CC',
    'p': '#99CC33', 'q': '#FF9966', 'r': '#66CCFF',
    's': '#FF99FF', 't': '#99CCFF', 'u': '#FFCC99',
    'v': '#99FFCC', 'w': '#FF99CC', 'x': '#CC99FF',
    'y': '#FFCC66', 'z': '#66FFCC'
}

CHARACTER_COLORS = {
    'brackets': '#f08d49',    # (), [], {}
    'operators': '#cc99cd',   # +, -, *, /, =, >, <
    'numbers': '#f8c555',     # 0-9
    'spaces': '#4a4a4a',      # spaces and tabs
    'specials': '#fc929e'     # special characters
}

class BlockVisualizer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Code Blocks Visualizer")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')
        
        self.setup_ui()
        self.current_blocks = []
        
    def get_character_color(self, char):
        lower_char = char.lower()
        if lower_char in LETTER_COLORS:
            return LETTER_COLORS[lower_char]
        if char in '()[]{}':
            return CHARACTER_COLORS['brackets']
        if char in '+-*/=><|&%':
            return CHARACTER_COLORS['operators']
        if char.isdigit():
            return CHARACTER_COLORS['numbers']
        if char.isspace():
            return CHARACTER_COLORS['spaces']
        return CHARACTER_COLORS['specials']
    
    def setup_ui(self):
        # Title
        title = tk.Label(
            self.root,
            text="Code Blocks Visualizer",
            font=('Arial', 24),
            bg='#f0f0f0'
        )
        title.pack(pady=20)
        
        # Frame for blocks
        self.blocks_frame = tk.Frame(
            self.root,
            bg='#f0f0f0',
            width=700,
            height=300
        )
        self.blocks_frame.pack(pady=20)
        self.blocks_frame.pack_propagate(False)
        
        # Input field
        self.input_var = tk.StringVar()
        self.input_var.trace_add('write', self.update_blocks)
        entry = tk.Entry(
            self.root,
            textvariable=self.input_var,
            font=('Arial', 12),
            width=40
        )
        entry.pack(pady=20)
        
        # Set default text
        self.input_var.set("console.log('Hello World!');")
    
    def clear_blocks(self):
        for block in self.current_blocks:
            block.destroy()
        self.current_blocks = []
    
    def update_blocks(self, *args):
        self.clear_blocks()
        text = self.input_var.get()
        
        block_size = 20
        gap = 4
        max_blocks_per_row = 30
        current_row = 0
        current_col = 0
        
        for i, char in enumerate(text):
            if current_col >= max_blocks_per_row:
                current_row += 1
                current_col = 0
            
            # Calculate position with wave effect
            y_offset = math.sin(i * 0.2) * 2
            
            block_frame = tk.Frame(
                self.blocks_frame,
                width=block_size,
                height=block_size,
                bg=self.get_character_color(char)
            )
            
            x_pos = current_col * (block_size + gap) + 10
            y_pos = current_row * (block_size + gap) + 10 + y_offset
            
            block_frame.place(x=x_pos, y=y_pos)
            block_frame.pack_propagate(False)
            
            if char.isspace():
                dot = tk.Label(
                    block_frame,
                    text='·',
                    fg='white',
                    bg=self.get_character_color(char)
                )
                dot.place(relx=0.5, rely=0.5, anchor='center')
            
            self.current_blocks.append(block_frame)
            current_col += 1
    
    def run(self):
        self.root.mainloop()

def main():
    visualizer = BlockVisualizer()
    visualizer.run()

if __name__ == "__main__":
    main()
