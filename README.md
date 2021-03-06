# 딥러닝 인퍼런스를 위한 RabbitMQ 데모입니다.

사용 방법은 다음과 같습니다.

RabbitMQ를 설치합니다. 자세한 설치 방법은 RabbitMQ 공식 문서를 보세요.

의존 패키지는 다음과 같습니다.

```
pika
pickle
```

`rpc_server.py`에 `load_model()` 함수를 변경하여 모델을 로드하도록 합니다.

별도의 터미널을 열어서 

```
python rpc_server.py
```

를 실행합니다. 그러면 서버 대기 상태가 됩니다.


`rpc_client_demo.py`를 보면 간단한 예제가 있습니다.

```
client = RpcClient()
pred = client(img)
```

`RpcClient` 개체를 생성하고 이미지를 전달하고 처리한 결과를 받습니다.

RabbitMQ로 주고 받을 수 있는 데이터는 바이트배열이나 문자열입니다. 전송하기 전에 반드시 포맷을 변경해야 함에 주의 합니다.

별도의 블로그 글은 [이곳](https://booiljung.github.io/technical_articles/machine_learning/rabbitmq_demo_for_machine_learning_inference.html?fbclid=IwAR237Sor0DkyLh7IRajg4YV_3TawzGDkR30c77UsXRB8ctCtENsIJ8RX2Fk)에서 확인할 수 있습니다.
