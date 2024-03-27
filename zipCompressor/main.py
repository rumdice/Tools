import os
import zipfile
import shortuuid as suuid
from datetime import datetime


def compress_to_zip(target, zip_file_name, password=None):
    try:
        # 대상 폴더가 존재하는지 확인
        if not os.path.exists(target):
            raise FileNotFoundError("대상 폴더를 찾을 수 없습니다.")
        
        # 대상 폴더의 파일 및 하위 폴더 리스트를 가져옴
        files = []
        for root, dirs, filenames in os.walk(target):
            for filename in filenames:
                files.append(os.path.join(root, filename))

        # 압축 파일 생성
        with zipfile.ZipFile(zip_file_name, 'w') as zipf:
            for file in files:
                zipf.write(file, os.path.relpath(file, target))

        # 압축 파일 생성
        with zipfile.ZipFile(zip_file_name, 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
            # 암호를 사용하여 압축
            if password:
                zipf.setpassword(password.encode())
            for file in files:
                zipf.write(file, os.path.relpath(file, target))

        print("압축 완료!")
    
    except Exception as e:
        print("압축 오류 발생:", e)


def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
            print(f"디렉토리 '{directory}'가 생성되었습니다.")
        except OSError as e:
            print(f"디렉토리 생성 실패: {e}")
    else:
        print(f"디렉토리 '{directory}'가 이미 존재합니다.")    


if __name__ == "__main__":
    origin_path = "./data/"
    target_path = "./zip/"

    now = datetime.now()
    nowStr = now.strftime("%Y-%m-%d %H:%M:%S")

    ensure_directory_exists(target_path)
    zip_zip_file_name = target_path + f"{nowStr}.zip" # 경로 지정해서 저장하기.

    # password = "1234"
    password = suuid.uuid()
    print(f"password is {password}")
    compress_to_zip(origin_path, zip_zip_file_name, password)



