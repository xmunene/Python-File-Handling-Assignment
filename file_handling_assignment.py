def modify_file_content(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            content = infile.readlines()

        modified_content = [line.upper() for line in content]

        with open(output_file, 'w') as outfile:
            outfile.writelines(modified_content)
        
        print(f"Modified content has been written to {output_file}")
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    input_file = "input.txt" 
    output_file = "output.txt" 
    input_file = input("Enter the input file name: ")
    output_file = input("Enter the output file name: ")
    try:
        modify_file_content(input_file, output_file)
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist or cannot be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")