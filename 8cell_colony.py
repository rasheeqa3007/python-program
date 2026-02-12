def cell_colony(cells, days):
    for _ in range(days):
        new_cells = [0] * 8  

        for i in range(1, 7):
            if cells[i - 1] == cells[i + 1]:
                new_cells[i] = 1
            else:
                new_cells[i] = 0

        cells = new_cells

    return cells



cells = [1, 0, 0, 0, 0, 1, 0, 0]
days = 1
print(cell_colony(cells, days))
