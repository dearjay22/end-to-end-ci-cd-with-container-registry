## Explanation of Parameters

### Top‑level workflow fields

| Parameter                  | Description                                                                                                                         |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **name**                   | A human‑readable name for your workflow (shown in the UI).                                                                          |
| **on**                     | Which events trigger this workflow. Can list one or more of: `push`, `pull_request`, `workflow_dispatch` (manual), `schedule`, etc. |
|   └ **push**               | Triggers on pushes. You can scope by `branches`, `tags`, or `paths`.                                                                |
|   └ **pull\_request**      | Triggers on PR events. Also supports scoping by `branches`, `paths`, etc.                                                           |
|   └ **workflow\_dispatch** | Allows manual runs from the Actions tab.                                                                                            |
| **env**                    | Global environment variables available to all jobs and steps.                                                                       |
| **defaults**               | Default settings for all `run:` steps (e.g. default `shell`, default `working-directory`).                                          |
| **permissions**            | Fine‑grained permissions granted to `GITHUB_TOKEN`. Use least privilege (e.g. `contents: read`, `id-token: write`).                 |

### Jobs

A workflow is composed of one or more **jobs**. Each job runs in its own fresh runner (unless you specify a `container` or `services`).

| Parameter       | Description                                                                                                        |
| --------------- | ------------------------------------------------------------------------------------------------------------------ |
| **jobs**        | Top‑level key under which you declare each job (e.g. `build`, `test`, `deploy`).                                   |
| **\<job\_id>**  | Identifier for the job (must be unique).                                                                           |
| **name**        | Friendly display name for the job.                                                                                 |
| **runs-on**     | Runner image or label (e.g. `ubuntu-latest`, `windows-latest`, `macos-latest`, or self-hosted label).              |
| **needs**       | List of jobs that must complete successfully before this one starts.                                               |
| **if**          | A [conditional expression](https://docs.github.com/actions/learn-github-actions/expressions) that gates execution. |
| **environment** | Deployment environment name (and optional `url`) for environment protection rules.                                 |
| **strategy**    | Configuration for parallel or matrix builds.                                                                       |
|   └ **matrix**  | Defines one or more axes of variation (e.g. Node versions, OSes). The job runs once per combination.               |
| **steps**       | Ordered list of steps (actions or shell commands) that make up the job.                                            |

### Steps

Each job’s `steps` array can include:

| Parameter | Description                                                                                           |     |
| --------- | ----------------------------------------------------------------------------------------------------- | --- |
| **uses**  | Runs a pre‑built [action](https://github.com/marketplace?type=actions). Format: `owner/name@version`. |     |
| **run**   | Executes shell commands. Supports multi‑line scripts with \`                                          | \`. |
| **name**  | Human‑readable label for the step (appears in the UI).                                                |     |
| **with**  | Key/value inputs for the action you’re using. Keys are action‑specific.                               |     |
| **env**   | Step‑level environment variables (override job or workflow `env`).                                    |     |

#### Common action inputs (`with:`)

* **actions/setup-node\@v3**

  * `node-version`: (Required) Node.js version to install (e.g. `14.x`, `16.x`).

* **aws-actions/configure-aws-credentials\@v1**

  * `aws-access-key-id`
  * `aws-secret-access-key`
  * `aws-region`

*(Always consult the action’s Marketplace page for the full list of supported inputs.)*

---

### Other optional workflow keys

GitHub Actions supports many more parameters you may find useful:

* **concurrency**: Cancel in‑progress runs for the same concurrency group.
* **container**: Run a job inside a Docker container.
* **services**: Attach supporting containers (e.g. databases) to a job.
* **timeout-minutes**: Max execution time for a job before it’s canceled.
* **continue-on-error**: Allow a step or job to fail without failing the entire workflow.
* **outputs**: Export values from one job/step for downstream consumption.
* **secrets**: Access sensitive values via `${{ secrets.MY_SECRET }}`.
* **permissions**: Override the top‑level `permissions` at the job level.

For a deep dive into every possible field, see the official reference:
[https://docs.github.com/actions/reference/workflow-syntax-for-github-actions](https://docs.github.com/actions/reference/workflow-syntax-for-github-actions)
