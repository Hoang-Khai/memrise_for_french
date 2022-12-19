# Define the pattern to search for
pattern = ' /'

# Initialize an empty list to store the modified lines
modified_lines = []

# Open the file in read mode
with open('fra-eng.dict', 'r', encoding='utf-8') as file:
  # Read the lines of the file
  lines = file.readlines()
  
  # Iterate through the list of lines
  for line in lines:
    current = lines.index(line)+1
    # line = line.replace('\n', ' ')
    # If the line contains the pattern
    if pattern in line:
      # Initialize a variable to store the modified line
      modified_line = line
      
      # Set a flag to indicate that the pattern has been found
      pattern_found = True
      
      # Iterate through the remaining lines
      for next_line in lines[current:]:
        # If the next line contains the pattern
        if pattern in next_line:
          # Reset the flag and break the inner loop
          break
        # If the next line does not contain the pattern
        else:
          # Concatenate the next line to the modified line
          modified_line += next_line
      
      # If the pattern was found, append the modified line to the list
      if pattern_found:
        modified_line = modified_line.replace('\n', ' __ ')[:-4]
        modified_lines.append(modified_line)
    # If the line does not contain the pattern
    else:
      # Append the line to the list as is
      pass

# Open a new file in write mode
with open('new_file.txt', 'w', encoding='utf-8') as new_file:
  # Write the modified lines to the new file
  for line in modified_lines:
    new_file.write(line + "\n")
