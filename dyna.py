import os
import shutil

SOURCE_FOLDER = "data/updates"
TARGET_FOLDER = "data/new_docs"

def fetch_new_documents():

    if not os.path.exists(TARGET_FOLDER):
        os.makedirs(TARGET_FOLDER)

    files = os.listdir(SOURCE_FOLDER)

    for file in files:
        src = os.path.join(SOURCE_FOLDER, file)
        dst = os.path.join(TARGET_FOLDER, file)

        shutil.move(src, dst)

    print("New documents fetched.")
