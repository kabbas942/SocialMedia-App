import uuid

def getRandom():
    namespace = uuid.UUID('00000000-0000-0000-0000-000000000000')  # Example namespace UUID
    name = 'example_name'
    code = str(uuid.uuid5(namespace,name))[:8].lower()
    print(code)
    return code