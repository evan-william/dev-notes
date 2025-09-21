import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # Ensure we are matching ONLY inside <iframe> tags
    pattern = r'<iframe[^>]+src="https?://(?:www\.)?youtube\.com/embed/([^"]+)"'
    match = re.search(pattern, s)

    if match:
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"
    return None  # If no valid YouTube iframe is found, return None

if __name__ == "__main__":
    main()
