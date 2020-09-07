from hashlib import sha1

for i in range(10000000, 100000000):
    for _ in range(500):
        password = sha1(str(i)+"salt_for_you").hexdigest()
    if password == "문제에서 나온 값":
        print(i)
        break

#레인보우 테이블 (이런 값을 모아둔 파일) 문제라 csv나 그런 파일로 저장하는게 가장 best 하지만 그러면 엄청난 용량이 나올것이므로 4분의 1정도 잘라서 풀거나 하면 된다.