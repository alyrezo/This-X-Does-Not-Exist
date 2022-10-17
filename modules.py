TEMP = 'tmp'
PERSON = 'person'
CAT = 'cat'
ARTWORK = 'artwork'
HORSE = 'horse'

class PathChecker:
    def tempcheck():
        import os
        if os.path.exists(TEMP) == True:
            pass
        else:
            os.mkdir(TEMP)

    def check(path):
        import os
        if os.path.exists(path) == True:
            pass
        else:
            os.mkdir(path)

class ReturnHash:
    def get_hash(img_path):
        import hashlib
        with open(img_path, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()
