import pdb

if __name__ == "__main__":
    sample_file = "./files/sample.txt"
    with open(sample_file, 'r') as file:
        content = file.read()
        print(content)
file.close()
