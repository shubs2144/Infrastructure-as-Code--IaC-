# 📘 AWS CDK Crash Course - 

---

## 🧠 What is AWS CDK?

- **CDK = Cloud Development Kit**
- Use code (Python, JS, TypeScript, etc.) to build AWS infrastructure.
- No need to click around the AWS Console.
- Makes managing infra easier, faster, and less error-prone.

---

## ❓ Why Use CDK?

- Manual setup = slow + error-prone
- CDK = write, deploy, destroy infra using code
- Helps with:
  - Reusability
  - Team collaboration
  - Auto-complete in IDE
  - Version control (Git)

---

## 🔧 Core CDK Concepts

### 🧱 Constructs
- Building blocks for AWS resources. 
- 3 Levels:
  - **L1**: Raw CloudFormation (low-level, more control) 
    - Directly maps to CloudFormation resources
    - More complex, less user-friendly
  - **L2**: Smart defaults (recommended)
    - Preconfigured, easier to use
    - Good balance of control and simplicity
  - **L3**: Ready-made solutions (quick setups)
    - Higher-level abstractions
    - Fast to implement, but less flexible

### 📦 Stack
- A group of related resources.
- Like a container for infra.

### 🧩 App
- A full CDK project.
- Can have one or more stacks.

---

## 🛠️ CDK Development Workflow

- `cdk init` → Create new CDK project
- `cdk synth` → Generate CloudFormation template
- `cdk deploy` → Deploy to AWS
- `cdk destroy` → Delete resources
- `cdk watch` → Auto-deploy on file save

---

## ✅ Best Practices

- Prefer **L2 constructs**: clean, simple, safe
- Use **L3 constructs** for fast setups
- Keep stacks modular for better structure

---

## 🔄 CI/CD Integration

- Use GitHub Actions or other CI/CD tools
- Auto-deploy CDK code when pushed to repo
- Enables team reviews, testing, and safer deployments

---

## 💻 Hands-On Example

- Instructor shows:
  - Setting up CDK project
  - Creating **S3 Bucket**
  - Connecting it to **SQS Queue**
- Code → Deploy → Verify in AWS Console

---

## 📚 Learning Resources

- **Construct Hub**: Browse prebuilt constructs
- Official AWS Docs
- Keep practicing with real setups

---

> 🚀 CDK helps you write infrastructure like application code — version-controlled, automated, and scalable.

## without cdk
![alt text](<Screenshot 2025-07-28 134232.png>)

## with cdk
![alt text](<Screenshot 2025-07-28 134305.png>)