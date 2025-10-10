## Explanation of Parameters

### **trigger**

Controls which pushes trigger the pipeline.

* `branches.include`: list of branch names (or glob patterns) that cause a run on `git push`.

### **pr**

Controls which pull requests trigger the pipeline.

* `branches.include`: list of target branches for PR validation.

### **variables**

Define pipeline‑wide variables.

* `NODE_ENV`: common runtime flag.
* `buildConfiguration`: passed to build scripts (`Debug`/`Release` etc.).

### **stages**

Top‑level grouping into sequential phases. Each stage may contain one or more `jobs`.

---

## **Stage: Build**

```yaml
- stage: Build
  displayName: Build Stage
```

* `stage`: logical identifier, also appears in the UI.
* `displayName`: friendly name shown in the pipeline view.

### **jobs**

Each stage can have multiple parallel jobs; here we use one.

```yaml
jobs:
  - job: BuildJob
    displayName: Build Job
```

* `job`: internal ID, unique within the stage.
* `displayName`: shown under the stage in the UI.

### **pool**

Selects the VM image to run on.

```yaml
pool:
  vmImage: ubuntu-latest
```

* `vmImage`: Microsoft‑hosted agent label (`ubuntu-latest`, `windows-latest`, `macos-latest`).

### **workspace.clean**

Controls workspace cleanup before the job.

```yaml
workspace:
  clean: all
```

* `all`: deletes sources, artifacts, and other files—ensures a fresh start.

### **steps**

Ordered list of actions (tasks or scripts).

#### **Task: NodeTool**

```yaml
- task: NodeTool@0
  displayName: Install Node.js
  inputs:
    versionSpec: '14.x'
```

* `task`: built‑in Azure Pipelines task (`<Name>@<MajorVersion>`).
* `displayName`: label in the logs/UI.
* `inputs.versionSpec`: semver version or range to install.

#### **Script step**

```yaml
- script: |
    npm install
    npm run build -- --configuration $(buildConfiguration)
  displayName: Install dependencies & build
```

* `script`: inline shell commands (on Linux/macOS agents; on Windows use `powershell:` or `bash:`).
* `|`: multi‑line block.
* `$(buildConfiguration)`: variable expansion syntax.

#### **PublishBuildArtifacts**

```yaml
- task: PublishBuildArtifacts@1
  displayName: Publish build artifacts
  inputs:
    pathToPublish: 'dist'
    artifactName: 'drop'
    publishLocation: 'Container'
```

* `pathToPublish`: folder or file path (relative to repo root).
* `artifactName`: logical name under which artifacts are stored.
* `publishLocation`: `Container` sends them to the pipeline’s built‑in artifact store (alternatively `FilePath` or `AzureStorage`).

---

## **Stage: Test**

Triggered only after **Build** succeeds:

```yaml
dependsOn: Build
```

* `dependsOn`: lists prior stage(s) that must finish before this one.

### **Condition**

The **Deploy** stage uses a condition; Test implicitly runs if `Build` succeeds.

---

### **PublishTestResults**

```yaml
- task: PublishTestResults@2
  displayName: Publish test results
  inputs:
    testResultsFormat: JUnit
    testResultsFiles: 'reports/junit.xml'
    failTaskOnFailedTests: true
```

* `testResultsFormat`: format of the test report (e.g. `JUnit`, `NUnit`, `VSTest`).
* `testResultsFiles`: glob path to result files.
* `failTaskOnFailedTests`: whether failures should mark the step (and thus pipeline) as failed.

---

## **Stage: Deploy**

Runs only if **Test** succeeded:

```yaml
dependsOn: Test
condition: succeeded()
```

* `condition`: Azure Pipelines expression language; `succeeded()` means all prior stages/jobs were successful.

### **deployment job**

```yaml
- deployment: DeployJob
  displayName: Deploy to Azure Web App
  environment: production
```

* `deployment`: special job type for deployments.
* `environment`: name of the target environment (maps to Azure Pipelines Environments feature for approvals, resource checks, and secrets).

### **download: current**

```yaml
- download: current
  displayName: Download artifacts
```

* Fetches artifacts published earlier in the pipeline.
* `current`: alias for this pipeline’s published artifacts.

### **AzureWebApp task**

```yaml
- task: AzureWebApp@1
  displayName: Deploy to Web App
  inputs:
    azureSubscription: 'MyServiceConnection'
    appType: webAppLinux
    appName: 'my-app-service'
    package: '$(Pipeline.Workspace)/drop/**/*.zip'
```

* `azureSubscription`: name of an Azure Resource Manager service connection configured in the project.
* `appType`: type of Web App (`webApp`, `webAppLinux`, `functionApp` etc.).
* `appName`: name of your Azure App Service instance.
* `package`: path to the zip or folder to deploy (you can use wildcards).

---

## **Additional Optional Keys**

* **resources**: pull in other repositories, containers, or package feeds.
* **schedules**: define cron‑style scheduled triggers.
* **parameters**: static, type‑checked inputs you can pass at queue time.
* **extends**: inherit from a template YAML.
* **timeoutInMinutes** (at job level): how long Azure should wait before cancelling.
* **variables**: can be scoped to stages or jobs, and support templates, runtime parameters, and secret variables.

For full reference, see Microsoft’s docs:
[https://docs.microsoft.com/azure/devops/pipelines/yaml-schema/](https://docs.microsoft.com/azure/devops/pipelines/yaml-schema/)