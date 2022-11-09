FROM ubuntu:20.04

# Time Zone
ENV TZ=Europe/Vienna
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Make /app as working directory
WORKDIR /app

RUN mkdir -p /app/smbmount /app/smbconfig
COPY main.py /app/smbconfig

# Install dependencies
RUN apt update && \
    apt -y upgrade && \
    apt install -y smbclient cifs-utils python3-pip nginx && \
    apt clean && rm -rf /var/lib/apt/lists/*

COPY default /etc/nginx/sites-available/default

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


# Run Python Script
ENTRYPOINT ["python3", "/app/smbconfig/main.py"]

EXPOSE 80
# Run the Nginx server
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]
