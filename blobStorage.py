import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


from config import Config


class BlobStorage:

    def __init__(self,create_container):
        self.config = Config()
        self.container_name = self.config.container_name
        self.blob_service_client = BlobServiceClient
        self.__create_container = create_container
    
    def __new_container(self):

        _container_name = None
        # Create a unique name for the container
    
        self.blob_service_client.from_connection_string(self.config.connection_string)

        # Create the container
        container_client = self.blob_service_client.create_container(_container_name)
        return _container_name

    def upload_to_blob_storage(self,file_path,file_name):
        try:
            
            if self.__create_container == True:
                self.__new_container()

            # Create a local directory to hold blob data
            #local_path = "./data"
            #os.mkdir(local_path)
            blob_service_client = self.blob_service_client.from_connection_string(self.config.connection_string)
            # Create a file in the local data directory to upload and download
            local_file_name = str(file_name) 
            upload_file_path = os.path.join(file_path, local_file_name)

            # Crie um cliente blob usando o nome do arquivo local como nome do blob
            blob_client = blob_service_client.get_blob_client(container=self.container_name, blob=local_file_name)

            print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

            # Upload the created file
            with open(file=upload_file_path, mode="rb") as data:
                blob_client.upload_blob(data)
                return True
            
        except Exception as ex:
            print('Exception:')
            print(ex)
            return False
        
    def read_blob_storage_all(self):
        try:  
                blob_serve_cliente = self.blob_service_client.from_connection_string(self.config.connection_string)
                container_client = blob_serve_cliente.get_container_client(self.config.container_name)
                print()
                blob_list = []
                for index,blob_i in enumerate(container_client.list_blobs()):
                    print(index, blob_i.name)
                    blob_list.append(blob_i.name)

                return blob_list

        except Exception as ex:
            print('Exception:')
            print(ex)
            return False

    def download_blob_storage(self,_file_name):
        # Download the blob to a local file
        # Add 'DOWNLOAD' before the .txt extension so you can see both files in the data directory
        try:
            blob_serve_client = self.blob_service_client.from_connection_string(self.config.connection_string)

            local_path = "./data"
            _file_name = "curriculum Natã.pdf"

            download_file_path = os.path.join(local_path, str(_file_name))

            container_client = blob_serve_client.get_container_client(container= self.config.container_name) 

            print("\nDownloading blob to \n\t" + download_file_path)

            with open(file=download_file_path, mode="wb") as download_file:
                download_file.write(container_client.download_blob(_file_name).readall())

                return True
        except Exception as ex:
            print('Exception:')
            print(ex)
            return False