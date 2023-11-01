import time, json
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

def helloword1(self, params, packet):
    print('Received Message from AWS IoT Core')
    print('Topic: ' + packet.topic)
    value = json.loads(packet.payload.decode('utf-8'))
    print("Payload: ", value)


def helloword2(self, params, packet):
    print('Received Message from AWS IoT Core')
    print('Topic: ' + packet.topic)
    value = json.loads(packet.payload.decode('utf-8'))
    print("Payload: ", value)


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

myMQTTClinet.subscribe("/101/in", 1, helloword1)
myMQTTClinet.subscribe("/101/out", 1, helloword2)
myMQTTClinet.subscribe("/111/in", 1, helloword3)
myMQTTClinet.connect()
