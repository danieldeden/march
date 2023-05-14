# March documentation #

This repository shows the prototype system used by Jack Florberg in this thesis (computer science and engineering, bachelor's level). The prototype system is based upon [DollarDoc](https://github.com/dollardoc/dollardoc) and is intended to facilitate the process of documenting a system's architecture by using object-orientation.

## Description

The project contains architectural documentation for:

* A demo/dummy system that has no functionallity but rather serves to demonstrate the process of generating architectural views and diagrams based on metadata and is/was used for testing purposes.
* xTT2 benchmark that shows how actual architectural documentation can be structured to display complex information, while being easy to maintain.

>NOTE: The xTT2 documentation in this project is only for demonstrating purposes and shouldn't be used for studying the xTT2 architecture. Instead refer to the [xTT2 repository](https://bitbucket.org/bnearit/xtt2/src/master/documentation/architecture/docs/)

## How it works

The system works by utilizing [DollarDoc](https://github.com/dollardoc/dollardoc) to define metadata in the header section of a `.mdd` file. This metadata is then used to link objects together and generate text and diagrams upon compilation.

This projects has introduced two object types. Component and context.

### Components

Think of components like microservices or any other service that takes an input, does some work and then outputs some data.

A component type should use the following header interface:

``` component dollar-file
---
id: some-name-string
type: component

title: some-title
description: Some short description of $this.title

inputs: 
    components:
        - some-component
    formats:
        - some-format-string
    protocols: 
        - some-protocol-string
outputs:
    components:
        - $some-output-component
    formats:
        - some-format-string
    protocols: 
        - some-protocol-string

contexts:
    components:
        - $some-context
---
```

Input/output components can either be a string value or a reference to a dollar-object. By using the `$` sign, a reference to another component can be made as shown in the outputs/components list. The current implementation requires all fields to have some sort of value, if a component for instance does not have a component it outputs to, the keyword `none` is used to indicate this.

Components can be applied to one or multiple context(s) and utilize the dollar-function `$$ComponentContext($this)`, which displays a component diagram based on the metadata of the specific compoents header section, as well as some describing text.

### Context

A context acts as a architectural view of the system and maintains a list of components.

A dollarfile with the type `context` can utilize the dollar-function `$$GenerateContextView($this)`, which generates a component diagram of all components that are subscribed to the context, as well as a list that describes each component and contains a link to their respective page. The context view is generated based solely on metadata.

## Built in support

The primary intent for the component interface is to link dollar-objects together, however since it is common to want to display queues, interfaces and databases in diagrams that represents an overview of the system, these three types are supported in the generation process.

To use these, simply include the string `queue` or `database` in the name of an input or output component in the header section of a component that has this connection. `Interface` is used as default.


Example output:
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