# import shutil
# import os

# folder_path = ".\\Repos\\"

# for filename in os.listdir(folder_path):
#    file_path = os.path.join(folder_path, filename)
#    if os.path.isfile(file_path) or os.path.islink(file_path):
#       os.unlink(file_path)
#       print(filename, "is removed")
#    elif os.path.isdir(file_path):
#       shutil.rmtree(file_path)
#       print(filename, "subdirectory is removed")