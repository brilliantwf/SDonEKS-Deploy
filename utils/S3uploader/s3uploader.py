import argparse
import boto3
import urllib3
import csv

# 初始化S3客户端
session = boto3.Session(profile_name='ue1')
s3 = session.client('s3')

# 读取CSV文件
def read_csv(csv_file):
    urls = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            urls.append(row)
    return urls

# 下载文件并上传到S3
def download_and_upload_to_s3(url, bucket, key):
    http = urllib3.PoolManager()
    response = http.request('GET', url, preload_content=False)
    s3.upload_fileobj(http.request('GET', url,preload_content=False), bucket, key)
    response.release_conn()

def main(csv_file):
    # 读取CSV文件
    urls = read_csv(csv_file)
    for row in urls:
        url = row['url']
        bucket = row['bucket']
        key = row['key']
        
        try:
            download_and_upload_to_s3(url, bucket, key)
            print(f"正在下载 {url} 到S3桶{bucket}/{key}")
        except Exception as e:
            print(f"Failed to download and upload {url} to S3 bucket {bucket} with key {key}: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download and upload files from a CSV to S3')
    parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    args = parser.parse_args()
    main(args.csv_file)
