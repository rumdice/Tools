import subprocess
import os

def git_push_with_commit(repo_path, commit_message):
    try:
        
        # git add . : 모든 변경사항을 스테이징
        subprocess.run(["git", "-C", repo_path, "add", "."], check=True)
        
        # git commit -m "commit_message" : 커밋 메시지와 함께 커밋
        subprocess.run(["git", "-C", repo_path, "commit", "-m", commit_message], check=True)
        
        # git push origin master : 변경사항을 원격 저장소로 푸시
        subprocess.run(["git", "-C", repo_path, "push", "origin", "main"], check=True)
        
        print("커밋 및 푸시 완료!")
    except subprocess.CalledProcessError as e:
        print("깃 커밋 오류 발생:", e)


def git_log(repo_path):
    try:
        # git log : 깃의 로그를 본다
        log_output = subprocess.check_output(["git", "-C", repo_path, "log"], universal_newlines=True)
        print("커밋 로그:")
        print(log_output)

    except subprocess.CalledProcessError as e:
        print("깃 커밋 오류 발생:", e)


def git_pull(repo_path):
    try:
        # git pull origin master : 원격 저장소의 변경사항을 가져와 로컬 브랜치 업데이트
        subprocess.run(["git", "-C", repo_path, "pull", "origin", "main"], check=True)
        print("변경사항 가져오기 및 로컬 브랜치 업데이트 완료!")
    except subprocess.CalledProcessError as e:
        print("깃 풀 오류 발생:", e)


def git_clone(repo_url, destination_path):
    try:
        # git clone <repo_url> <destination_path> : 리포지토리 클론
        subprocess.run(["git", "clone", repo_url, destination_path], check=True)
        print("리포지토리 클론 완료!")
    except subprocess.CalledProcessError as e:
        print("깃 클론 오류 발생:", e)


if __name__ == "__main__":
    repo_url = "https://github.com/rumdice/Temp.git"
    repo_path = "./data"                                 # 리포지토리 경로
    commit_message = "테스트 커밋 이다222."                  # 커밋 메시지 (고정값이 아닌 유연함 필요)

    # TODO: 이미 클론 받았으면 패스해야 한다? 오류 발생 - 오류만 출력하고 넘어가게 함.
    git_clone(repo_url, repo_path)
    
    # 풀 받을게 없으면 오류가 뜬다? - 오류만 출력하고 일단 넘어가게 둠.
    git_pull(repo_path)

    # 만약 어떤 작업툴을 사용하여 해당 경로에 파일을 생성,변경,삭제 함
    # ./data 경로에 파일이 변경되었다 친다.

    # 푸쉬 할게 없으면 에러가 뜬다? - 오류만 출력하고 넘어감
    git_push_with_commit(repo_path, commit_message)

    git_log(repo_path)
