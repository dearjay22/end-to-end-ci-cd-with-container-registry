## Explanation of Parameters

### 1. `pipeline`

The root block for a declarative pipeline. All configuration lives inside.

### 2. `agent`

* **`any`**: run on any available executor.
* You can also specify labels (e.g. `agent { label 'docker' }`) or Docker containers (e.g. `agent { docker 'node:14' }`).

### 3. `environment`

Defines environment variables available to **all** stages and steps.

* `NODE_ENV`: common in Node.js apps to distinguish environments.
* `AWS_REGION`: used by AWS CLI if region isn’t passed on every command.

### 4. `tools`

Declarative shortcut to install or inject tools defined under **Manage Jenkins → Global Tool Configuration**.

* `nodejs 'NodeJS_14'`: tells Jenkins to use the NodeJS installation named “NodeJS\_14”.

### 5. `options`

Job‑level settings:

* **`buildDiscarder(logRotator…)`**: how many builds/days to keep.
* **`timestamps()`**: prefix each log line with a timestamp.
* **`disableConcurrentBuilds()`**: prevents overlapping runs.

### 6. `triggers`

Controls how builds are triggered:

* **`pollSCM('H/5 * * * *')`**: Cron‑style schedule to check for changes. Alternatives include `cron()`, `githubPush()` (GitHub hook), etc.

### 7. `stages` & `stage`

Groups logical phases of your pipeline:

* **`Checkout`**: clones your Git repo.
* **`Install Dependencies`**: runs `npm ci` to install from lockfile.
* **`Build`**: compiles or bundles code (`npm run build`).
* **`Test`**: executes your test suite.
* **`Deploy`**: conditional on branch and uses AWS credentials.

#### Step‑specific directives

* **`checkout scm`**: built‑in step to clone the current repo.
* **`sh '…'`**: run a shell command. Use `bat '…'` on Windows agents.
* **`when { branch 'main' }`**: only run this stage on the `main` branch.
* **`dir('infra') { … }`**: change working directory for enclosed steps, analogous to `working-directory` in GitHub Actions.
* **`credentials('id')`**: fetch a credential by its Jenkins **credentialsId** and expose it as an environment variable.

### 8. `post`

Defines actions after the pipeline completes:

* **`success`** / **`failure`** / **`always`**: different conditions.
* **`mail`**: send an email (requires appropriate plugin).
* **`cleanWs()`**: workspace cleanup helper from the Workspace Cleanup Plugin.

---

### Customization Tips

* **Docker-based builds**:

  ```groovy
  agent {
    docker {
      image 'node:14'
      args  '-v /tmp:/tmp'
    }
  }
  ```
* **Matrix-style builds**: use the [Matrix Plugin](https://plugins.jenkins.io/pipeline-matrix/) for multiple axes.
* **Parallel stages**:

  ```groovy
  stage('Test') {
    parallel {
      unit { steps { sh 'npm run test:unit' } }
      integration { steps { sh 'npm run test:integration' } }
    }
  }
  ```
* **Timed triggers**: use `cron('H 2 * * *')` under `triggers` for nightly runs.
* **Declarative credentials binding**: under `withCredentials([...])` for other types (SSH keys, secret files, tokens).