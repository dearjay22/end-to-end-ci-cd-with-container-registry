## Explanation of Parameters

### `version`

* **Type**: string
* **Description**: Buildspec format version. `0.2` is the current, recommended version.

---

### `env`

Defines environment variables available during all phases.

| Sub‑key             | Description                                                                         |
| ------------------- | ----------------------------------------------------------------------------------- |
| **variables**       | Plaintext key/value pairs you set directly in the spec.                             |
| **parameter-store** | Map of names to AWS SSM Parameter Store paths; fetched at runtime.                  |
| **secrets-manager** | Map of names to Secrets Manager ARNs or secret paths; supports JSON key extraction. |

> Variables from Parameter Store or Secrets Manager are injected into the build container as environment variables.

---

### `phases`

Defines ordered lifecycle stages; each may include `commands` and (in v0.2) `runtime-versions`.

| Phase           | Purpose                                                                                           |
| --------------- | ------------------------------------------------------------------------------------------------- |
| **install**     | Prepare the environment: install dependencies, specify runtimes via `runtime-versions`.           |
| **pre\_build**  | Authentication or pre-check steps (e.g., ECR login, version checks).                              |
| **build**       | The main build steps: compile code, build images, run scripts.                                    |
| **post\_build** | Actions after build completes: push artifacts, generate metadata (e.g., `imagedefinitions.json`). |

* **`runtime-versions`**: specify versions for supported runtimes (e.g. `nodejs`, `python`, `java`, `docker`).
* **`commands`**: list of shell commands. Supports multi‑line blocks with `|`.

---

### `reports`

(Optional) Collect and publish test or coverage report files.

| Parameter          | Description                                              |
| ------------------ | -------------------------------------------------------- |
| **<report-name>**  | Arbitrary key naming a report group.                     |
| **files**          | Glob patterns for report files.                          |
| **base-directory** | Directory under which to search for files.               |
| **file-format**    | Format identifier (e.g. `JACOCO`, `COVERAGE`, `TESTNG`). |

---

### `artifacts`

Describes the files to return to CodePipeline or S3 after a successful build.

| Parameter          | Description                                                                |
| ------------------ | -------------------------------------------------------------------------- |
| **files**          | Glob patterns of files to include (e.g. build outputs, imagedefinitions).  |
| **discard-paths**  | `yes`/`no`; if `yes`, flattens directory paths so only filenames are used. |
| **base-directory** | (v0.2) Root directory for artifacts (defaults to project root if omitted). |
| **name**           | (Optional) Name of the primary artifact.                                   |

---

### `cache`

Speeds up consecutive builds by caching directories between runs.

| Parameter | Description                                                          |
| --------- | -------------------------------------------------------------------- |
| **paths** | List of file/directory patterns to cache (e.g. `node_modules/**/*`). |

---

### `logs`

Configures build logs to external destinations.

| Parameter                  | Description                                                    |
| -------------------------- | -------------------------------------------------------------- |
| **cloudwatch.status**      | `true`/`false`; whether to send build logs to CloudWatch Logs. |
| **cloudwatch.group-name**  | Name of the CloudWatch Logs group.                             |
| **cloudwatch.stream-name** | Name of the log stream within the group.                       |

---

### `timeout-in-minutes`

* **Type**: integer
* **Description**: Maximum allowed build time in minutes before CodeBuild terminates the build. Defaults to 60.

---

#### Notes

* **Secondary artifacts**: you can define multiple artifacts in a `secondary-artifacts:` section if needed.
* **Compute resources** and **cache modes** are defined on the CodeBuild project itself, not in `buildspec.yml`.
* For full reference, see the AWS docs:
  [https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html)
