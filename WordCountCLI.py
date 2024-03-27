import argparse
import os

class WCTool:

    def __init__(self, file_path):
        self.file_path = file_path
    
    def CountLines(self):
        with open(self.file_path) as file:
            lines = file.readlines()
        return len(lines)

    def CountWords(self):
        words = []
        number_of_words = 0
        with open(self.file_path) as file:
            for line in file:
                words = line.split()
                number_of_words += len(words)
        return number_of_words

    def CountCharacters(self):
        characters = 0
        with open(self.file_path) as file:
            for line in file:
                line = line.strip("\n")
                characters += len(line)
        return characters
    
    def get_file_size(self):
        return os.path.getsize(self.file_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("command", nargs="?", help="Command to execute (e.g., L, W, C, SB)")
    parser.add_argument("FilePath", help="Specify the path of the file")
    args = parser.parse_args()
    
    tool = WCTool(args.FilePath)

    if args.command == "SB":
        print(tool.get_file_size(), args.FilePath)
    elif args.command == "L":
        print(tool.CountLines(), args.FilePath)
    elif args.command == "W":
        print(tool.CountWords(), args.FilePath)
    elif args.command == "C":
        print(tool.CountCharacters(), args.FilePath)
    else:
        print(tool.get_file_size(),
              tool.CountLines(),
              tool.CountWords(),
              tool.CountCharacters(),
              args.FilePath
              )
