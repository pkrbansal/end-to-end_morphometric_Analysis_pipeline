import os
from google.cloud import storage

def upload_images(bucket_name, source_folder):
    client = storage.Client()
    bucket = client.bucket(bucket_name)

    for filename in os.listdir(source_folder):
        if filename.endswith((".jpg", ".png", ".jpeg")):
            blob = bucket.blob(f"train_data/{filename}")
            blob.upload_from_filename(os.path.join(source_folder, filename))
            print(f"Uploaded {filename} to {bucket_name}")

if __name__ == "__main__":
    upload_images("Danio_echo_images", "./mutant_larvae")
