
# service-registry-connector

Connects to a service registry

## Component context

* service-registry-connector inputs JSON from: [service-registry-registration-orchestrator](./service-registry-registration-orchestrator.md) via http get



``` plantuml
component "service_registry_connector" as service_registry_connector
component "service_registry_registration_orchestrator" as service_registry_registration_orchestrator
service_registry_registration_orchestrator  -->  service_registry_connector  :JSON

```