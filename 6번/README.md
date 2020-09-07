# webhacking.kr 6번
php 암호화 문제
암호화 문제다. 소스를 보니 id adimin pw nimda로 하면 된다는데..  
id랑 pw를 모두 base64로 20번 복호화 하고 cookie에 넣어 확인하는데 그럼 저 admin 과 nimda 를 20번 암호화만 하면 되나... 싶었다..  
위에 자세히 보니 들어온 값을 특정 숫자를 특정 특수문자로 바꾸는 코드가 있어 그거에 맞게 replace 한 암호문을 cookie값에 넣어주면 끝