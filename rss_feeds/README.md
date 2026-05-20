# rss_feeds

## Getting Started

To deploy and manage this bundle, follow these steps:

### 1. Deployment

- Click the **deployment rocket** 🚀 in the left sidebar to open the **Deployments** panel, then click **Deploy**.

### 2. Running Jobs & Pipelines

- To run a deployed job or pipeline, hover over the resource in the **Deployments** panel and click the **Run** button.

### 3. Managing Resources

- Use the **Add** dropdown to add resources to the bundle.
- Click **Schedule** on a notebook within the bundle to create a **job definition** that schedules the notebook.

## Variables

The following variables can be configured when deploying or running this bundle:

| Variable | Description | Default |
| --- | --- | --- |
| `warehouse_id` | The SQL warehouse ID used for SQL tasks | `492d1c843b4cc40a` |

### Overriding Variables

You can override variables via the CLI at deploy or run time:

```bash
databricks bundle deploy --var="warehouse_id=<your_warehouse_id>"
```

Or set per-target overrides in `databricks.yml`:

```yaml
targets:
  prod:
    variables:
      warehouse_id: "<prod_warehouse_id>"
```

## Documentation

- For information on using **Declarative Automation Bundles in the workspace**, see: [Declarative Automation Bundles in the workspace](https://docs.databricks.com/aws/en/dev-tools/bundles/workspace-bundles)
- For details on the **Declarative Automation Bundles format** used in this bundle, see: [Declarative Automation Bundles Configuration reference](https://docs.databricks.com/aws/en/dev-tools/bundles/reference)
