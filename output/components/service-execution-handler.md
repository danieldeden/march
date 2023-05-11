
# service-execution-handler

## Description

Management of service-execution-worker's.

The [service-execution-handler](./service-execution-handler.md) 's main resposibility is to manage the [service-execution-worker](./service-execution-worker.md) 's. It will redirect any requests to create, destroy or otherwise manage to the responsible worker.

[service-execution-handler](./service-execution-handler.md) is dependant on [service-execution-item](./service-execution-item.md) and [service-execution-worker-item](./service-execution-worker-item.md), that is tasked with keeping information related to available execution-workers and make that information accessable by the client.

[service-execution-handler](./service-execution-handler.md) also has a flexible dependency on all accessable execution-workers, however a specific execution-worker should not be required for this service to work. The number of execution-workers managed by the handler should scale from 0 to a reasonable amount.

This component should be seen as part of the larger xTT2 service handling system.

## Justification
This component is a result of the decision to use workers for service execution. In order to reduce the complexity of each single execution-worker a handler was chosen to orchistrate the interaction between client and node. Using a worker handler allows more flexibilty when it comes to deployment of said worker nodes.

## Component context



* service-execution-handler outputs Manage to: [service-execution-worker](./service-execution-worker.md) via Manage
* service-execution-handler outputs JSON to: [service-registry-registration-orchestrator](./service-registry-registration-orchestrator.md) via http get

``` plantuml
component "service_execution_handler" as service_execution_handler
component "service_execution_worker" as service_execution_worker
component "service_registry_registration_orchestrator" as service_registry_registration_orchestrator
service_execution_handler  -->  service_execution_worker  :Manage
service_execution_handler  -->  service_registry_registration_orchestrator  :JSON

```