# Travel expenses for multiple trips
travel_costs = [[500, 150, 100, 50],[200, 300, 120, 80],
                [180, 220, 130, 170], [600, 250, 200, 90],
                [300, 180, 150, 70], [400, 320, 110, 100],
                [550, 270, 180, 60], [250, 190, 140, 120],
                [700, 350, 210, 110], [450, 230, 160, 95],
                [320, 280, 190, 85], [580, 260, 175, 75]]

# List to store processed expenses
processed_expenses = []
tmp_lst = []
i = 0
while i < len(travel_costs):
    j = 0
    while j < len(travel_costs[i]):
        if travel_costs[i][j] <= 100:
            tmp_lst.append('Cheap')
            j += 1
        else:
            tmp_lst.append(travel_costs[i][j])
            j += 1
    processed_expenses.append(tmp_lst)
    i += 1
    tmp_lst = []


# Testing
print('Processed Travel Expenses:', processed_expenses)