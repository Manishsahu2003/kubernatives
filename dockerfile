FROM redhat/ubi8

RUN yum install python3 -y

RUN pip3 install flask

COPY kube.py /kube.py

CMD ['python3','kube.py']
