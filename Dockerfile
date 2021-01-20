FROM python:3.6-alpine

# set up folder
WORKDIR /home/iljaz

# copy everything into it
COPY . .

# install dependencies
RUN pip install -r requirements.txt

# actually run the app
EXPOSE 5000
# option 1
CMD python app.py

# option 2
# ENTRYPOINT [ "python" ]
# CMD [ "app.py" ]

# ------------------------------------------------------------------------------
# then
# 1) to build:
# docker build -t iljaz_app:latest .
# 2) to run)
# IMPORTANT - make sure to include the p argument, which makes the port available on your machine so you can access it
# IMPORTANT2 - second port is CONTAINER, first port is your local machine
# docker run -d -p 80:5000 iljaz_app
