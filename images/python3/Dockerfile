FROM python:3-alpine

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app
COPY runcode.py /usr/src/app

RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt -i https://mirrors.aliyun.com/pypi/simple


CMD ["python", "/usr/src/app/runcode.py", "print('hello CodeRunner')"]
