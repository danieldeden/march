
# test-component

Some short description of test-component

## Component context



* test-component outputs raw JSON to: [test-component2](./test-component2.md) via pub/sub
* test-component outputs raw JSON to: [test-component3](./test-component3.md) via pub/sub

``` plantuml
component "test_component" as test_component
queue "queue" as queue0
component "test_component2" as test_component2
component "test_component3" as test_component3
queue0  ->  test_component  :pub/sub
test_component  -->  test_component2  :raw JSON
test_component  -->  test_component3  :raw JSON

```

## Use case

``` plantuml

left to right direction
actor Guest as g
package Professional {
actor Chef as c
actor "Food Critic" as fc
}
package Restaurant {
usecase "Eat Food" as UC1
usecase "Pay for Food" as UC2
usecase "Drink" as UC3
usecase "Review" as UC4
}
fc --> UC4
g --> UC1
g --> UC2
g --> UC3
```

## Sequence Diagram


``` plantuml

Alice -> Bob: Authentication Request
Bob --> Alice: Authentication Response
Alice -> Bob: Another authentication Request
Alice <-- Bob: Another authentication Response
```
