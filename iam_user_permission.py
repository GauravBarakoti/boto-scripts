import boto3

client = boto3.client('iam')

response = client.list_users()
for user in response['Users']:
    name=user['UserName']
    print("User: ",user['UserName'])
    inline=client.list_user_policies(
        UserName=name
    )
    print("InLine Policy: ", inline['PolicyNames'])
    listPolicy = client.list_attached_user_policies(
        UserName=name
    )
    for policy in listPolicy['AttachedPolicies']:
        print("Attached Policies: ",policy['PolicyName'])
    print()


# response = client.get_user(
#     UserName='aws_cli'
# )
# print(response)

# response = client.get_user(
#     UserName='aws_cli'
# )
# # print(response)
# print(response['User']['Path'])

