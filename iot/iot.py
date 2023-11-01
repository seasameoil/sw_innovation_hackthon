import time, json
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

count = [0]
fire = [False]
crime = ["OFF"]


def helloword1(self, params, packet):
    print('Received Message from AWS IoT Core')
    print('Topic: ' + packet.topic)
    value = json.loads(packet.payload.decode('utf-8'))
    print("Payload: ", value)
    count[0] = value['count']
    fire[0] = value['fire']
    crime[0] = value['crime']


def helloword2(self, params, packet):
    print('Received Message from AWS IoT Core')
    print('Topic: ' + packet.topic)
    value = json.loads(packet.payload.decode('utf-8'))
    print("Payload: ", value)
    fire[0] = value['fire']


def helloword3(self, params, packet):
    print('Received Message from AWS IoT Core')
    print('Topic: ' + packet.topic)
    value = json.loads(packet.payload.decode('utf-8'))
    print("Payload: ", value)


myMQTTClinet = AWSIoTMQTTClient("MyTest2")
myMQTTClinet.configureEndpoint("a34lkk6u0zedod-ats.iot.ap-northeast-2.amazonaws.com", 8883)
myMQTTClinet.configureCredentials("C:/Users/jeongho/certs/AmazonRootCA1.pem", "C:/Users/jeongho/certs/private.pem.key", "C:/Users/jeongho/certs/device.pem.crt")
myMQTTClinet.configureOfflinePublishQueueing(-1)
myMQTTClinet.configureDrainingFrequency(2)
myMQTTClinet.configureConnectDisconnectTimeout(10)
myMQTTClinet.configureMQTTOperationTimeout(5)
print("Initiating IoT Core Topic ...")
myMQTTClinet.connect()

myMQTTClinet.subscribe("test1", 1, helloword1)

