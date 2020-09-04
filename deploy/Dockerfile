FROM rackspacedot/python37:latest

RUN mkdir -p /tieba-sign

ADD tieba_schedule.py /tieba-sign
ADD requirements.txt /tieba-sign

RUN pip install -r /tieba-sign/requirements.txt

CMD python /tieba-sign/tieba_schedule.py