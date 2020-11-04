curl -d '{"tweet": "i hate you bitch just die"}' -H "Content-Type: application/json" -X POST http://localhost:8000/tweet

curl -d '{"sepal_length" : 1.0,    "sepal_width" : 1.0,    "petal_length" : 1.0,    "petal_width" : 1.0}' -H "Content-Type: application/json" -X POST http://localhost:8000/iris
