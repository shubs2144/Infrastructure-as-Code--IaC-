# Terraform 101: Infrastructure as Code (IaC) Basics

## 🌍 **What is Terraform?**

* **Open-source IaC tool** to manage cloud infrastructure.
* Works with **declarative syntax** — you define *what you want*, and Terraform figures out **how to do it**.
* Used for provisioning servers, networks, storage, etc., especially on **clouds like AWS**.
* Maintained by **HashiCorp**.
* Supports **multi-cloud** environments (AWS, Azure, GCP, etc.).

## 📜 **Key Concepts**

* **Providers**: Plugins that allow Terraform to interact with cloud providers (e.g., AWS, Azure).
* **Resources**: The components of your infrastructure (e.g., VMs, networks).
* **Modules**: Containers for multiple resources that are used together.
* **State**: Terraform keeps track of the real-world state of your infrastructure.

---

## 🆚 **Terraform vs. Ansible**

| Feature      | Terraform                       | Ansible                           |
| ------------ | ------------------------------- | --------------------------------- |
| Purpose      | Provision Infrastructure        | Configure Software/Apps           |
| Type         | Declarative                     | Procedural                        |
| When to Use  | Before deployment (infra setup) | After deployment (app setup)      |
| Common Usage | Create VMs, Networks, etc.      | Install packages, manage services |

✅ Many teams use **both together**.

---

## 🧱 **Terraform Architecture**

* **Config files (`.tf`)**: Define what infrastructure you want.
* **State file (`terraform.tfstate`)**: Tracks real-world infra state.
* **Providers**: Plugins to manage cloud resources (e.g., AWS, Azure, GCP).

---

## ⚙️ **Common Terraform Commands**

* `terraform init` – Start project (downloads providers).
* `terraform plan` – Preview changes before applying.
* `terraform apply` – Create/update infrastructure.
* `terraform destroy` – Delete all resources.

---

## ✅ **Why Declarative is Better**

* You **describe the end goal**, not the steps.
* Easier to manage changes — just edit the `.tf` file and re-apply.
* Keeps code **clean, consistent, and repeatable**.


