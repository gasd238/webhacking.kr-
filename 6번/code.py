import base64 #base 64 모듈 가져옴
 
id = b"nimda" # 바꿀값을 바이트로 저장 (암호화를 위해)
 
for _ in range(20):
    user_id=base64.b64encode(id) #20번 암호화
 
id=id.decode("utf-8") #바이트를 다시 utf8 로 저장(문자열 변경을 위해)
 
intab="12345678"  #이 값을
outtab="!@$^&*()" #이 값으로 변경(앞에서부터 순서대로)
transtab=id.maketrans(intab,outtab) #변경
 
print(id.translate(transtab))
