# Co-Resolve CI/CD Agent Integration Testing Template

This repository is a starter/testing template designed to demonstrate and verify the **Co-Resolve CI/CD Agent** in action.

Because external users do not have direct write permission to this repository, they cannot trigger workflow runs here. To run a demo, **you must create your own copy of this template**.

Follow the step-by-step instructions below to set up your own end-to-end integration test.

---

## Prerequisites
1. **GitHub Account**: To create your repository copy and configure webhooks.
2. **ngrok**: To forward public webhooks to your local running instance.
3. **Docker**: Running locally (the agent executes tests inside an isolated Docker sandbox).

---

## Step-by-Step Setup Tutorial

### 1. Fork this repo from GitHub.

### 2. Configure Your Local Agent Environment
Open your local `co_resolve` agent project directory and make sure your `.env` file contains your credentials.

### 3. Expose Your Local Server and Start the Agent
1. **Start ngrok** in a new terminal window to expose the webhook port (`8000`):
   ```bash
   ngrok http 8000
   ```
   Copy the generated forwarding HTTPS URL (e.g., `https://a1b2-34-56-78-90.ngrok-free.app`).

### 4. Configure the Webhook on GitHub
1. Go to your newly created copy of the repository on GitHub.
2. Click on the **Settings** tab -> **Webhooks** -> **Add webhook**.
3. Fill in the webhook parameters:
   * **Payload URL**: `<your-ngrok-forwarding-url>/api/webhook` (e.g., `https://a1b2-34-56-78-90.ngrok-free.app/api/webhook`).
   * **Content type**: `application/json`
   * **Secret**: The exact value of your `GITHUB_WEBHOOK_SECRET` defined in Step 2.
   * **Which events**: Select **Let me select individual events**, check **Workflow runs**, and ensure everything else is unchecked.
4. Click **Add webhook**. GitHub will send a test ping, which should show a green checkmark indicating a successful `200 OK` response.

Configuration is now done. To see it in action:
### 5. Start the TUI with:
```bash
   python interface/app.py
   ```

### 6. Trigger a Build Failure 
Option A:
   This step can be automated by using /trigger within the TUI command line
Option B:
1. Clone your copy of the testing repository to your local machine:
   ```bash
   git clone https://github.com/your-username/my-co-resolve-testing.git
   cd my-co-resolve-testing
   ```
2. Commit and push (without changes to trigger failing tests) to your main branch:
   ```bash
   git add .
   git commit --allow-empty -m "trigger test failure"
   git push origin main
   ```
3. Navigate to the **Actions** tab on GitHub and watch the workflow run. It will fail.

### 7. Watch the Agent Auto-Resolve the Issue!
When the GitHub Actions workflow fails:
1. GitHub fires a webhook event to your local FastAPI server.
2. The agent detects the failed workflow run, spins up an isolated Docker sandbox, clones your repository, run tests, utilizes its LLM architecture to determine and implement the fix, verifies the fix, and automatically opens a Pull Request with the resolution back to your testing repository.
3. Check the TUI Dashboard at `~/codebase/release/co_resolve` to monitor the agent's real-time reasoning and execution logs!
