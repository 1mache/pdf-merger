from pypdf import PdfWriter
import sys

def main():
    # should get precisely 3 arguments: script name and 2 
    if len(sys.argv) != 3:
        print("Error: Bro, give me 2 pdf document names, with their path (as cmd args)")
        return
    
    writer = PdfWriter()
    #get the filenames
    filename1, filename2 = sys.argv[1:3]
    for file in [filename1, filename2]:
        try:
            writer.append(file)
        except FileNotFoundError:
            print(f"Error: Bro, file {file} was not found.")
            writer.close()
            return

    writer.write("merged-pdf.pdf")
    writer.close()

if __name__ == '__main__':
    main()   