from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'new_topic', 
    bootstrap_servers=['kfk.x:14310'],
    auto_offset_reset='earliest')

for message in consumer:
    key = message.key.decode()
    value = message.value.decode()
    print("receive, key: {}, value: {}".format(key, value))

    try:
        data = json.loads(value)
        prodId = data.get('prodId')
        type = data.get('type')
        deviceId = data.get('deviceId')
        spaceCode = data.get('spaceCode')
        payload = data.get('payload')
        id = data.get('id')
        time = data.get('time')
        projectId = data.get('projectId')

        print("Parsed data:")
        print("prodId:", prodId)
        print("type:", type)
        print("deviceId:", deviceId)
        print("spaceCode:", spaceCode)
        print("payload:", payload)
        print("id:", id)
        print("time:", time)
        print("projectId:", projectId)

    except json.JSONDecodeError as e:
        print("Failed to parse JSON data:", e)

    print()  # empty line for separation
