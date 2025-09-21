import requests
import json # To clean up the json result

Artist = input("Enter artist name: ")

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + Artist) #limit can be change from 1 to 50
#print(response.json())
#print(json.dumps(response.json(), indent = 2)) # THIS CAN BE USED TO TIDY IT UP TO BE R

object = response.json()
for result in object["results"]:
    print(result["trackName"])
    
    
    
# ANOTHER EXAMPLE
import requests
import json

def main():
    count = 0
    Artist = input("Input Artist: ")
    
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            {"q": Artist} # q is parameters , works without parameters btw
            )
        response.raise_for_status() # Check Error or Nah
    except requests.HTTPError:
        print("Error!")
        return
    
    #content = json.dumps(response.json(), indent = 2) # TO IMPORT THE RESPOND INTO JSON
    content = response.json()
    #print(content)
    for _ in content["data"]:#content = gets data from above , then find the dict "list"
       count += 1
       print(f"{count}. {_['title']}")
       
main()

