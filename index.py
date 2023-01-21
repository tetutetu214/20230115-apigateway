import base64
import json
import boto3

table_name = 'mailaddress'

#DynamoDBオブジェクト
dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
  try:
    #フォームの入力データを得る
    body = event['body']
    if event['isBase64Encoded']:
      body = base64.b64decode(body)

    decoded = json.loads(body)
    username = decoded['username']
    email = decoded['email']
    notsend = decoded['notsend']
    send = decoded['send']


    #mailaddressテーブルに登録する
    item = {
      'username' : {'S': username},
      'email' : {'S': email},
      'notsend' : {'N': notsend},
      'send' : {'N': send}
    } 
    
    dynamodb.put_item(TableName=table_name, Item=item)

    #結果を返す
    return json.dumps({})
