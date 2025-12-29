import numpy as np
from collections import deque, defaultdict
import shutil


DIRECTIONS = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def solve(input_grid):
    """
    Connect colored bounding boxes with orthogonal paths based on instruction row.
    Does NOT remove blue boxes or the instruction row.
    
    Args:
        input_grid (List[List[int]]): 2D grid with colored boxes and path instruction row.
            
    Returns:
        List[List[int]]: Grid with colored paths added between boxes (L-shaped connections).
    """
    arr = np.array(input_grid, dtype=np.int32)
    
    # Step 1: Find the path instruction row (last row or row with spaced colored numbers)
    path_row_idx = None
    for r in range(arr.shape[0] - 1, -1, -1):
        colored_vals = [arr[r, c] for c in range(arr.shape[1]) if arr[r, c] > 1]
        if len(colored_vals) >= 3:
            path_row_idx = r
            break
    
    if path_row_idx is None:
        return arr.tolist()
    
    # Step 2: Extract the sequence of colors from the instruction row
    path_sequence = []
    for c in range(arr.shape[1]):
        if arr[path_row_idx, c] > 1:
            path_sequence.append(arr[path_row_idx, c])
    
    # Step 3: Find all bounding boxes and their connection points
    visited = np.zeros_like(arr, dtype=bool)
    boxes = defaultdict(list)
    
    def get_box_interior_color(min_r, max_r, min_c, max_c):
        """Extract the non-0, non-1 color from box interior"""
        for r in range(min_r + 1, max_r):
            for c in range(min_c + 1, max_c):
                if arr[r, c] not in [0, 1]:
                    return arr[r, c]
        return None
    
    # Find all 1-components (bounding boxes)
    for r in range(arr.shape[0]):
        for c in range(arr.shape[1]):
            if arr[r, c] == 1 and not visited[r, c]:
                # BFS to find connected component of 1s
                stack = [(r, c)]
                visited[r, c] = True
                component = [(r, c)]
                
                while stack:
                    cr, cc = stack.pop()
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < arr.shape[0] and 0 <= nc < arr.shape[1]:
                            if arr[nr, nc] == 1 and not visited[nr, nc]:
                                visited[nr, nc] = True
                                stack.append((nr, nc))
                                component.append((nr, nc))
                
                # Get bounding box
                rows = [p[0] for p in component]
                cols = [p[1] for p in component]
                min_r, max_r = min(rows), max(rows)
                min_c, max_c = min(cols), max(cols)
                
                # Extract interior color and store box boundaries
                color = get_box_interior_color(min_r, max_r, min_c, max_c)
                if color:
                    exit_cells = set()
                    for br, bc in component:
                        for dr, dc in DIRECTIONS:
                            nr, nc = br + dr, bc + dc
                            if 0 <= nr < arr.shape[0] and 0 <= nc < arr.shape[1]:
                                if nr == path_row_idx:
                                    continue
                                if arr[nr, nc] == 0:
                                    exit_cells.add((nr, nc))

                    if exit_cells:
                        center_r = (min_r + max_r) // 2
                        center_c = (min_c + max_c) // 2
                        boxes[color].append({
                            "bounds": (min_r, max_r, min_c, max_c),
                            "exits": sorted(exit_cells),
                            "center": (center_r, center_c),
                        })
    
    # Prepare per-color queues ordered top-to-bottom then left-to-right
    box_queues = {}
    for color, info_list in boxes.items():
        if info_list:
            info_list.sort(key=lambda info: (info["center"][0], info["center"][1]))
            box_queues[color] = deque(info_list)

    sequence_boxes = []
    for color in path_sequence:
        queue = box_queues.get(color)
        if queue:
            sequence_boxes.append((color, queue.popleft()))

    # Step 4: Connect boxes following the path sequence
    for i in range(len(sequence_boxes) - 1):
        color_from, box_from = sequence_boxes[i]
        _, box_to = sequence_boxes[i + 1]
        draw_path_between_boxes(arr, box_from, box_to, color_from, path_row_idx)
    
    return arr.tolist()


def draw_path_between_boxes(arr, box_from, box_to, color, path_row_idx):
    """
    Draw the shortest orthogonal path between two boxes using BFS.
    The path lives entirely in empty (0) cells and is coloured with `color`.
    """
    start_candidates = [cell for cell in box_from["exits"] if arr[cell] == 0]
    goal_candidates = {cell for cell in box_to["exits"] if arr[cell] == 0}

    if not start_candidates or not goal_candidates:
        return

    target_center = box_to["center"]
    start_candidates.sort(key=lambda cell: (abs(cell[0] - target_center[0]) + abs(cell[1] - target_center[1]), cell[0], cell[1]))

    path = bfs_path(arr, start_candidates, goal_candidates, path_row_idx)
    if not path:
        return

    for r, c in path:
        if arr[r, c] == 0:
            arr[r, c] = color


