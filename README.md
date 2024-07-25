# Armazenamento de Blobs com o Serviço de Blobs do Azure


link para configuração do Blob Azure:

* https://learn.microsoft.com/pt-br/azure/storage/blobs/storage-quickstart-blobs-python?tabs=managed-identity%2Croles-azure-portal%2Csign-in-powershell&pivots=blob-storage-quickstart-scratch#prerequisites

* https://www.youtube.com/watch?v=DrjIexCTF70

*   https://portal.azure.com/#view/Microsoft_Azure_Storage/ContainerMenuBlade/~/overview/storageAccountId/%2Fsubscriptions%2F9dddaa9e-b166-464d-8520-6d5aa4ea2e4d%2FresourceGroups%2Fwebapi%2Fproviders%2FMicrosoft.Storage%2FstorageAccounts%2Fnatanassis/path/storagecomcontainer/etag/%220x8DCACCA9545831E%22/defaultEncryptionScope/%24account-encryption-key/denyEncryptionScopeOverride~/false/defaultId//publicAccessVal/None



Este documento descreve uma classe Python chamada __ BlobStorageque facilita a interação com o Armazenamento de Blobs do Azure para carregar, baixar e listar blobs.

Requisitos:

* Python 3. x
* azure-identitybiblioteca: pip install azure-identity
* azure-storage-blobbiblioteca: pip install azure-storage-blob
* Config classe (pega as credencias no arquivo .env)

## Classe: BlobStorage

Esta classe fornece métodos para gerenciar blobs no Armazenamento de Blobs do Azure.

Construtor:

```Pitão
def __init__(self, create_container):
    self.config = Config()
    self.container_name = self.config.container_name
    self.blob_service_client = BlobServiceClient
    self.__create_container = create_container
Use o código com cuidado.
```

``create_container(booleano):`` Especifica se deve criar um novo contêiner caso ele não exista.

### Métodos:


* ``__new_container(self, _name_container=None)``(privado)

    * Gera um nome exclusivo para o contêiner se nenhum for fornecido.
    * Cria o contêiner usando o nome fornecido ou o nome exclusivo gerado.
    * Retorna o nome do contêiner.

* ``upload_to_blob_storage(self, file_path, file_name)``

    * Carrega um arquivo do caminho especificado para o Armazenamento de Blobs do Azure.
    * Cria um contêiner se create_containerfor True e não existir nenhum.
    * Carrega o arquivo usando o fornecido file_namecomo nome do blob.
    * Retornos Trueem caso de sucesso e fracasso. False

* ``read_blob_storage_all(self)``

    * Lista todos os blobs do contêiner configurado.
    * Imprime o índice e o nome de cada blob no contêiner.
    * Retorna uma lista de nomes de blobs em caso de sucesso e falha. False

* ``download_blob_storage(self, _file_name)``

    * Baixa um blob do Armazenamento de Blobs do Azure para um arquivo local.
    * Baixa o blob com o arquivo _file_name.
    * Cria o diretório local ./datase ele não existir (comentado).
    * Salva o blob baixado em ./data/_file_name.
    * Retornos Trueem caso de sucesso e fracasso. False

### Exemplo de uso:

````
from BlobStorage import BlobStorage

# Assuming your Config class provides the connection string
blob_storage = BlobStorage(create_container=True)

# Upload a file
upload_result = blob_storage.upload_to_blob_storage("/path/to/your/file.txt", "my_file.txt")
if upload_result:
    print("File uploaded successfully!")

# List all blobs
blob_list = blob_storage.read_blob_storage_all()
if blob_list:
    print("Blobs in the container:")
    for blob_name in blob_list:
        print(blob_name)

# Download a blob
download_result = blob_storage.download_blob_storage("my_file.txt")
if download_result:
    print("File downloaded successfully!")
Use o código com cuidado.
````

