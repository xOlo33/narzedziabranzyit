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