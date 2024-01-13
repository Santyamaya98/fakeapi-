FROM python3.8

WORKDIR /country_plot
COPY requirements.txt /country_plot/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /country_plot/requirements.txt 

COPY . / country_plot/

CMD bash -c "while true: do sleep 1; done"