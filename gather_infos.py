import csv
import os
import re
import sys

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    END = '\033[0m'  # Reset to default color

csv_file = 'Photo details.csv'

#dir = "/Users/mattia/Desktop/prova"
#dir = "/Volumes/T7 Shield/Photos/Icloud Photos"
dir = sys.argv[1]

def find_dir_rec(start_directory, name):
    photos_directories = []

    for root, dirs, files in os.walk(start_directory):
        for dir_name in dirs:
            if dir_name == name:
                full_path = os.path.join(root, dir_name)
                photos_directories.append(full_path)

    return photos_directories

def find_files_with_extension(start_directory, extension):
    matching_files = []

    for root, dirs, files in os.walk(start_directory):
        for file in files:
            if file.endswith(extension) and not file.startswith("._"):
                full_path = os.path.join(root, file)
                matching_files.append(full_path)

    return matching_files

def find_media(start_directory):
    matching_files = []

    for root, dirs, files in os.walk(start_directory):
        for file in files:
            if not file.endswith("csv") and not file.startswith("._"):
                full_path = os.path.join(root, file)
                matching_files.append(full_path)

    return matching_files

# Open the CSV file
#with open(csv_file, newline='') as file:
#    reader = csv.DictReader(file)
#    
#    # Iterate over each row
#    for row in reader:
#        # Access each column by its header name
#        file_name = row['imgName']
#        date_taken = row['importDate']
#        
#        # Perform your desired operation
#        print(f"File Name: {file_name}, Date Taken: {date_taken}")

photos_folders = find_dir_rec(dir, "Photos")
albums_folders = find_dir_rec(dir, "Albums")

#for photo_folder in photos_folders:
#    print(photo_folder)

photos = {}


for photo_folder in photos_folders:
    for photo in find_media(photo_folder):
        photo_name = os.path.basename(photo)
        #print(photo_name)
        photos[photo_name] = {"path" : photo}
        

found = 0
not_found = 0

albums = {}

for album_folder in albums_folders:
    for album in find_files_with_extension(album_folder, ".csv"):
        album_name = re.match( r'(.*)\.', os.path.basename(album)).group(1)
        albums[album_name] = []
        with open(album, newline='') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                photo_name = row[list(row.keys())[0]]
                #print(photo_name)
                if not (photo_name in photos):
                    #print("Una foto indicata nell'album non è stata trovata")
                    not_found += 1
                else:
                    albums[album_name].append(photos[photo_name]["path"])
                    #print(photos[photo_name]["path"] + " " + album_name)
                    #photos[photo_name]["album"] = album_name
                    found += 1


#print(albums)
print(len(albums))
for album_photos in albums.values():
    print(len(album_photos), end = " ")

print("")
for album_title in albums:
    print(album_title)
    for photo in albums[album_title]:
        print(photo)

#print("##" + album_name + "##")
#print(len(photos) + " " + len(photos) - found)
#print(Colors.GREEN + "Ho trovato l'album a " + str(found))
#print(Colors.RED + "Non ho trovato l'album a " + str(len(photos) - found) + "foto")
#print(f'tell application "Photos"\nmake new album with properties {{name:"{"AppleScript"}"}}\n')
