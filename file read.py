def modify_file(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            lines = infile.readlines()

        with open(output_file, 'w') as outfile:
            for index, line in enumerate(lines, start=1):
                modified_line = f"{index}: {line.strip().upper()}\n"  
                outfile.write(modified_line)

        print(f"Modified file has been written to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if _name_ == "_main_":
    input_path = input("Enter the path of the input file: ").strip()
    output_path = input("Enter the path of the output file: ").strip()

    modify_file(input_path, output_path)
