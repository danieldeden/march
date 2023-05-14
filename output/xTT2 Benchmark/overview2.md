
# Full xTT2 Service Handling

## Description

xTT - Extensible Test Tool. It has the ability to take the place of a system service and preform requests and respones as it was that service. Thus is used both for testing integrations with contract validation and for scenario-tests with with a set of predetermained responses to a set of queries.

The purpose of this system is to test complex functionality in big SOA systems.

## System components

* [service-execution-handler](./components/service-execution-handler.md):  Management of service-execution-worker's.
* [service-execution-worker](./components/service-execution-worker.md):  Acts as a worker that is capable of executing an specification from specification-item using a specified service-technology.
* [service-registry-connector](./components/service-registry-connector.md):  Connects to a service registry
* [service-registry-for-service-orchestrator](./components/service-registry-for-service-orchestrator.md):  Aids in finding the correct service-registry for a specific service being executed in a project.
* [service-registry-registration-orchestrator](./components/service-registry-registration-orchestrator.md):  Acts as an orchestrator between service-execution-handler and the individual service-registry-connector components.

``` plantuml
component "service_execution_handler" as service_execution_handler
component "service_execution_worker" as service_execution_worker
component "service_registry_connector" as service_registry_connector
component "service_registry_for_service_orchestrator" as service_registry_for_service_orchestrator
component "service_registry_registration_orchestrator" as service_registry_registration_orchestrator
service_execution_handler  -->  service_execution_worker  :Manage : Manage
service_execution_handler  -->  service_registry_registration_orchestrator  :JSON : http get
service_registry_registration_orchestrator  -->  service_registry_connector  :JSON : http get
service_registry_registration_orchestrator  -->  service_registry_for_service_orchestrator  :JSON : http get

```