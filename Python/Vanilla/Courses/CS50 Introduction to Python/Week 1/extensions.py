def main():
    File = input("File name: ").strip().lower()
    print(f"{extension_detect(File)}")

def extension_detect(File):
    File = "." + File.split(".")[-1]

    if File == ".jpg":
        return "image/jpeg"
    elif File == ".gif":
        return "image/gif"
    elif File == ".jpeg":
        return "image/jpeg"
    elif File == ".png":
        return  "image/png"
    elif File == ".zip":
        return  "application/zip"
    elif File == ".txt":
        return "text/plain"
    elif File == ".pdf":
        return "application/pdf"
    else:
        return "application/octet-stream"

main()

