
# service-registry-for-service-orchestrator

Aids in finding the correct service-registry for a specific service being executed in a project.

## Component context

* service-registry-for-service-orchestrator inputs JSON from: [service-registry-registration-orchestrator](./service-registry-registration-orchestrator.md) via http get



``` plantuml
component "service_registry_for_service_orchestrator" as service_registry_for_service_orchestrator
component "service_registry_registration_orchestrator" as service_registry_registration_orchestrator
service_registry_registration_orchestrator  -->  service_registry_for_service_orchestrator  :JSON

```