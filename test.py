import boto3

s3 = boto3.resource('s3')

#Get bucket names
bucket_names = []

for bucket in s3.buckets.all():
    bucket_names.append(bucket.name)



#Get each bucket objects
for bname in bucket_names:
    print(bname)
    bucket = s3.Bucket(bname)
    for obj in bucket.objects.all():
        print(obj.key, obj.last_modified)
