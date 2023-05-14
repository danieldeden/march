
# test-component3

Some short description of test-component3

## Component context

* test-component3 inputs formatted JSON from: [test-component](./test-componenet.md) via stream



``` plantuml
component "test_component3" as test_component3
component "test_component" as test_component
database "database" as database0
test_component  -->  test_component3  :formatted JSON
test_component3  ->  database0  :database connection

```

## Use case


