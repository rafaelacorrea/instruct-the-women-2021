import requests

# Referências sobre o uso do requests:
#
# Fazendo requisições:
# https://docs.python-requests.org/en/master/user/quickstart/#make-a-request
# Usando JSON retornado:
# https://docs.python-requests.org/en/master/user/quickstart/#json-response-content

BASE_URL = 'https://pypi.org/pypi/{package_name}/{version}/json'

"""
Se package_name e a version não foram inseridos. Retorna falso.

Se package_name não foi inserido, mas a version sim. Retorna falso.

Se package_name foi inserido, mas a version não foi inserida. Então é mostrada a ultima versão do pacote (default). Retorna verdadeiro.

Se a requisição do package_name e version foi feita com sucesso e se o nom
e do pacote e versão inseridos for igual ao nome do pacote e versão json, então retorna verdadeiro.

"""
import requests

BASE_URL = 'https://pypi.org/pypi/{package_name}/{version}/json'

def version_exists(package_name, version):
    
    if package_name is None and version is None or package_name is None and version is not None:
        return False
        
    elif package_name is not None and version is None:
        
        version = latest_version(package_name)
        request = requests.get(BASE_URL.format(package_name = package_name, version = version))
        if request.ok == True:
            json = request.json()
            name_pack = json['info']['name']
            name_ver = json['info']['version']
                
            if package_name == name_pack and version == name_ver:
                return True
            else: 
                return False
    else:
        request = requests.get(BASE_URL.format(package_name = package_name, version = version))
        if request.ok == True:
            json = request.json()
            name_pack = json['info']['name']
            name_ver = json['info']['version']
                
            if package_name == name_pack and version == name_ver:
                return True
            else: 
                return False

"""
Se o nome do pacote inserido for nulo ou inválido, então é retornado Nulo.

Verifica se o pacote requisitado é válido, criação de variável para mostrar as informações dentro da chave releases, acrecenta version à chave e define a variavel para chamar a ultima versão.

"""
def latest_version(package_name):
    if package_name is None:
       return None
    
    else:
        NEW_BASE_URL = BASE_URL.replace("{version}/", "")
        
        request = requests.get(NEW_BASE_URL.format(package_name = package_name))
        if request.ok == True:
            json = request.json()
            version = json['info']['version']
            return version
        else:
            return None

