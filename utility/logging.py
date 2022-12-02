from utility.vestiti import body_parts, class_names

def suggestion_log(population):
    pieces = ""
    for i, dress in enumerate(population[0]):
        pice = body_parts[i][dress]
        pieces += f"<b>{class_names[i]}:</b> {pice.name} <br>"
    return pieces

