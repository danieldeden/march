
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
component "test_component2" as test_component2
component "test_component3" as test_component3
database "database" as database0
test_component  -->  test_component2  :raw JSON
test_component  -->  test_component3  :raw JSON
test_component3  ->  database0  :database connection

```


## Data Flow