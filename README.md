# labsafety
make auto macro to check safety 

1. 먼저 파이썬을 설치(2.7)
2. virtualenv 환경설정(labsafety라는 가상환경 생성함)
3. pip를 통해 selenium 설치
4. 사용하고자 하는 브라우저 web driver 설치(IE용 x64 3.8.0 버전 설치함)
5. 로그인 후 시스템 접속 전까지는 DOM 구조라 selenium으로 자동화 가능
6. 시스템 접속 후에는 MS silverlight 기반이라 selenium 대신 Sikuli 사용
7. SikuliX 다운로드 (1.1.1 )
8. Javaw 통해 SikuliX.1.1.1.jar 실행 (자동 설치 진행)
9. 직접 파이썬 코드 실행하여 테스트
10. 파이썬 파일 윈도우 스케쥴러에 등록

required conf :
    https://github.com/SeleniumHQ/selenium/wiki/InternetExplorerDriver#required-configuration

xpath tutorial :
    https://www.guru99.com/xpath-selenium.html

# Sikuli Usage
sikuli documentation :
    http://doc.sikuli.org/index.html

sikulix tutorial :
    https://www.swtestacademy.com/quick-start-to-sikulix/

how-to-use dragDrop in Sikulix :
    https://stackoverflow.com/questions/8679929/drag-and-drop-with-sikuli

how to run jar file (to run sikulix.x.x.x.jar) :
    https://zetawiki.com/wiki/%EC%9C%88%EB%8F%84%EC%9A%B0_jar_%ED%8C%8C%EC%9D%BC_%EC%8B%A4%ED%96%89

Jython language tutorial :
    http://jythonbook-ko.readthedocs.io/en/latest/LangSyntax.html

how to run python file with window scheduler :
    http://fnmj.tistory.com/19

# Selenium Usage
how to use selenium(Korean blog) :
    https://m.blog.naver.com/PostView.nhn?blogId=nonamed0000&logNo=220977390647&proxyReferer=https%3A%2F%2Fwww.google.co.kr%2F

