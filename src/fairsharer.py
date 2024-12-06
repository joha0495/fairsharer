
def fair_sharer(values, num_iterations, share=0.1):

    for i in range (num_iterations):

        part = max(values) * share
        max_index = values.index(max(values))
        values[max_index] = values[max_index] - part * 2
        values[max_index - 1] = values[max_index - 1] + part
        values[max_index +1] = values[max_index + 1] + part

    return values




print(fair_sharer([1000,0, 800, 0], 1))  # --> [100, 800, 900, 0]
print(fair_sharer([0, 1000, 800, 0], 2))  # --> [100, 890, 720, 90]