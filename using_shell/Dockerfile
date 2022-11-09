FROM ubuntu:20.04

# Time Zone
ENV TZ=Europe/Vienna
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Make /app as working directory
WORKDIR /app

RUN mkdir -p /app/smbmount /app/smbconfig
COPY main.sh /app/smbconfig
RUN chmod +x  /app/smbconfig/main.sh

# Install dependencies
RUN apt update && \
    apt -y upgrade && \
    apt install -y smbclient cifs-utils nginx && \
    apt clean && rm -rf /var/lib/apt/lists/*

COPY default /etc/nginx/sites-available/default

# Run Python Script
ENTRYPOINT [./app/smbconfig/main.sh]

# port
EXPOSE 80

# Run the Nginx server
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]
