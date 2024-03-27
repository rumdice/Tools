import pandas as pd
import codecs as cd
import os

def excel_to_json(excel_file):
    # 엑셀 파일 읽기
    df = pd.read_excel(excel_file)
    
    # JSON으로 변환
    json_data = df.to_json(orient='records', indent=4)
    
    return json_data

def save_json_to_file(json_data, json_file):
    # json문자열 파일을 .json으로 저장
    with open(json_file, 'w') as f:
        f.write(json_data)

def save_json_to_binary(json_data, bin_file):
    # 문자열을 바이너리로 인코딩
    bin_data = cd.encode(json_data.encode('utf-8'), "base64")
    
    # 파이너리 파일을 지정된 경로에 저장.
    with open(bin_file, 'wb') as f:
        f.write(bin_data)


if __name__ == "__main__":
    
    xlsx_file_path = "./xlsx"
    json_file_path = "./json"
    bin_file_path = "./bin"
    target_path = ""
    
    try:
        file_list = os.listdir(xlsx_file_path)
        xlsx_file_list = [file for file in file_list if file.endswith('.xlsx')]

        for xlsx_file in xlsx_file_list:
            filename = xlsx_file.split(".")[0]
        
            # 파일 컨버팅
            target_path = xlsx_file_path + "/" + filename + ".xlsx"
            json_data = excel_to_json(target_path)
            
            # json데이터를 파일로 저장
            target_path = json_file_path + "/" + filename + ".json"
            save_json_to_file(json_data, target_path)
        
            # json데이터를 바이너리로 변환 후 저장
            target_path = bin_file_path + "/" + filename + ".bin"
            save_json_to_binary(json_data, target_path)
        
    except Exception as e:
        print("exception :", str(e))

    print("file convert is finished")
        

    


    
    
    