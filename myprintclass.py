import requests
from bs4 import BeautifulSoup

def fetch_google_doc(url):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text(separator="\n")  # Keeps line breaks
    
    coord_chunk=[]
    cordinates=[]
    start_of_message=0
    lines = text.splitlines()
    for idx, line in enumerate(lines):
        if line.strip() == "y-coordinate":
            lines = lines[idx + 1:]  # Skip the header line
            break

    seperator=1
    for line in lines:
        coord_chunk.append(line)
        if seperator==3:
            seperator=0
            cordinates.append(coord_chunk)
            coord_chunk=[]
        seperator+=1    
        

    return cordinates

def create_character_grid(lines):
    grid_map = {}
    max_x = max_y = 0

    for line in lines:
        char = line[1]
        x_str= line[0]
        y_str= line[2]
        x, y = int(x_str), int(y_str)
        grid_map[(x, y)] = char
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    # Build the 2D grid
    grid = []
    for y in range(max_y + 1):
        row = []
        for x in range(max_x + 1):
            row.append(grid_map.get((x, y), " "))#- tries to retrieve the value at position (x, y). If the key doesn’t exist, it returns a space character " " instead of throwing a KeyError
        grid.append("".join(row))

    return grid

def print_secret_message(url):
    lines = fetch_google_doc(url)
    grid = create_character_grid(lines)
    for row in grid:
        print(row)



# Example usage:
print_secret_message("https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub")
