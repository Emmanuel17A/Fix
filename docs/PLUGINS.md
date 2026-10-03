# Plugin Development

Create a new operation under:

```text
src/fix/plugins/<plugin_name>/
├── __init__.py
├── plugin.py
└── adapter.py
```

Use lowercase `snake_case`.

`plugin.py` defines metadata and creates the adapter.

`adapter.py` validates `OperationContext` and builds an `OperationPlan`.

Plugins should use the shared media layer instead of directly duplicating FFmpeg execution.
