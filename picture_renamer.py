import sys
import os, glob

# 파일명에 번호 추가하기
def rename_file():
    count = 1
    dir_name = input('번호처리 할 디렉토리명을 입력하시오: ')
    current_dir_path = '[your_current_directory includes png files folder]'
    rename_files_path = current_dir_path + '/' + dir_name

    # 파일 이름을 변경하기 위해 path 등록
    os.makedirs(os.path.dirname(rename_files_path), exist_ok=True)

    # 현재 위치의 파일 목록
    files = glob.glob(rename_files_path+'/*.png')
    files.sort(key=os.path.getctime) # 파일 생성시간 순으로 정렬
    print(files)

    # 파일리스트 출력 확인

    for filename in files:

        # 파이썬 실행파일명은 변경하지 않음
        if filename.endswith("png"):
            new_name = filename.replace(filename, str(count)+".png")
            new_filename = os.path.join(rename_files_path, new_name)
            os.rename(filename, new_filename)
            count += 1


if __name__ == "__main__":
    rename_file()
