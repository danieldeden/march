
# service-execution-worker

Acts as a worker that is capable of executing an specification from specification-item using a specified service-technology.

## Component context

* service-execution-worker inputs Manage from: [service-execution-handler](./service-execution-handler.md) via Manage



``` plantuml
component "service_execution_worker" as service_execution_worker
component "service_execution_handler" as service_execution_handler
service_execution_handler  -->  service_execution_worker  :Manage

```