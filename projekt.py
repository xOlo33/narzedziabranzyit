import sys

def parsearguments():
    if len(sys.argv) != 3:
        print("Usage: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)

    inputfile = sys.argv[1]
    outputfile = sys.argv[2]
    return inputfile, output_file

if __name == "__main":
    input_file, output_file = parse_arguments()
    print(f"Input File: {input_file}")
    print(f"Output File: {output_file}")

    import json


    def load_json(file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                # Opcjonalnie: Weryfikacja składni za pomocą schematu JSON
                return data
        except json.JSONDecodeError as e:
            print(f"Invalid JSON format: {e}")
            sys.exit(1)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            sys.exit(1)

            if name == "main":
                input_file, output_file = parse_arguments()

                if input_file.endswith('.json'):
                    data = load_json(input_file)
                    print(f"Data: {data}")
                else:
                    print("Unsupported input format")
                    sys.exit(1)