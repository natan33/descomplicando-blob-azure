from blobStorage import BlobStorage


# if __name__ == '__main__':
#     # Assuming your Config class provides the connection string
#     blob_storage = BlobStorage(create_container=True)

#     # Upload a file
#     upload_result = blob_storage.upload_to_blob_storage("/path/to/your/file.txt", "my_file.txt")
#     if upload_result:
#         print("File uploaded successfully!")

#     # List all blobs
#     blob_list = blob_storage.read_blob_storage_all()
#     if blob_list:
#         print("Blobs in the container:")
#         for blob_name in blob_list:
#             print(blob_name)

#     # Download a blob
#     download_result = blob_storage.download_blob_storage("my_file.txt")
#     if download_result:
#         print("File downloaded successfully!")