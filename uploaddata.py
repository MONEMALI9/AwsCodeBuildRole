import os
import boto3

# instantiate client
client = boto3.client('s3')

# set variable
bucket = '' #<bucketname>
cur_path = os.getcwd()
file = ''   #<filename.csv>
filename = os.path.join(cur_path,'data',file)

# open file
data = open(filename,'rb')

#load data int s3
client.upload_file(filename,bucket,file)