def bfs_path(arr, starts, goals, path_row_idx):
    goals = set(goals)
    queue = deque()
    parents = {}
    visited = set()

    for cell in starts:
        if cell in visited:
            continue
        queue.append(cell)
        visited.add(cell)
        parents[cell] = None

    while queue:
        r, c = queue.popleft()
        if (r, c) in goals:
            return _reconstruct_path((r, c), parents)

        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < arr.shape[0] and 0 <= nc < arr.shape[1]:
                if nr == path_row_idx:
                    continue
                if (nr, nc) not in visited and (arr[nr, nc] == 0 or (nr, nc) in goals):
                    visited.add((nr, nc))
                    parents[(nr, nc)] = (r, c)
                    queue.append((nr, nc))

    return None


def _reconstruct_path(end_cell, parents):
    path = []
    current = end_cell
    while current is not None:
        path.append(current)
        current = parents[current]
    path.reverse()
    return path
                 



# Map integer -> ANSI background color code (approximate)
BG = {
    1: 44,   # blue
    2: 41,   # red
    3: 42,   # green
    4: 103,  # bright yellow (approx. yellow)
    5: 100,  # grey
    6: 45,   # magenta (fuchsia)
    7: 43,   # orange-ish (use yellow background)
    8: 46,   # cyan / teal
    9: 101,  # light grey (approx brown/other)
}

RESET = "\x1b[0m"

def cell_str(val):
    """Return a small string representing the cell:
       - 0 -> ' o' with black-ish foreground
       - others -> two-space block with background color
    """
    if val == 0:
        # Use bright black / grey for 'o' so it's visible on dark terminals
        return "\x1b[90m" + "o " + RESET
    bg = BG.get(val, 47)  # fallback to white background if missing
    return f"\x1b[{bg}m  {RESET}"

def print_grid(g):
    for row in g:
        print("".join(cell_str(v) for v in row))

def print_side_by_side(g1, g2, title1="Input", title2="Output"):
    # Align titles and detect terminal width to avoid wrapping (best-effort)
    cols, _ = shutil.get_terminal_size((120, 40))
    gap = 4
    width = len(g1[0]) * 2  # approx characters per grid (2 chars per cell)
    # print titles centered above each grid
    left_pad = (width - len(title1)) // 2
    right_pad = (width - len(title2)) // 2
    print(" " * left_pad + title1 + " " * (cols - left_pad - len(title1) - right_pad - len(title2) - gap) + " " * right_pad + title2)
    for r in range(max(len(g1), len(g2))):
        left = "".join(cell_str(g1[r][c]) for c in range(len(g1[0]))) if r < len(g1) else " " * width
        right = "".join(cell_str(g2[r][c]) for c in range(len(g2[0]))) if r < len(g2) else ""
        print(left + " " * gap + right)

if __name__ == "__main__":
    # Put your input grid here (the one you provided)
    G = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,1,1,1,1,0,0,1,1,1,1,0,0,0,1,1,1,1,0,0],
         [0,1,2,2,1,0,0,1,5,5,1,0,0,0,1,7,7,1,0,0],
         [0,1,2,2,1,0,0,1,5,5,1,0,0,0,1,7,7,1,0,0],
         [0,1,1,1,1,0,0,1,1,1,1,0,0,0,1,1,1,1,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,1,1,1,1,0,0,1,1,1,1,0,0,0,1,1,1,1,0,0],
         [0,1,3,3,1,0,0,1,9,9,1,0,0,0,1,6,6,1,0,0],
         [0,1,3,3,1,0,0,1,9,9,1,0,0,0,1,6,6,1,0,0],
         [0,1,1,1,1,0,0,1,1,1,1,0,0,0,1,1,1,1,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,1,1,1,1,0,0,0,1,1,1,1,0,0],
         [0,0,0,0,0,0,0,1,4,4,1,0,0,0,1,2,2,1,0,0],
         [0,0,0,0,0,0,0,1,4,4,1,0,0,0,1,2,2,1,0,0],
         [0,0,0,0,0,0,0,1,1,1,1,0,0,0,1,1,1,1,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [2,0,3,0,9,0,4,0,2,0,6,0,7,0,5,0,0,0,0,0]]  # Instruction row: sequence of connections

    out = solve(G)
    print_side_by_side(G, out, "Input", "Output")