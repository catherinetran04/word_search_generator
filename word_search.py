import random
import string

# Define directions as constants for better readability
DIRECTIONS = {
    "right": (1, 0),
    "down": (0, 1),
    "right_down": (1, 1),
    "right_up": (1, -1),
    "left": (-1, 0),
    "up": (0, -1),
    "left_down": (-1, 1),
    "left_up": (-1, -1)
}

def get_size(grid):
    """Get the size of the word search grid."""
    return len(grid[0]), len(grid)

def print_word_grid(grid):
    """Print the word search grid."""
    for row in grid:
        print("".join(row))

def copy_word_grid(grid):
    """Create a copy of the grid."""
    return [row[:] for row in grid]

def extract(grid, position, direction, max_len):
    """Extract a word from the grid given its start position and direction."""
    word = []
    for i in range(max_len):
        x = position[0] + (i * direction[0])
        y = position[1] + (i * direction[1])
        if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
            word.append(grid[y][x])
        else:
            break
    return "".join(word)

def show_solution(grid, word, solution):
    """Highlight the found word in the grid."""
    if not solution:
        print(f"{word} is not found in this word search.")
        return
    
    sol_grid = copy_word_grid(grid)
    for i in range(len(word)):
        x = solution[0][0] + (i * solution[1][0])
        y = solution[0][1] + (i * solution[1][1])
        sol_grid[y][x] = sol_grid[y][x].upper()

    print(f"{word.upper()} can be found as below:")
    print_word_grid(sol_grid)

def find(grid, word):
    """Find the word in the grid in all possible directions."""
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            for direction in DIRECTIONS.values():
                if extract(grid, (x, y), direction, len(word)) == word:
                    return (x, y), direction
    return False

def find_all(grid, words):
    """Find all words in the grid."""
    return {word: find(grid, word) for word in words}

def can_place_word(grid, word, start, direction):
    """Check if a word can be placed at a given position and direction."""
    for i in range(len(word)):
        x = start[0] + i * direction[0]
        y = start[1] + i * direction[1]
        if not (0 <= x < len(grid[0]) and 0 <= y < len(grid)):
            return False
        if grid[y][x] not in ("", word[i]):
            return False
    return True

def place_word(grid, word, start, direction):
    """Place the word in the grid at the given position and direction."""
    for i in range(len(word)):
        x = start[0] + i * direction[0]
        y = start[1] + i * direction[1]
        grid[y][x] = word[i]

def generate(width, height, words):
    """Generate a word search grid with the given words."""
    grid = [["" for _ in range(width)] for _ in range(height)]
    words_found = []

    for word in words:
        placed = False
        for _ in range(100):  # Attempt to place the word 100 times
            start = (random.randrange(width), random.randrange(height))
            direction = random.choice(list(DIRECTIONS.values()))
            if can_place_word(grid, word, start, direction):
                place_word(grid, word, start, direction)
                words_found.append(word)
                placed = True
                break

        if not placed:
            print(f"Could not place the word: {word}")

    # Fill empty cells with random letters
    for y in range(height):
        for x in range(width):
            if grid[y][x] == "":
                grid[y][x] = random.choice(string.ascii_lowercase)

    return grid, words_found

if __name__ == "__main__":
    grid, words_placed = generate(10, 5, ['cat', 'dog', 'art', 'town', 'den', 'wolf', 'part', 'mansion'])
    print("Generated Word Search Grid:")
    print_word_grid(grid)
    print("\nWords placed:", words_placed)
