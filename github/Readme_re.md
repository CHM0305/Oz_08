### Day1    
*Git의 3가지 범위 

지역(Local)- 특정 저장소 한정/폴더 하나만 적용, 
전역(Global)- 모든 저장소 한정/생성하는 모든 폴더 적용, 
시스템(System)- 해당 컴의 모든 저장소, 사용자 걸쳐 적용/잘 사용되지 않음


*Git 기본 명령어

1. git -- version - 버전 확인
2. git status - 파일 상태 확인 명령어

   
*Git파일 Commit하는 순서

1. git init - 선택 폴더를 깃 저장소로 만드는 명령어 (이때 깃 저장소에 필요한 모든 뼈대 파일이 담긴 .git라는 숨겨진 폴더가 생성됨, cmd+shift_.로 확인)
2. git config --global user.name/ user.email "Github 가입시 사용한 닉넴과 이멜" - 전역에 사용자 정보 입력
3. git config --global user.name/ user.email - 이름 이멜 확인
4. git config --list - 저장소의 설정 전체 출력
5. git config --unset user.name/ user.email - 전역에 설정된 이름 이멜 삭제
6. git config --global init.defaultBranch main - 로컬 저장소를 master->main 변경
   
*git 관리 설정 순서

1.back.yaml, front.yaml.yaml(야물) 파일 생성 JSON과 같은 데이터 형식 파이썬의 dict 자료형처럼 key, value 형태로 저장하는 .yaml 확장자 파일 생성
2. git status - 파일 상태 확인 명령어 (Untracked-Git 추적 X,Tracked-Git 추적 O)
3. git add "commit 원하는 파일명" - Untracked 상태인 한가지 파일만 임시저장영역인 스테이지로 더하기 위한 명령어
4. git add . - 모든 Untracked 상태인 파일을 임시저장영역인 스테이지로 더하기 위한 명령어
5. admin_info.yaml -
6. .gitignore - Git 관리를 원하지 않은 파일
7. admin_info.yaml gitignore - 관리를 원하지 않는 파일이니, .gitignore 파일 안에 파일명 적어주기

* git을 이용해 commit 작성
-commit -확인 가능한 스테이지의 파일을 하나의 버전으로 만들 수 있음. 그리고 그렇게 만든 것을 스냅샷 형태로 저장도 가능.
1. git commit -m "메세지" -   -m 바로 뒤 메세지를 입력할 수 있도록 해주는 옵션
2. git commit -am "메세지" - 변경된 모든 사항을 바로 add 하고 commit하는 명령어

*vim 문서 편집기
git commit - 문서 편집기 화면이 나타남.
i - 문서 편집 모드 진입
esc - 문서 편집 모드 종료
shift +wq - w(write)저장 q(quit)편집 종료
:q - 저장 없이 종료
:q! - 저장 없이 강제 종료
k/j - 위/ 아래로 스크롤

*git log를 이용한 commit 이력 확인
1. git log -p - 각 커밋마다 변경 사항 함꼐 보기
2. git log -(갯수) - 최근 갯수 커밋만 보기
3. git log --stat - 통계 함께 보기
4. git log --oneline - 한 줄로 보기
5. git log -S (검색어) - 변경사항 내 단어 검색
6. git log --all --decorate --oneline --graph (검색어) - 자주 사용되는 그래프 로그 보기
