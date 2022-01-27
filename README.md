# doit_django
## 블로그 제작 프로젝트
   
### - 2022.01.14.   
가상환경 세팅   
프로젝트폴더 생성   
blog, single_page 앱 생성   
post(blog) 모델 생성 [포스트 이름, 내용, 시간 작성]   
FBV로 블로그 포스트 목록 페이지 만들기   
상세페이지 제작 및 링크 연결   
   
### - 2022.01.15.   
대문, 소개페이지 틀 만들기   
네비게이션바 틀 제작   
FBV 방식에서 CBV 방식으로 변경   
현재까지의 내용에 부트스트랩 적용   
리스트와 상세페이지에 이미지 업로드 및 출력   
이미지없을때 예외처리 추가   
파일 업로드 기능 추가   
업로드된 파일 다운로드 기능 및 버튼 추가   
turncate 활용, 요약문 기능추가 및 표시   
   
### - 2022.01.17
블로그의 포스트리스트, 상세페이지 디자인통일(block활용 모듈화)   
네비게이션바, 푸터 모듈화   
작성자 항목 추가   
카테고리 항목 추가   
포스트리스트, 상세 페이지에 카테고리 뱃지, 리스트카드 추가   
html div 배치 오류 수정   
   
### - 2022.01.18
카테고리별 페이지 구축   
미분류 페이지 따로 작성   
   
### - 2022.01.19
태그기능 추가 및 표시   
태그 페이지 구축   
포스트 작성, 수정 버튼 및 기능 구현   
로그인한 staff, superuser만 포스트 작성 권한 부여   
포스트를 작성한 사람만 포스트 수정 권한 부여   
   
### - 2022.01.21
마크다운 적용(markdownx)   
회원가입 로그인기능 추가(allauth)   
구글 로그인기능 추가   
로그아웃기능 추가   
이메일 회원가입 및 로그인 로그아웃 기능 추가   
   
### - 2022.01.22
댓글기능 추가 및 포스트 상세페이지에 출력구현   
비로그인시 댓글에 로그인툴바 활성화 구현   
댓글쪽 디자인 수정 및 버튼(만)추가   
   
### - 2022-01-23
댓글에 추가시킨 드롭다운 버튼에 삭제, 수정 기능 구현   
페이지 리스트에 pagination 적용   

### - 2022-01-24
검색기능 구현   
구글 프로필이미지, 사용자별 아바타 출력 기능 구현   
메인페이지 업데이트   
어바웃 미 임시 업데이트   
   
### - 2022-01-25
도커 사용준비(requirements/Dockerfile 작성) / [이후 쿠버네티스로도 적용해볼것]   
   
### - 2022-01-27
도커에 컨테이너 빌드 & up 테스트 완료
   