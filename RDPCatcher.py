import csv
import re

def extract_text_from_csv(csv_file, search_column_index, extract_column_index, output_file):
    with open(csv_file, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        extracted_text = []
            
        for row in csv_reader:            
            if len(row) > search_column_index and row[search_column_index] == LogOn21:
                if len(row) > extract_column_index:
                    #extracted_text.append(row[6])
                    extract_value = row[extract_column_index]
                    regex = r"<User>(.*?)<\/User>"
                    match = re.search(regex, extract_value)
                    if match:
                        extracted_text.append("LogOn(eventid 21) ")
                        extracted_text.append("User : "+match.group(1)) 
                    regex = r"<SessionID>(.*?)<\/SessionID>"
                    match = re.search(regex, extract_value)
                    if match:
                        extracted_text.append("SessionID : "+match.group(1)) 
                    
                    # 정규 표현식을 사용하여 <Address>와 </Address> 사이의 문자열을 추출
                    regex = r"<Address>(.*?)<\/Address>"
                    match = re.search(regex, extract_value)
                    if match:                        
                        extracted_text.append("Address : "+match.group(1))
                        extracted_text.append("\n")
            elif len(row) > search_column_index and row[search_column_index] == LogOn25:
                if len(row) > extract_column_index:
                    #extracted_text.append(row[6])
                    extract_value = row[extract_column_index]
                    regex = r"<User>(.*?)<\/User>"
                    match = re.search(regex, extract_value)
                    if match:
                        extracted_text.append("LogOn(eventid 25) ")
                        extracted_text.append("User : "+match.group(1)) 
                    regex = r"<SessionID>(.*?)<\/SessionID>"
                    match = re.search(regex, extract_value)
                    if match:
                        extracted_text.append("SessionID : "+match.group(1)) 
                    
                    # 정규 표현식을 사용하여 <Address>와 </Address> 사이의 문자열을 추출
                    regex = r"<Address>(.*?)<\/Address>"
                    match = re.search(regex, extract_value)
                    if match:                        
                        extracted_text.append("Address : "+match.group(1))
                        extracted_text.append("\n")
            elif len(row) > search_column_index and row[search_column_index] == LogOff24:
                if len(row) > extract_column_index:
                    #extracted_text.append(row[6])
                    extract_value = row[extract_column_index]
                    regex = r"<User>(.*?)<\/User>"
                    match = re.search(regex, extract_value)
                    if match:
                        extracted_text.append("LogOff(eventid 24) ")
                        extracted_text.append("User : "+match.group(1)) 
                    regex = r"<SessionID>(.*?)<\/SessionID>"
                    match = re.search(regex, extract_value)
                    if match:
                        extracted_text.append("SessionID : "+match.group(1)) 
                    
                    # 정규 표현식을 사용하여 <Address>와 </Address> 사이의 문자열을 추출
                    regex = r"<Address>(.*?)<\/Address>"
                    match = re.search(regex, extract_value)
                    if match:                        
                        extracted_text.append("Address : "+match.group(1))
                        extracted_text.append("\n")
            elif len(row) > search_column_index and row[search_column_index] == LogOn4624:
                if len(row) > extract_column_index:                    
                    extract_value = row[extract_column_index]
                    regex = r"<Data Name=\"LogonType\">10</Data>" #|<Data Name=\"LogonType\">3</Data>|<Data Name=\"LogonType\">11</Data>
                    match = re.search(regex, extract_value)
                    if match:
                        #extracted_text.append(row[6])                         
                        regex = r"<Data Name=\"TargetUserName\">(.*?)<\/Data>"
                        match = re.search(regex, extract_value)
                        if match:
                            extracted_text.append("LogOn(eventid 4624) ")
                            extracted_text.append("TargetUserName : "+match.group(1)) 
                        regex = r"<Data Name=\"TargetDomainName\">(.*?)<\/Data>"
                        match = re.search(regex, extract_value)
                        if match:
                            extracted_text.append("TargetDomainName : "+match.group(1)) 
                        
                        # 정규 표현식을 사용하여 <Address>와 </Address> 사이의 문자열을 추출
                        regex = r"<Data Name=\"TargetLogonId\">(.*?)<\/Data>"
                        match = re.search(regex, extract_value)
                        if match:                        
                            extracted_text.append("TargetLogonId : "+match.group(1))
                        
                        regex = r"<Data Name=\"LogonType\">(.*?)<\/Data>"
                        match = re.search(regex, extract_value)
                        if match:
                            extracted_text.append("LogonType : "+match.group(1))
                        
                        regex = r"<Data Name=\"IpAddress\">(.*?)<\/Data>"
                        match = re.search(regex, extract_value)
                        if match:                        
                            extracted_text.append("IpAddress : "+match.group(1))
                            extracted_text.append("\n")
                    else:
                        continue

            elif len(row) > search_column_index and row[search_column_index] == LogOff4634:
                if len(row) > extract_column_index:
                    extract_value = row[extract_column_index]
                    regex = r"<Data Name=\"LogonType\">10</Data>" #|<Data Name=\"LogonType\">3</Data>|<Data Name=\"LogonType\">11</Data>
                    match = re.search(regex, extract_value)
                    if match:
                        #extracted_text.append(row[6])
                        regex = r"<Data Name=\"TargetUserName\">(.*?)<\/Data>"
                        match = re.search(regex, extract_value)
                        if match:
                            extracted_text.append("LogOff(eventid 4634) ")
                            extracted_text.append("TargetUserName : "+match.group(1)) 
                        regex = r"<Data Name=\"TargetDomainName\">(.*?)<\/Data>"
                        match = re.search(regex, extract_value)
                        if match:
                            extracted_text.append("TargetDomainName : "+match.group(1)) 
                        
                        # 정규 표현식을 사용하여 <Address>와 </Address> 사이의 문자열을 추출
                        regex = r"<Data Name=\"TargetLogonId\">(.*?)<\/Data>"
                        match = re.search(regex, extract_value)
                        if match:                        
                            extracted_text.append("TargetLogonId : "+match.group(1))
                        
                        regex = r"<Data Name=\"LogonType\">(.*?)<\/Data>"
                        match = re.search(regex, extract_value)
                        if match:                        
                            extracted_text.append("LogonType : "+match.group(1))
                            extracted_text.append("\n")
                    else:
                        continue
            elif len(row) > search_column_index and row[search_column_index] == LogOn1149:
                if len(row) > extract_column_index:
                    #extracted_text.append(row[6])
                    extract_value = row[extract_column_index]
                    regex = r"<Param1>(.*?)<\/Param1>"
                    match = re.search(regex, extract_value)
                    if match:
                        extracted_text.append("LogOn(eventid 1149) ")
                        extracted_text.append("User : "+match.group(1))                     
                    regex = r"<Param3>(.*?)<\/Param3>"
                    match = re.search(regex, extract_value)
                    if match:                        
                        extracted_text.append("Address : "+match.group(1))
                        extracted_text.append("\n")       

            
    with open(output_file, 'w', encoding='utf-8', newline='') as file:
        csv_writer = csv.writer(file)
        threadeddata = []
        for data in extracted_text:            
            if(data == '\n'):
                csv_writer.writerow(threadeddata)
                threadeddata.clear()
                continue
            else:
                threadeddata.append(data)
                


    
# .csv 파일 경로와 이름
csv_file = 'KAV.csv'

# 특정 문자열을 찾을 열의 인덱스
search_column_index = 3

# 찾을 문자열
LogOn21 = '21'
LogOn25 = '25'
LogOff24 = '24'
LogOn1149 = '1149'

LogOn4624 = '4624'
LogOff4634 = '4634'

# 추출할 문자열을 포함한 열의 인덱스
extract_column_index = 14

# .txt 파일 경로와 이름
output_file = 'output.csv'

# 함수 호출
extract_text_from_csv(csv_file, search_column_index, extract_column_index, output_file)