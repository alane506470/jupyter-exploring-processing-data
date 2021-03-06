
import os
from dotenv import find_dotenv,load_dotenv
from requests import session
import logging
import csv
from contextlib import closing
payload={
    'eamil': os.environ.get("KAGGLE_USERNAME"),
    'password': os.environ.get("KAGGLE_PASSWORD"),
    'X-XSRF-TOKEN': 'CfDJ8LdUzqlsSWBPr4Ce3rb9VL_y_NbFaUd3UvKyA87g-6f_duSDyTbcvnSdqgsUUd6f9nZZgzvwtknzZy7kB1hVo4NezWLbcDUCa0dwX2diSkdFx6_nXb0oy0eNClalAHBUBJB0YPXmzvED6srSMEKcLjY'
}

def extract_data(url, file_path):
    with session() as c:
        with open(file_path,'w',encoding="utf-8") as handle:
            with closing(c.get(url,verify=False,stream=True)) as r:
                lines = (line.decode('utf-8') for line in r.iter_lines())
                for row in csv.reader(lines):
                    handle.write("".join(row))
def main(project_dir):
    logger= logging.getLogger(__name__)
    logger.info('getting raw data')
    
    train_url = 'https://apiservice.mol.gov.tw/OdService/download/A17000000J-020067-bVl'
    test_url = 'https://apiservice.mol.gov.tw/OdService/download/A17000000J-020028-cAw'
    raw_data_path = os.path.join(project_dir,'data', 'raw')
    train_data_path = os.path.join(raw_data_path,'train.csv')
    test_data_path = os.path.join(raw_data_path, 'test.csv')
    
    extract_data(train_url,train_data_path)
    extract_data(test_url,test_data_path)
    logger.info('downloadend raw training and test data')
    
#os.path.dirname()-返回目錄名稱和路徑包含檔案
#os.pardir-往上一層
if __name__ =='__main__':
    project_dir = os.path.join(os.path.dirname(__file__),os.pardir,os.pardir)
    
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO,format=log_fmt)
    
    dotenv_path = find_dotenv()
    load_dotenv(dotenv_path)
    
    main(project_dir)
    
