### 사용법
- 기본 DB 생성
    ```bash
    python3 manage.py makemigrations burgers
    python3 manage.py migrate
    ```

- 서버 실행
    ```bash
    python3 manage.py runserver
    ```

- 데이터 추가
    1. 슈퍼유저 생성
        ```bash
        python3 manage.py createsuperuser
        ```
    2. 서버 실행
        ```bash
        python3 manage.py runserver
        ```
    3. http://127.0.0.1/admin에 접속
        1번에서 만든 Username/Password 입력
        Burgers에 데이터 추가
