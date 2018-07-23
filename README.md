# AvocadoAPI  

### 역할:  

베지아보카도의 백엔드를 가동하는 코드 베이스  

### 기술 스택:  

백엔드: Django + Django Rest Framework + JWT  
테스트: Travis CI + Pytest  
서버: uWSGI + Nginx + Docker + Docker Compose  
데이터베이스: PostgreSQL  
캐시: Redis  

### 상세 설명:  

1. accounts 앱은 유저 정보를 관리해주고, JWT 토큰 발행, 리뉴얼 등과 같은 작업을 맡아서 처리해준다.  
2. services 앱은 우박 템플릿 엔진의 핵심으로, 템플릿 처리 기술에 필요한 API들이 정의내려져 있다.

=====

개발자 (owner): Robert --> 로버트, 로비, 라비 ...... 명훈
