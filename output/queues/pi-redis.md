
# Test Queue

Some short description of Test Queue

## Protocol

Subscribers

* [Test Page Subscriber 2](../data-subscriber-2.md)
* [Test Page Subscriber](../data-subscriber.md)

Publishers

* [Test Page Publisher](../data-publisher.md)
* [Test Page](../test-page.md)

# UML

``` plantuml
queue "pi-redis" as pi_redis
component "test-page" as test_page
pi_redis -> test_page : some test
```