# Multiline input containing helicopter names, potentially separated by spaces or new lines
helicopters_line = """
RHS_MELB_AH6M
RHS_MELB_MH6M
RHS_MELB_H6M
"""

# Normalize the input by replacing new lines and extra spaces with a single space, then split
helicopters = ' '.join(helicopters_line.split()).split()

# Format each helicopter name
formatted_helicopters = ['"{}",'.format(helicopter) for helicopter in helicopters]

# Print each formatted name on a new line
for helicopter in formatted_helicopters:
    print(helicopter)

