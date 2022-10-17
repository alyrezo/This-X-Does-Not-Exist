import requests, shutil, modules
type = modules.HORSE
temp_path = f'{modules.TEMP}/{type}.jpg'
modules.PathChecker.tempcheck()
with open(temp_path,'wb') as image:
    image.write(requests.get('https://thishorsedoesnotexist.com/').content)
hash = modules.ReturnHash.get_hash(f'{modules.TEMP}/{type}.jpg')
modules.PathChecker.check(type)
shutil.move(temp_path,f'{type}/{hash}.jpg')
