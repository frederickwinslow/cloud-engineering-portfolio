# Azure Entra ID + RBAC + Least Privilege Storage Lab

## 📌 Project Overview

This project demonstrates how **Microsoft Entra ID** and **Azure Role-Based Access Control (RBAC)** can be used to control employee access to Azure Blob Storage.

The lab simulates a company environment where an employee needs access to company documents but should not automatically have access to sensitive financial files.

The project focuses on **identity, authentication, authorization, least privilege, RBAC scope, and access testing**.

---

## 🎯 Objectives

* Create an employee identity using Microsoft Entra ID.
* Authenticate the employee using Microsoft Authenticator MFA.
* Configure Azure RBAC for Blob Storage.
* Test Contributor and Reader permissions.
* Demonstrate the principle of least privilege.
* Restrict permissions to a specific Blob container.
* Test both allowed and denied access.

---

## 🏗️ Architecture

```text
                    Microsoft Entra ID
                           │
                           ▼
                    Cloud Lab User
                           │
                    MFA Authentication
                           │
                           ▼
                      Azure RBAC
                           │
              ┌────────────┴────────────┐
              ▼                         ▼
       company-files              finance-files
       Reader Access                No Access
            ✅                          ❌
```

---

## ☁️ Azure Resources

| Resource        | Configuration               |
| --------------- | --------------------------- |
| Resource Group  | `rg-cloud-lab02`            |
| Storage Account | `stcloudlab02`              |
| Container       | `company-files`             |
| Container       | `finance-files`             |
| Entra ID User   | `Cloud Lab User`            |
| Authentication  | Microsoft Authenticator MFA |

---

## 🔐 Identity and Authentication

A Microsoft Entra ID user named **Cloud Lab User** was used to simulate an employee.

The user successfully authenticated to Azure and completed MFA using the **Microsoft Authenticator** application.

### Authentication flow

```text
Employee
   │
   ▼
Microsoft Entra ID
   │
   ▼
Password Authentication
   │
   ▼
Microsoft Authenticator MFA
   │
   ▼
Authenticated User
```

---

# 🔑 RBAC Testing

## Test 1 — Storage Blob Data Contributor

The employee was initially assigned:

**Storage Blob Data Contributor**

The user was able to:

* Upload a file
* Download a file
* Delete a file
* Perform other permitted Blob data operations

### Result

```text
Upload   → ✅
Download → ✅
Delete   → ✅
```

This demonstrated that the Contributor role provides read and write access to Blob data.

---

# Test 2 — Storage Blob Data Reader

The Contributor role was removed and replaced with:

**Storage Blob Data Reader**

The employee was then tested again.

### Result

```text
Upload   → ❌
Download → ✅
Delete   → ❌
```

The employee could read/download existing Blob data but could not modify or delete it.

This demonstrated the practical difference between **Contributor** and **Reader** permissions.

---

# Test 3 — Container-Level RBAC

The Reader role was then assigned specifically at the:

**`company-files` container**

A second container was created:

**`finance-files`**

The employee was not given equivalent Blob data access to the finance container.

### Final test

| Resource        | Employee Access |
| --------------- | --------------- |
| `company-files` | ✅ Read access   |
| `finance-files` | ❌ No access     |

This demonstrated that RBAC permissions can be restricted to a specific resource scope rather than automatically granting access across the entire storage account.

---

# 🛡️ Least Privilege

The lab demonstrates the principle of **least privilege**.

Instead of giving an employee broad access to the storage account, permissions were restricted to the resource required for their work.

### Example

```text
Broad Access

Employee
   │
   ▼
Entire Storage Account
   │
   ├── company-files
   └── finance-files


Least Privilege

Employee
   │
   ▼
company-files
   │
   └── Reader
```

The second model reduces unnecessary access to sensitive resources.

---

# 🧪 Access Validation

The permissions were validated by performing real operations using the employee account.

| Test                    | Expected     | Result   |
| ----------------------- | ------------ | -------- |
| Employee authentication | MFA required | ✅ Passed |
| Upload with Contributor | Allowed      | ✅ Passed |
| Delete with Contributor | Allowed      | ✅ Passed |
| Download with Reader    | Allowed      | ✅ Passed |
| Upload with Reader      | Denied       | ✅ Passed |
| Delete with Reader      | Denied       | ✅ Passed |
| Access `company-files`  | Allowed      | ✅ Passed |
| Access `finance-files`  | Denied       | ✅ Passed |

---

# 🧠 Key Concepts Demonstrated

### Microsoft Entra ID

Used to provide the employee identity and authentication mechanism.

### Multi-Factor Authentication

Microsoft Authenticator was used as an additional authentication factor.

### Azure RBAC

Used to authorize the employee's access to Azure resources.

### Role-Based Access

Different roles provided different levels of access.

### Least Privilege

The employee received only the permissions required for the assigned task.

### RBAC Scope

Permissions were restricted to a specific Blob container.

### Access Validation

Permissions were tested using actual employee operations.

---

# 🛠️ Technologies Used

* Microsoft Azure
* Microsoft Entra ID
* Azure Role-Based Access Control (RBAC)
* Azure Blob Storage
* Microsoft Authenticator
* Azure Portal

---

# 📚 Skills Demonstrated

* Cloud Identity and Access Management
* Microsoft Entra ID administration
* MFA configuration
* Azure RBAC
* Azure Storage administration
* Blob Storage permissions
* RBAC scope
* Least privilege
* Access control testing
* Azure Portal administration

---

# 💼 Real-World Scenario

This lab represents a common enterprise access-control scenario.

For example, a company employee may need access to general company documents but should not automatically receive access to sensitive financial information.

Using Microsoft Entra ID and Azure RBAC, administrators can assign permissions based on the employee's responsibilities and restrict access to the appropriate resource.

The same approach can be extended to other Azure resources such as virtual machines, databases, Key Vaults, and applications.

---

# 🚀 Future Improvements

Future versions of this project can extend the environment with:

* Azure Virtual Machines
* Microsoft Entra-based VM login
* Azure Key Vault
* Azure Monitor
* Log Analytics
* Azure Policy
* Managed identities
* Resource-group-level RBAC
* Custom RBAC roles
* Automated infrastructure using Terraform

---

## 👤 Author

**Frederick Winslow-Nyanney**

Cloud Engineering & Identity and Access Management Lab
