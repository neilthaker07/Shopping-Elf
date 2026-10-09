from pyfcm import FCMNotification
#from uregression import estimate_days


push_service = FCMNotification(api_key="x")

registration_id = ["x"]

message_title ="Shopping notification"
message_body="6"
print message_body
result = push_service.notify_multiple_devices(registration_ids=registration_id, message_title=message_title, message_body=message_body)

#print result
