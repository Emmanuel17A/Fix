# FIX Architecture

FIX separates user interface, shared core, media infrastructure, and media features.

New feature work belongs in plugins unless it is genuinely shared infrastructure.

The current data flow is:

```text
UI -> OperationContext -> Plugin -> Adapter -> OperationPlan
   -> OperationExecutor -> Media Layer -> Validation -> UI
```

The shared `Selection` objects are owned by the application, not by individual plugins.
