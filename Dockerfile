FROM fishtownanalytics/dbt:0.21.0

WORKDIR /app
COPY . .
WORKDIR /app/dbt/dbt_training

# install dependencies
RUN dbt deps
