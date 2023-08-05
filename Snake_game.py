import tkinter as tk
import random

# Constants
WIDTH = 400
HEIGHT = 400
GRID_SIZE = 20

class SnakeGame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Snake Game")
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.resizable(0, 0)

        self.canvas = tk.Canvas(self, bg="black", width=WIDTH, height=HEIGHT)
        self.canvas.pack()

        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.food = self.generate_food()
        self.direction = "Right"

        self.bind("<Key>", self.change_direction)

        self.score = 0
        self.score_label = tk.Label(self, text=f"Score: {self.score}")
        self.score_label.pack()

        self.update()

    def generate_food(self):
        x = random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        y = random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        return x, y

    def change_direction(self, event):
        if event.keysym == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif event.keysym == "Down" and self.direction != "Up":
            self.direction = "Down"
        elif event.keysym == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif event.keysym == "Right" and self.direction != "Left":
            self.direction = "Right"

    def update(self):
        head_x, head_y = self.snake[0]
        if self.direction == "Up":
            head_y -= GRID_SIZE
        elif self.direction == "Down":
            head_y += GRID_SIZE
        elif self.direction == "Left":
            head_x -= GRID_SIZE
        elif self.direction == "Right":
            head_x += GRID_SIZE

        self.snake.insert(0, (head_x, head_y))

        if self.snake[0] == self.food:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.food = self.generate_food()
        else:
            self.snake.pop()

        self.canvas.delete("all")

        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(
                x, y, x + GRID_SIZE, y + GRID_SIZE, fill="green", outline="black"
            )

        fx, fy = self.food
        self.canvas.create_oval(
            fx, fy, fx + GRID_SIZE, fy + GRID_SIZE, fill="red", outline="black"
        )

        if (
            head_x < 0
            or head_x >= WIDTH
            or head_y < 0
            or head_y >= HEIGHT
            or (head_x, head_y) in self.snake[1:]
        ):
            self.canvas.create_text(
                WIDTH // 2, HEIGHT // 2, text="Game Over", fill="white", font=("Arial", 20)
            )
        else:
            self.after(100, self.update)

game = SnakeGame()
game.mainloop()
