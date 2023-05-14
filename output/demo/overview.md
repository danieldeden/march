
# System name

## Description

Some short description of System name

The purpose of this system is to...

## System components

* [test-component](./components/test-componenet.md):  Some short description of test-component
* [test-component2](./components/test-component2.md):  Some short description of test-component2
* [test-component3](./components/test-component3.md):  Some short description of test-component3

``` plantuml
component "test_component" as test_component
component "test_component2" as test_component2
component "test_component3" as test_component3
queue "queue" as queue
database "database" as database
test_component  -->  test_component2  :formatted JSON : stream
test_component  -->  test_component3  :formatted JSON : stream
queue  -->  test_component  :raw JSON : pub/sub
test_component3  -->  database  :SQL : database connection

```