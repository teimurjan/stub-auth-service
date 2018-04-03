FROM python:3.6.2-alpine3.6
WORKDIR /app
ADD requirements.txt ./
RUN apk add --update && pip install -r requirements.txt
ADD backend ./
EXPOSE 5000
CMD ["gunicorn", "app:create_app()", "-b",  "0.0.0.0:5000"]