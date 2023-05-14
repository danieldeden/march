
# service-registry-registration-orchestrator

Acts as an orchestrator between service-execution-handler and the individual service-registry-connector components.

## Component context

* service-registry-registration-orchestrator inputs JSON from: [service-execution-handler](./service-execution-handler.md) via http get

* service-registry-registration-orchestrator outputs none to: [service-registry-connector](./service-registry-connector.md) via none
* service-registry-registration-orchestrator outputs none to: [service-registry-for-service-orchestrator](./service-registry-for-service-orchestrator.md) via none

``` plantuml
component "service_registry_registration_orchestrator" as service_registry_registration_orchestrator
component "service_execution_handler" as service_execution_handler
component "service_registry_connector" as service_registry_connector
component "service_registry_for_service_orchestrator" as service_registry_for_service_orchestrator
service_execution_handler  -->  service_registry_registration_orchestrator  :JSON
service_registry_registration_orchestrator  -->  service_registry_connector  :none
service_registry_registration_orchestrator  -->  service_registry_for_service_orchestrator  :none

```