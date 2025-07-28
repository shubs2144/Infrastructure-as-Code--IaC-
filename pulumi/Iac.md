# 📦 Infrastructure as Code (IaC) – In-Depth Notes

---

## ✅ What is IaC?

**Infrastructure as Code (IaC)** means managing and provisioning your cloud infrastructure using **code** instead of manual processes (like clicking in AWS Console).

### 🔧 Traditional Way (Manual):
- Open AWS Console
- Click to create EC2 instance
- Manually configure storage, network, etc.

### 💻 IaC Way:
- Write infrastructure definitions in YAML, JSON, or code (Python, JS).
- Run the code to automatically create and configure infrastructure.

> Think of it as writing code to "build your data center."

---

## 🚀 Benefits of IaC

### 🔁 Repeatable
- Setup can be reused across dev, test, and prod.
- One file = consistent environments.

### ⚡ Faster Deployment
- Infrastructure ready in minutes instead of hours.

### 🛡️ Fewer Errors
- Eliminates manual mistakes.
- Scripts behave consistently.

### 🔄 Rollback Support
- Store infra files in Git.
- Revert to previous versions if needed.

---

## 🛠️ How IaC Works

- IaC tools allow you to **describe infrastructure in code**.
- The tool reads these definitions and provisions resources automatically.

### 🧾 Example Flow:
1. Write `infra.yaml`
2. Define EC2 + S3 bucket
3. Run deploy command
4. Infrastructure is created

---

## 🧭 IaC Approaches

### 1. Declarative (What to build)
- Define the **end state**.
- Tool figures out the steps.

> _"I want an EC2 instance with 8GB RAM."_

### 2. Imperative (How to build)
- Define **each step** explicitly.

> _"Step 1: Create EC2 → Step 2: Install packages → Step 3: Configure firewall"_

| Approach     | Focus      | Tools                      |
|--------------|------------|----------------------------|
| Declarative  | End Result | Terraform, CloudFormation |
| Imperative   | Steps      | Ansible, Shell Scripts     |

---

## 🤝 IaC in DevOps

- IaC is a **core DevOps practice**.
- Infra changes are stored and tracked like app code (Git).
- Enables CI/CD: Infra deploys with every push or merge.
- Improves Dev + Ops collaboration.

---

## ☁️ AWS Tools for IaC

| Tool              | Language     | Description                                          |
|-------------------|--------------|------------------------------------------------------|
| **CodeCommit**    | Git-based    | Git repository to store IaC code                     |
| **CodePipeline**  | Managed CI/CD| Automate deployments based on repo triggers   


| Tool               | Type        | Language           | Example Use                            |
| ------------------ | ----------- | ------------------ | -------------------------------------- |
| **Terraform**      | Declarative | Own language (HCL) | Build on AWS, Azure, etc. Very popular |
| **OpenTofu**       | Declarative | Same as Terraform  | Free & Open Terraform                  |
| **Pulumi**         | Declarative | Python, JS, etc.   | Use real languages                     |
| **ARM**            | Declarative | JSON               | Native Azure, but hard to read         |
| **Bicep**          | Declarative | Clean Syntax       | Better version of ARM                  |
| **CloudFormation** | Declarative | YAML/JSON          | AWS native                             |
| **AWS CDK**        | Imperative  | Python/JS          | AWS in real code                       |
| **Ansible/Chef**   | Mix         | YAML, DSL          | Manage servers (also infra)            |
|


---

## 📘 Real-Life Example

1. Define EC2 + S3 + Security Groups using AWS CDK (Python)
2. Push the code to AWS CodeCommit
3. CodePipeline runs, deploys infra automatically

---

## 📌 Summary

| Key Concept | Explanation |
|-------------|-------------|
| IaC         | Code-based infra provisioning |
| Declarative | Define desired state |
| Imperative  | Define steps to reach state |
| CI/CD       | Automate infra deploys |
| Git + IaC   | Track infra like app code |

---

> 🔁 Use IaC like you use code: version it, review it, deploy it!

